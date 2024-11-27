import json
import logging
from datetime import datetime
from typing import Optional
from fastapi import Depends, HTTPException, APIRouter, Security, Header
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse
from app.api.models import UserLogin, UserResponse
from app.utils.access_control import (authenticate_user, access_security, refresh_security, redis_conn,
                                      ACCESS_TOKEN_EXPIRE_SECONDS, REFRESH_TOKEN_EXPIRE_SECONDS)
from app.core.database.models import User
from app.core.database.session import SessionLocal
from fastapi_jwt import (
    JwtAccessBearerCookie,
    JwtAuthorizationCredentials,
    JwtRefreshBearer,
)

router = APIRouter()


@router.post("/login")
def login_and_get_tokens(user_login: UserLogin):
    user = authenticate_user(user_login.username, user_login.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        session = SessionLocal()
        current_user = session.query(User).filter(User.username == user_login.username).first()
        returnResult = {}
        if current_user:
            subject = {"username": user_login.username}
            access_token = access_security.create_access_token(subject=subject)
            returnResult["access_token"] = access_token
            refresh_token = refresh_security.create_refresh_token(subject=subject)
            returnResult["refresh_token"] = refresh_token
            returnResult["token_type"] = "bearer"

        return JSONResponse({"data": returnResult})
    except Exception as e:
        logging.error(f"Error getting User for Authentication: {e}")
        session.rollback()  # Rollback the transaction on error
        raise e
    finally:
        # Close the session
        session.close()


@router.post('/refreshToken')
def regenerate_access_token(credentials: JwtAuthorizationCredentials = Security(refresh_security)):
    access_token = access_security.create_access_token(subject=credentials.subject)

    return JSONResponse({
        "data": {"access_token": access_token},
        "message": "Token refreshed successfully"
    })


@router.delete('/logout')
def logout_and_revoke_tokens(refresh_token: Optional[str] = None,
                             authorization: Optional[str] = Header(None),
                             credentials: JwtAuthorizationCredentials = Depends(access_security)):
    """Store both access and refresh tokens in Redis with a value of true to indicate revocation. Additionally,
    we set an expiry time on these tokens in Redis, ensuring they are automatically removed after expiration."""

    if not credentials:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if not authorization:
        raise HTTPException(status_code=400, detail="Access token is required in the Authorization header")
    access_token = authorization.split(" ")[1]
    redis_conn.set(access_token, "blacklisted", ex=ACCESS_TOKEN_EXPIRE_SECONDS)
    if refresh_token:
        refresh_decoded = refresh_security.decode_jwt(refresh_token)
        refresh_expires_in = refresh_decoded["exp"] - int(datetime.utcnow().timestamp())
        redis_conn.set(refresh_token, "blacklisted", ex=refresh_expires_in)

    return JSONResponse({"message": "Logged out successfully"})
