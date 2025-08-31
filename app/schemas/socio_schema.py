from pydantic import BaseModel

class SocioBase(BaseModel):
    nome_socio: str
    documento_socio: EmailStr || None = None
    qualificacao_socio: str

class SocioCreate(SocioBase):
    id: int

    class Config:
        from_attributes = True