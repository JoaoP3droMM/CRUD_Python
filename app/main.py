from fastapi import FastAPI
from .database import engine, Base
from .routers import user_router
from .models import user_model, empresa_model, estabelecimento_model, socio_model, associations
from .schemas import filter_schema,empresa_schema,token_schema,user_schema

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Minha API com FastAPI',
    version='1.0.0'
)

# Incluir as rotas da aplicação aqui
app.include_router(user_router.router)

@app.get('/')
def read_root():
    return {'message': 'Bem-vindo à API!'}

@app.post("/empresas/consultar")
async def consultar_empresas(filtro: filter_schema.Filter):
    """
    Consultar empresas próximas baseado no CEP e no CNAE.
    """
    