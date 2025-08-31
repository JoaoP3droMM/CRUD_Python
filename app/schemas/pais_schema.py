from pydantic import BaseModel
from typing import List

class PaisBase(BaseModel):
    id: int
    desc: str

class PaisCreate(PaisBase):
    pass

class Pais(PaisBase):
    id: int

    class Config:
        from_attributes = True