from fastapi import FastAPI
from .models import UserCreateRequest, UserResponse
from .service import UserService

app = FastAPI()

user_service = UserService()


@app.post("/users", response_model=UserResponse)
def create_user(req: UserCreateRequest) -> UserResponse:
    return create_user(
        name=req.name,
        age=req.age,
        role=req.role
    )

@app.get("/greet")
async def hello():
    return "Hello There"