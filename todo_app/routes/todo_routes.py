from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from ..database.database import db
from ..models.models import Todo, TodoResponse, TodoUpdate, TodoUpdateResponse
from ..raw_sql import queries

router = APIRouter()


@router.post("/todos")
def create_todo(todo: Todo):
    new_todo = TodoResponse(
        **todo.model_dump(),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    with db.get_cursor() as cursor:
        cursor.execute(queries.CREATE_TODO, (todo.title, todo.user_id))

    return {
        "success": True,
        "data": new_todo,
        "message": "Todo created successfully"
    }


@router.patch("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoUpdate):

    with db.get_cursor() as cursor:
        cursor.execute(queries.UPDATE_TODO, (todo.title, todo_id))

    updated_todo = TodoUpdateResponse(
        **todo.model_dump(),
        updated_at=datetime.now()
    )

    return {
        "success": True,
        "data": updated_todo,
        "message": "Todo updated successfully"
    }
    
    
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if not todo_id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid todo ID"
        )

    with db.get_cursor() as cursor:
        cursor.execute(queries.DELETE_TODO, (todo_id,))

    return {
        "success": True,
        "message": "Todo deleted successfully"
    }