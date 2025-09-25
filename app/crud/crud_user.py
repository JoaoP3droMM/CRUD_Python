from sqlalchemy.orm import Session
from ..schemas import user_schema
from ..core.security import get_password_hash
from ..models import user_model

# Função para buscar um usuário pelo e-mail
def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

# Função para buscar todos os usuários (com paginação)
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()

# Função para criar um usuário
def create_user(db: Session, user: user_schema.UserCreate):
    # Criptografa a senha
    hashed_password = get_password_hash(user.password)
    
    db_user = user_model.User(
        email=user.email, 
        name=user.name, 
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user) 
    return db_user

# Função para deletar um usuário
def delete_user(db: Session, user_id: int):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        return None 
    
    db.delete(user)
    db.commit()
    return user