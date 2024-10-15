from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

from app.helpers.enums import UserRole
from app.schemas.sche_base import MappingByFieldName


class UserBase(MappingByFieldName):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True


class UserItemResponse(UserBase):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool
    role: str
    last_login: Optional[datetime]


class UserCreateRequest(UserBase):
    full_name: Optional[str]
    password: str
    email: EmailStr
    is_active: bool = True
    role: UserRole = UserRole.GUEST


class UserRegisterRequest(MappingByFieldName):
    full_name: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.GUEST


class UserUpdateMeRequest(MappingByFieldName):
    full_name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]


class UserUpdateRequest(MappingByFieldName):
    full_name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]
    is_active: Optional[bool] = True
    role: Optional[UserRole]
