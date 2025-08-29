from SQLAlchemy import Table, Column, Integer, ForeignKey
from SQLAlchemy.orm import relationship
from config import db
from .associations_model import empresa_socio_assiciation

# Cria tabela de sócios
class Socio(db.Model):
    __tablename__ = 'socios'
    
    id = Column(Integer, primary_key=True)
    nome_socio = Column(String(255), index=True)
    documento_socio = Column(String(14), unique=True) 
    qualificacao_socio = Column(String(100))
    
    # Relacionamento com Empresa
    empresas = relationship('Empresa', secondary=empresa_socio_association, back_populates='socios')