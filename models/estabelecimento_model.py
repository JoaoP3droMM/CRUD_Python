from SQLAlchemy import Table, Column, Integer, ForeignKey
from SQLAlchemy.orm import relationship
from config import db

# Cria tabela de estabelecimento
class Estabelecimento(db.Model):
    __tablename__ = 'estabelecimentos'

    id = Column(Integer, primary_key=True)
    cnpj_completo = Column(String(14), unique=True, nullable=False, index=True) 
    nome_fantasia = Column(String(255))
    situacao_cadastral = Column(String(50))
    data_inicio_atividade = Column(Date)
    cnae_fiscal_principal = Column(String(7))
    uf = Column(String(2))
    municipio = Column(String(100))

    # Chave estrangeira para relacionamento
    empresa_id = Column(Integer, ForeignKey('empresas.id'), nullable=False)

    empresa = relationship('Empresa', back_populates='estabelecimentos')