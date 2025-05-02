from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI
from app.routes import (
    auth, usuarios, empresa, orgaos, resumos, notificacoes, pagamentos,
    tipo_orgao, canais_alerta, usuario_canal_alerta, usuario_orgao, log_processamento
)

app = FastAPI(title="API FastAPI Oracle")

# Rotas principais
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(empresa.router, prefix="/empresa", tags=["Empresa"])
app.include_router(orgaos.router, prefix="/orgaos", tags=["Órgãos Reguladores"])
app.include_router(tipo_orgao.router, prefix="/tipo_orgao", tags=["Tipos de Órgão"])
app.include_router(resumos.router, prefix="/resumos", tags=["Resumos DOU"])
app.include_router(canais_alerta.router, prefix="/canais_alerta", tags=["Canais de Alerta"])
app.include_router(usuario_canal_alerta.router, prefix="/usuario_canal_alerta", tags=["Usuário x Canal"])
app.include_router(usuario_orgao.router, prefix="/usuario_orgao", tags=["Usuário x Órgão"])
app.include_router(log_processamento.router, prefix="/log_processamento", tags=["Logs"])
app.include_router(pagamentos.router, prefix="/pagamentos", tags=["Pagamentos"])
app.include_router(notificacoes.router, prefix="/notificacoes", tags=["Notificações"])

# Swagger customizado
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API FastAPI Oracle",
        version="1.0.0",
        description="Esta API conecta um sistema frontend com um banco de dados Oracle, fornecendo autenticação, CRUD completo e estrutura escalável.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
