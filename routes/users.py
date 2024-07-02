from fastapi import APIRouter, HTTPException, Depends
from ..models.schemas import UserCreate, UserResponse
from ..models._1models import User

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register_user(user: UserCreate):
    user = User(**user.dict())
    await user.create()
    return user
