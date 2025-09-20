from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base
from .associations import empresa_socio_association

class CNAE:
    __tablename__ = "cnae"

    id: Column(Integer, primary_key=True)

    descricao: Column(String())