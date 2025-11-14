from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from ..database.database import db
from ..raw_sql import queries
from ..models.models import User, UserResponse, UserUpdate, UserUpdateResponse

router = APIRouter()


@router.post("/users")
def create_user(user: User):
    new_user = UserResponse(
        **user.model_dump(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    with db.get_cursor() as cursor:
        cursor.execute(queries.CREATE_USER, (user.username, user.email, user.password))

    return {
        "success": True,
        "data": new_user,
        "message": "User created successfully"
    }


@router.patch("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid user input"
        )

    with db.get_cursor() as cursor:
        cursor.execute(
            queries.UPDATE_USER,
            (user.username, user.email, user.password, user_id)
        )

    updated_user = UserUpdateResponse(
        **user.model_dump(),
        updated_at=datetime.now()
    )

    return {
        "success": True,
        "data": updated_user,
        "message": "User updated successfully"
    }


@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid user ID"
        )

    with db.get_cursor() as cursor:
        cursor.execute(queries.DELETE_USER, (user_id,))

    return {
        "success": True,
        "message": "User deleted successfully"
    }
