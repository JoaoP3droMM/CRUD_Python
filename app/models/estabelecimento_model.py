from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Estabelecimento(Base):
    __tablename__ = 'estabelecimentos'
    
    id = Column(Integer, primary_key=True)

    cnpj_basico: Column(Integer)
    cnpj_ordem: Column(Integer)
    cnpj_dv: Column(Integer)
    identificador: Column(Integer)
    nome_fantasia: Column(String(), nullable=True)
    situacao_cadastral: Column(Integer)
    data_situacao_cadastral: Column(String())
    motivo_situacao_cadastral: Column(Integer)
    nome_cidade_exterior: Column(String())
    pais: Column(String())
    data_inicio_atividade: Column(String())
    cnae_principal: Column(Integer)
    cnaes_secundarios: Column(String())
    tipo_logradouro: Column(String())
    lougradouro: Column(String())
    numero: Column(Integer, nullable=True)
    complemento: Column(String(), nullable=True)
    bairro: Column(String(), nullable=True)
    cep: Column(Integer, nullable=True)
    uf: Column(String(), nullable=True)
    municipio: Column(Integer, nullable=True)
    ddd_1: Column(Integer, nullable=True)
    telefone_1: Column(Integer, nullable=True)
    ddd_2: Column(Integer, nullable=True)
    telefone_2: Column(Integer, nullable=True)
    ddd_fax: Column(Integer, nullable=True)
    fax: Column(Integer, nullable=True)
    email: Column(String(), nullable=True)
    situacao_especial: Column(String(), nullable=True)
    data_situacao_especial: Column(String(), nullable=True)

    # Chave estrangeira que cria o link com a tabela 'empresas'
    empresa_id = Column(Integer, ForeignKey('empresas.id'), nullable=False)
    
    # Relação de volta para a Empresa
    empresa = relationship('Empresa', back_populates='estabelecimentos')