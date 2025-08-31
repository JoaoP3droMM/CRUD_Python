from sqlalchemy import Table, Column, Integer, ForeignKey
from ..database import Base

empresa_socio_association = Table(
    'empresa_socio',
    Base.metadata,
    Column('empresa_id', Integer, ForeignKey('empresas.id'), primary_key=True),
    Column('socio_id', Integer, ForeignKey('socios.id'), primary_key=True)
)