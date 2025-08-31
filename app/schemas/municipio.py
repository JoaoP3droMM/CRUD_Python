from pydantic import BaseModel
from typing import List

class MunicipioBase(BaseModel):
    id: int
    desc: str

class MunicipioCreate(MunicipioBase):
    pass

class Municipio(MunicipioBase):
    id: int

    class Config:
        from_attributes = True