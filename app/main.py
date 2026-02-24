from fastapi import FastAPI
from .models import UserCreateRequest, UserResponse
from .service import UserService

app = FastAPI()

user_service = UserService()


@app.post("/users", response_model=UserResponse)
def create_user(req: UserCreateRequest) -> UserResponse:
    return user_service.create_user(
        name=req.name,
        age=req.age,
        role=req.role
    )
