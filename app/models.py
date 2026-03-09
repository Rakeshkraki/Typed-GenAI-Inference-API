from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Literal


class UserCreateRequest(BaseModel):
    model_config = ConfigDict(strict=True)
    name: str
    age: int
    email : EmailStr
    role: Literal["admin", "user"]


class UserResponse(BaseModel):
    name: str
    email : EmailStr
    age : int
    role: Literal["admin", "user"]