from pydantic import BaseModel
from typing import List
from .estabelecimento_schema import Estabelecimento
from .socio_schema import Socio

class EmpresaBase(BaseModel):
    razao_social: str
    cnpj_basico: str
    natureza_juridica: str
    capital_social: float

class EmpresaCreate(EmpresaBase):
    pass

# Schema de resposta, incluindo relacionamentos
class Empresa(EmpresaBase):
    id: int

    estabelecimentos: List[Estabelecimento] = []
    socios: List[Socio] = []

    class Config:
        from_attributes = True