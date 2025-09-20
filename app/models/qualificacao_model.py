from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base
from .associations import empresa_socio_association

class Pais:
    __tablename__ = "qualificacao"

    id: Column(Integer, primary_key=True)

    desc: Column(String())