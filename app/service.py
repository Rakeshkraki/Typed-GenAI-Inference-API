from uuid import uuid4

from sqlalchemy import UUID
from sqlalchemy.orm import Session

from .db_models import User
from .models import UserResponse, UserCreateRequest
from typing import Literal
from pydantic import EmailStr

class UserService:
    def create_user(self, db:Session , name: str, email : EmailStr, age: int, role:  Literal["admin", "user"]) -> UserResponse:
        user_id = UUID  # pretend DB insert

        db_user = UserCreateRequest(name=name,email = email, age=age, role=role)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return UserResponse(
            name=name,
            email = email,
            age=age,
            role=role
        )

    def create_user(
            self,
            db: Session,
            name: str,
            email: EmailStr,
            age: int,
            role: Literal["admin", "user"]
    ) -> UserResponse:
        user_id = str(uuid4())

        db_user = User(
            id=user_id,
            name=name,
            email=email,
            age=age,
            role=role
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return UserResponse(
            name=db_user.name,
            email=db_user.email,
            age=db_user.age,
            role=db_user.role
        )

    def get_all_users(self, db: Session) -> list[UserResponse]:
        users = db.query(UserCreateRequest).all()

        return [
            UserResponse(id=user.id, name=user.name, email=user.email, age=user.age, role=user.role )
            for user in users
        ]

