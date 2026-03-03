from .models import UserResponse
from typing import Literal
from pydantic import EmailStr

class UserService:
    def create_user(self, name: str, email : EmailStr, age: int, role:  Literal["admin", "user"]) -> UserResponse:
        user_id: int = 1  # pretend DB insert

        return UserResponse(
            id=user_id,
            name=name,
            email = email,
            age=age,
            role=role
        )

