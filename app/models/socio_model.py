from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base
from .associations import empresa_socio_association

class Socio(Base):
    __tablename__ = 'socio'
    
    id = Column(Integer, primary_key=True)

    cnpj_basico: Column(Integer)
    identificador_socio: Column(Integer)
    nome_socio: Column(String())
    cpf: Column(Integer)
    qualificacao: Column(Integer)
    data_entrada: Column(String())
    pais: Column(Integer)
    representante_legal: Column(Integer)
    nome_representante: Column(String())
    qualificacao_representante: Column(Integer)
    faixa_etaria: Column(Integer)
    
    # Relação de volta para a Empresa
    empresas = relationship(
        'Empresa',
        secondary=empresa_socio_association,
        back_populates='socios'
    )