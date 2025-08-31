from pydantic import BaseModel
from typing import List

class CNAEBase(BaseModel):
    id: int
    desc: str

class CNAECreate(CNAEBase):
    pass

class CNAE(CNAEBase):
    id: int

    class Config:
        from_attributes = True