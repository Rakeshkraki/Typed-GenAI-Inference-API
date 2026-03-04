from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base
from pydantic import EmailStr

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email : Mapped[EmailStr] = mapped_column(String, unique=True, nullable=True)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)