from fastapi import FastAPI
from .database import engine, Base
from .auth.routes.auth_router import auth_router
from .routers import user_router
from .models import user_model, empresa_model, estabelecimento_model, socio_model, associations

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Minha API com FastAPI',
    version='1.0.0'
)

# Incluir as rotas da aplicação aqui
app.include_router(auth_router, prefix='/api')
app.include_router(user_router.router, prefix='/api', tags=['Users'])

@app.get('/')
def read_root():
    return {'message': 'Bem-vindo à API!'}