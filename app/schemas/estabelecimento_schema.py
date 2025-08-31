from pydantic import BaseModel
from datetime import date int | None

class EstabelecimentoBase(BaseModel):
    cnpj_basico: int
    cnpj_ordem: int
    cnpj_dv: int
    identificador: int
    nome_fantasia: str | None
    situacao_cadastral: int
    data_situacao_cadastral: str
    motivo_situacao_cadastral: int
    nome_cidade_exterior: str
    pais: str
    data_inicio_atividade: str
    cnae_principal: int
    cnaes_secundarios: str
    tipo_logradouro: str
    lougradouro: str
    numero: int | None
    complemento: str | None
    bairro: str | None
    cep int | None
    uf: str | None
    municipio int | None
    ddd_1 int | None
    telefone_1 int | None
    ddd_2 int | None
    telefone_2 int | None
    ddd_fax int | None
    fax int | None
    email: str | None
    situacao_especial: str | None
    data_situacao_especial: str | None

class EstabelecimentoCreate(EstabelecimentoBase):
    pass

class Estabelecimento(EstabelecimentoBase):
    id: int

    class Config:
        from_attributes = True