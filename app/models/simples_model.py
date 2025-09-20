from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base
from .associations import empresa_socio_association

class Simples(Base):
    __tablename__ = "simples"

    id = Column(Integer, primary_key=True)

    cnpj_basico: Column(Integer)
    optante: Column(String(), nullable=True)
    data_opcao: Column(String(), nullable=True)
    data_exclusao: Column(String(), nullable=True)
    optante_mei: Column(String(), nullable=True)
    data_opcao_mei: Column(String(), nullable=True)
    data_exclusao_mei: Column(String(), nullable=True)