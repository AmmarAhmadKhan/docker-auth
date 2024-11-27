import logging
import os
from datetime import timedelta
from typing import List
from fastapi import HTTPException, Depends, Header
from fastapi import Security
from passlib.context import CryptContext
from starlette import status
from app.core.database.models import User
from app.core.database.session import SessionLocal
from fastapi_jwt import (
    JwtAccessBearerCookie,
    JwtAuthorizationCredentials,
    JwtRefreshBearer,
)
from redis import Redis

SECRET_KEY = os.getenv("SECRET_KEY")
ACCESS_TOKEN_EXPIRE_SECONDS = 15 * 60
REFRESH_TOKEN_EXPIRE_SECONDS = 5 * 24 * 60 * 60  # Number of seconds for refresh token expiry

redis_conn = Redis(host="apibus-redis", port=6379, decode_responses=True)

access_security = JwtAccessBearerCookie(
    secret_key=SECRET_KEY,
    auto_error=True,
    access_expires_delta=timedelta(seconds=ACCESS_TOKEN_EXPIRE_SECONDS)
)
refresh_security = JwtRefreshBearer(
    secret_key=SECRET_KEY,
    auto_error=True,
    refresh_expires_delta=timedelta(seconds=REFRESH_TOKEN_EXPIRE_SECONDS)
)

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def authenticate_user(username: str, password: str):
    """Authenticate user by using username and user password"""
    if not username:
        return None
    try:
        session = SessionLocal()
        db_user = session.query(User).filter(User.username == username).first()
        if not pwd_context.verify(password, db_user.password):
            return None
        return db_user
    except Exception as e:
        logging.error(f"Error getting User for Authentication: {e}")
        session.rollback()  # Rollback the transaction on error
        raise e
    finally:
        # Close the session
        session.close()


def get_current_user_by_jwt(
        credentials: JwtAuthorizationCredentials = Security(access_security),
        authorization: str = Header(None)  # Extract token from the Authorization header
):
    """Dependency for API endpoints to authorize access tokens and retrieve the current user."""
    if not credentials:
        raise HTTPException(status_code=401, detail="Unauthorized")

    current_user_name = credentials["username"]

    # Extract the raw JWT token (the one passed in the Authorization header)
    if not authorization:
        raise HTTPException(status_code=400, detail="Access token is required in the Authorization header")

    # Extract access token (Authorization: Bearer <access_token>)
    try:
        access_token = authorization.split(" ")[1]  # Assuming "Bearer <token>"
    except IndexError:
        raise HTTPException(status_code=400, detail="Invalid Authorization header format")

    if redis_conn.get(access_token):
        raise HTTPException(status_code=401, detail="User has already Logged Out")

    try:
        session = SessionLocal()
        db_user = session.query(User).filter(User.username == current_user_name).first()
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
            )
        return db_user
    except Exception as e:
        logging.error(f"Error getting User for Authentication: {e}")
        session.rollback()  # Rollback the transaction on error
        raise e
    finally:
        # Close the session to prevent memory leaks
        session.close()


class RoleChecker:
    """Dependency for Assigning and Verifying allowed roles for different endpoints"""

    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user=Depends(get_current_user_by_jwt)):
        if user.level not in self.allowed_roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted")
