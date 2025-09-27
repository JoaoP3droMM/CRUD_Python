from pydantic import BaseModel, Field
from typing import Optional

class Filter(BaseModel):
    cnae: int = Field(..., description="código CNAE da empresa", examples=6541300)
    cep: int = Field(..., description="seu CEP ou parte dele", examples=70040250)

    class Config:
        schema_extra = {
            "example": {
                "cnae": 6541300,
                "cep": 70040250
            }
        }