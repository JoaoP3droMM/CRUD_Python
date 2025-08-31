from pydantic import BaseModel
from typing import List

class NaturezaBase(BaseModel):
    id: int
    desc: str

class NaturezaCreate(NaturezaBase):
    pass

class Natureza(NaturezaBase):
    id: int

    class Config:
        from_attributes = True