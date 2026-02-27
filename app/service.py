from .models import UserResponse
from typing import Literal

class UserService:
    def create_user(self, name: str, age: int, role:  Literal["admin", "user"]) -> UserResponse:
        user_id: int = 1  # pretend DB insert

        return UserResponse(
            id=user_id,
            name=name,
            age=age,
            role=role
        )

