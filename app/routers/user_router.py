from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..schemas import user_schema
from ..database import get_db
from ..services import user_services

router = APIRouter(
    prefix="/users",
    tags=["Users"]  
)

@router.post("/", response_model=user_schema.User, status_code=201)
def add_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_services.add_user(user, db)

@router.get("/", response_model=List[user_schema.User])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return user_services.list_users(db, skip=skip, limit=limit)

@router.delete("/{user_id}", response_model=user_schema.User)
def remove_user(user_id: int, db: Session = Depends(get_db)):
    return user_services.remove_user(user_id, db)
