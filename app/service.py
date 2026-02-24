from .models import UserResponse


class UserService:
    def create_user(self, name: str, age: int, role: str) -> UserResponse:
        user_id: int = 1  # pretend DB insert

        return UserResponse(
            id=user_id,
            name=name,
            role=role
        )