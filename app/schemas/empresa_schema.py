from pydantic import BaseModel
from typing import List
from .estabelecimento_schema import Estabelecimento
from .socio_schema import Socio

class EmpresaBase(BaseModel):
    cnpj_basico: int
    razao_social: str | None
    natureza_juridica: int
    qualificacao_responsavel: str | None
    capital_social: float | None
    porte: int
    ente_federativo_responsavel: int | None

class EmpresaCreate(EmpresaBase):
    pass

# Schema de resposta, incluindo relacionamentos
class Empresa(EmpresaBase):
    id: int

    estabelecimentos: List[Estabelecimento] = []
    socios: List[Socio] = []

    class Config:
        from_attributes = True