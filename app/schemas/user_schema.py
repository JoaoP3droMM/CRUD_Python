from pydantic import BaseModel, EmailStr
from enum import Enum

# Tipos de usuário
class UserRole(str, Enum):
    admin = 'admin'
    leitor = 'leitor'

# Campos compartilhados
class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole = UserRole.leitor

# Criação de usuário (recebe a senha)
class UserCreate(UserBase):
    password: str

# Lê o usuário
class User(UserBase):
    id: int

    # Configuração para o pydantic entender o modelo do ORM
    class Config:
        from_attributes = True