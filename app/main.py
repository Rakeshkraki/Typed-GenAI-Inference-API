from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from .models import UserCreateRequest, UserResponse
from .service import UserService
from .db_models import Base

app = FastAPI()

user_service = UserService()

Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users", response_model=UserResponse)
def create_user(
    req: UserCreateRequest,
    db: Session = Depends(get_db)
) -> UserResponse:

    return user_service.create_user(
        db=db,
        name=req.name,
        email=req.email,
        age=req.age,
        role=req.role
    )


@app.get("/users", response_model=list[UserResponse])
def get_all_users(
    db: Session = Depends(get_db)
) -> list[UserResponse]:

    return user_service.get_all_users(db=db)