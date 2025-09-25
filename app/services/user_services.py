from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import user_schema
from ..crud import crud_user

def add_user(user: user_schema.UserCreate, db: Session) -> user_schema.User:
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")
    
    return crud_user.create_user(db=db, user=user)

def list_users(db: Session, skip: int = 0, limit: int = 100) -> List[user_schema.User]:
    return crud_user.get_users(db, skip=skip, limit=limit)

def remove_user(user_id: int, db: Session) -> user_schema.User:
    user = crud_user.delete_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return user

def get_user_by_email(db: Session, email: str) -> user_schema.User:
    return crud_user.get_user_by_email(db, email=email)
