from typing import List, Optional, Dict
from pydantic import BaseModel, PositiveInt, validator
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

    @validator('password_updated', pre=True, always=True)
    def isoformat_password_updated(cls, v):
        if isinstance(v, datetime):
            return v.isoformat()
        return v

    class Config:
        orm_mode = True


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


class AutomatonCreate(BaseModel):
    name: str
    description: Optional[str] = None
    node_details: List[dict]
    connection_details: List[dict]


class AutomatonResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    node_details: Optional[List[dict]]
    connection_details: Optional[List[dict]]
    creator: UserResponse
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
