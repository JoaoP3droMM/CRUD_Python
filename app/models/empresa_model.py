from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..database import Base
from .associations import empresa_socio_association

class Empresa(Base):
    __tablename__ = 'empresas'

    id = Column(Integer, primary_key=True)

    cnpj_basico: Column(String(), unique=True, nullable=False, index=True)
    razao_social: Column(String(), nullable=False)
    natureza_juridica: Column(Integer)
    qualificacao_responsavel: Column(String(), nullable=True)
    capital_social: Column(Float)
    porte: Column(Integer)
    ente_federativo_responsavel: Column(Integer)

    # Relacionamento 1:N com Estabelecimento
    estabelecimentos = relationship('Estabelecimento', back_populates='empresa', cascade='all, delete-orphan')

    # Relacionamento N:N com Sócio
    socios = relationship(
        'Socio',
        secondary=empresa_socio_association,
        back_populates='empresas'
    )