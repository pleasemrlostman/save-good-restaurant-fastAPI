# app/user/controllers/user_controller.py
from fastapi import APIRouter, HTTPException
from app.user.services.user_service import UserService
from app.user.models.user import User
from typing import List

router = APIRouter()
user_service = UserService()

@router.get("/{user_id}")
def read_user(user_id: str):
    user = user_service.get_user(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/")
def create_user(user: User):
    created_user_id = user_service.create_user(user)
    return {"message": "User created successfully", "user_id": created_user_id}

@router.get("/")
def read_all_users() -> List[User]:
    return user_service.get_all_users()