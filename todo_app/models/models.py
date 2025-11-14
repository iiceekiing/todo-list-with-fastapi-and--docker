from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(User):
    created_at: Optional[str]
    updated_at: Optional[str]


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class UserUpdateResponse(UserUpdate):
    updated_at: Optional[str]


class Todo(BaseModel):
    title: str
    user_id: int


class TodoResponse(Todo):
    created_at: Optional[str]
    updated_at: Optional[str]


class TodoUpdate(BaseModel):
    title: Optional[str] = None


class TodoUpdateResponse(TodoUpdate):
    updated_at: Optional[str]
