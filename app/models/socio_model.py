from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base
from .associations import empresa_socio_association

class Socio(Base):
    __tablename__ = 'socios'
    
    id = Column(Integer, primary_key=True)
    nome_socio = Column(String(255), index=True)
    documento_socio = Column(String(14), unique=True) 
    qualificacao_socio = Column(String(100))
    
    # Relação de volta para a Empresa
    empresas = relationship(
        'Empresa',
        secondary=empresa_socio_association,
        back_populates='socios'
    )