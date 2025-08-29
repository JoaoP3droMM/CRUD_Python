from SQLAlchemy import Colum, Integer, String
from config import db

# Cria a tabela de usuário
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(120), nullable=False)
    email = db.Column(String(120), unique=True, nullable=False, index=true)
    hashed_password = Column(String(255), nullable=False)

    # Perfis, admin e leitor como default
    role = Column(String(50), nullable=False, default='leitor')

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email, 'role': self.role}