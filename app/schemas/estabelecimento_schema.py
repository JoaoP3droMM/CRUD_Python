from pydantic import BaseModel
from datetime import date

class EstabelecimentoBase(BaseModel):
    cnpj_completo: str
    nome_fantasia: str | None = None
    situacao_cadastral: str
    data_inicio_atividade: date | None = None
    cnae_fiscal_principal: str
    uf: str
    municipio: str

class EstabelecimentoCreate(EstabelecimentoBase):
    pass

class Estabelecimento(EstabelecimentoBase):
    id: int
    empresa_id: int

    class Config:
        from_attributes = True