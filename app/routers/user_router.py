from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import user_schema
from ..crud import crud_user
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]  
)

@router.post("/", response_model=user_schema.User, status_code=201)
def add_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")
    
    return crud_user.create_user(db=db, user=user)

@router.get("/", response_model=List[user_schema.User])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users

@router.delete("/{user_id}", response_model=user_schema.User)
def remove_user(user_id: int, db: Session = Depends(get_db)):
    user = crud_user.delete_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return user