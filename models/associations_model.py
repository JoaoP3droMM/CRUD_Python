from sqlalchemy import Table, Column, Integer, ForeignKey
from config import db

# Cria a tabela de empresa e sócio
empresa_socio_assiciation = Table('empresa_socio', db.metadata, 
    Column('empresa_id', Integer, ForeignKey('empresas.id'), primary_key=True),
    Column('socio_id', Integer, ForeignKey('socios.id'), primary_key=True)
)