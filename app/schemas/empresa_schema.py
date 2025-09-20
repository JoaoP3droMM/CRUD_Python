from pydantic import BaseModel, Field
from typing import Optional

class EmpresaResponseSchema:
    nome_fantasia: str = Field(..., description="Nome fantasia da empresa")
    tipo_logradouro: str = Field(..., description="Tipo do logradouro (Rua, Av, etc.)")
    logradouro: str = Field(..., description="Nome do logradouro")
    numero: str = Field(..., description="Número do endereço")
    complemento: Optional[str] = Field(None, description="Complemento do endereço")
    bairro: str = Field(..., description="Bairro")
    uf: str = Field(..., max_length=2, description="Unidade Federativa (Estado)")
    cep: str = Field(..., description="CEP", example="12345-678")

    class Config:
        schema_extra = {
            "example": {
                "nome_fantasia": "Tech Solutions LTDA",
                "tipo_logradouro": "Rua",
                "logradouro": "das Palmeiras",
                "numero": "123",
                "complemento": "Sala 45",
                "bairro": "Centro",
                "uf": "SP", 
                "cep": "01234-567"
            }
        }