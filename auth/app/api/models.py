import logging
from ipaddress import IPv4Address
from typing import List, Optional, Dict
from pydantic import BaseModel, PositiveInt, validator, field_validator
from datetime import datetime, date


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    full_name: Optional[str]
    level: int
    email: Optional[str]
    active: int
    mobile: Optional[str]
    password_updated: str

    @field_validator('password_updated', mode='before')
    def isoformat_password_updated(cls, value):
        if isinstance(value, datetime):
            return value.isoformat()
        return value

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    full_name: str
    password: str
    level: int
    email: str = None
    active: int = 1
    mobile: str = None


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    password: Optional[str] = None
    level: Optional[int] = None
    email: Optional[str] = None
    active: Optional[int] = None
    mobile: Optional[str] = None


class PaginationIn(BaseModel):
    page_no: Optional[PositiveInt] = 1
    limit: Optional[int] = 10


class HealthResponse(BaseModel):
    status: str


