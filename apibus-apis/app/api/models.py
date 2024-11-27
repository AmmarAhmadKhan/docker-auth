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


class APIConfigCreate(BaseModel):
    type: str
    url: str
    ip: IPv4Address
    port: str
    api_key: str
    api_doc_url: Optional[str]
    status: str

    @field_validator('ip', mode='after')
    def convert_ip_to_string(cls, value):
        return str(value)

    @field_validator('type')
    def validate_type(cls, value):
        allowed_types = {'phpipam', 'corero'}
        if value not in allowed_types:
            raise ValueError(f"Invalid type: {value}. Allowed values are {allowed_types}.")
        return value

    @field_validator('status')
    def validate_status(cls, value):
        allowed_statuses = {'enabled', 'disabled', 'suspended'}
        if value not in allowed_statuses:
            raise ValueError(f"Invalid status: {value}. Allowed values are {allowed_statuses}.")
        return value

    class Config:
        from_attributes = True


class APIConfigResponse(BaseModel):
    type: str
    url: str
    ip: str
    port: str
    api_key: str
    api_doc_url: Optional[str]
    status: str

    class Config:
        orm_mode = True
