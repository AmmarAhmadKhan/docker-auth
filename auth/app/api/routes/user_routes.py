from typing import List
from fastapi import APIRouter, HTTPException, Query, Depends, Security
from app.api.models import UserLogin, UserResponse, UserCreate, UserUpdate
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from app.utils.access_control import RoleChecker, get_current_user_by_jwt
from starlette import status
from app.core.database.models import User
from app.core.database.session import SessionLocal

router = APIRouter()
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

allow_admin_user = RoleChecker([0])


@router.post("", dependencies=[Depends(allow_admin_user)])
async def create_user(user: UserCreate,
                      current_user=Depends(get_current_user_by_jwt)):
    session = SessionLocal()
    already_existing_user = session.query(User).filter(User.username == user.username).first()
    if already_existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User '{user.username}' already exists")

    db_user = User(
        username=user.username,
        full_name=user.full_name,
        password=pwd_context.hash(user.password),
        level=user.level,
        email=user.email,
        active=user.active,
        mobile=user.mobile
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return JSONResponse(content="User Created Successfully")


@router.get("", response_model=List[UserResponse], dependencies=[Depends(allow_admin_user)])
async def get_users_list(current_user=Depends(get_current_user_by_jwt)):
    session = SessionLocal()
    users = session.query(User).all()
    return users


@router.get("/me")
async def get_current_user(current_user=Depends(get_current_user_by_jwt)):
    return current_user


@router.get("/{username}", response_model=UserResponse, dependencies=[Depends(allow_admin_user)])
async def get_user(username: str, current_user=Depends(get_current_user_by_jwt)):
    session = SessionLocal()
    db_user = session.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.patch("/{id}", dependencies=[Depends(allow_admin_user)])
def update_user(id: int, user_update: UserUpdate,
                current_user=Depends(get_current_user_by_jwt)):
    session = SessionLocal()
    db_user = session.query(User).filter(User.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for attr, value in user_update.dict(exclude_unset=True, exclude_none=True).items():
        if attr == "password":
            value = pwd_context.hash(value)
        setattr(db_user, attr, value)

    session.commit()
    session.refresh(db_user)
    return JSONResponse(content="User Updated Successfully")


@router.delete("/{id}", dependencies=[Depends(allow_admin_user)])
async def delete_user_by_id(id: int, current_user=Depends(get_current_user_by_jwt)):
    session = SessionLocal()
    db_user = session.query(User).filter(User.id == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    try:
        session.delete(db_user)
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete user")
    finally:
        session.close()

    return {"detail": "User deleted successfully"}
