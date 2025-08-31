from pydantic import BaseModel

class SocioBase(BaseModel):
    cnpj_basico: int
    identificador_socio: int
    nome_socio: str
    cpf: int
    qualificacao: int
    data_entrada: str
    pais: int
    representante_legal: int
    nome_representante: str
    qualificacao_representante: int
    faixa_etaria: int

class SocioCreate(SocioBase):
    id: int

    class Config:
        from_attributes = True