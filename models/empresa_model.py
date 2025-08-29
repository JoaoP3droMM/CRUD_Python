from SQLAlchemy import Table, Column, Integer, ForeignKey
from config import db

# Cria tabela de empresas
class Empresa(db.Model):
    __tablename__ = 'empresas'

    id = Column(Integer, primary_key=True)
    cnpj_basico = Column(String(8), unique=True, nullable=False, index=True)
    razao_social = Column(String(255), nullable=False)
    natureza_juridica = Column(String(100))
    capital_social = Column(Float)

    # Relacionamento com estabelecimento
    estabelecimentos = relationship('Estabelecimento', back_populates='empresa', cascade='all, delete-orphan')

    # Relacionamento com os socios
    socios = relationship('Socio', secondary=empresa_socio_association, back_populates='empresas')