from pydantic import BaseModel, ConfigDict
from typing import Literal


class UserCreateRequest(BaseModel):
    model_config = ConfigDict(strict=True)
    name: str
    age: int
    role: Literal["admin", "user"]


class UserResponse(BaseModel):
    id: int
    name: str
    age : int
    role: Literal["admin", "user"]