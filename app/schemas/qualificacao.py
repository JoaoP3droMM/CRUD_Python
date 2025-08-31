from pydantic import BaseModel
from typing import List

class QualificacaoBase(BaseModel):
    id: int
    desc: str

class QualificacaoCreate(QualificacaoBase):
    pass

class Qualificacao(QualificacaoBase):
    id: int

    class Config:
        from_attributes = True