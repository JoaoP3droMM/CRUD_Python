from pydantic import BaseModel
from typing import List

class SimplesBase(BaseModel):
    cnpj_basico: int
    optante: str | None
    data_opcao: str | None
    data_exclusao: str | None
    optante_mei: str | None
    data_opcao_mei: str | None
    data_exclusao_mei: str | None

class SimplesCreate(SimplesBase):
    pass

class Simples(SimplesBase):
    id: int

    class Config:
        from_attributes = True