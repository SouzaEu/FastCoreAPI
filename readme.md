# 📦 Projeto: API FastAPI com OracleDB

API REST desenvolvida em **FastAPI** com conexão ao banco **Oracle** via `cx_Oracle` e mapeamento ORM com **SQLAlchemy**.

Inclui sistema completo de autenticação JWT, CRUD para todas as entidades do banco, estrutura modular escalável, documentação Swagger e testes automatizados com Pytest.

---

## 🚀 Tecnologias utilizadas

- **FastAPI** – Framework web moderno e rápido
- **SQLAlchemy** – ORM para mapeamento relacional
- **cx_Oracle** – Conexão com banco de dados Oracle
- **Pydantic v2** – Validação de dados com `from_attributes`
- **JWT** – Autenticação segura
- **Uvicorn** – ASGI Server
- **dotenv** – Variáveis de ambiente
- **Pytest** – Testes automatizados

---

## ⚙️ Configuração e execução

### 1. Instale os pacotes:
```bash
pip install -r requirements.txt
```

### 2. Configure o `.env` com os dados do Oracle:
```dotenv
ORACLE_USER=seu_usuario
ORACLE_PASS=sua_senha
ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SID=XE
```

### 3. Execute o projeto:
```bash
uvicorn app.main:app --reload
```

### 4. Acesse:
- Swagger UI: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

---

## 📌 Funcionalidades principais

- Autenticação com registro, login e perfil via JWT
- CRUD completo para:
  - Usuários
  - Empresa (configuração)
  - Órgãos reguladores
  - Tipos de órgão
  - Resumos do DOU
  - Canais de alerta
  - Relacionamentos entre usuários e órgãos/canais
  - Logs de processamento
  - Assinatura, fatura e método de pagamento
  - Preferências de notificação
- Documentação Swagger customizada
- Testes automatizados com Pytest

---

## 🧪 Rodando os testes
```bash
pytest
```

---

## 📂 Estrutura do projeto

```
app/
├── main.py
├── models/
│   ├── database.py
│   ├── schemas.py
│   └── tables.py
├── routes/
│   ├── auth.py
│   ├── usuarios.py
│   ├── empresa.py
│   ├── ... (demais rotas)
└── services/
    └── auth_service.py
```

---

## 🔒 Exemplo de uso de token JWT

```http
Authorization: Bearer <token>
```

---

## 📄 Licença
Este projeto é distribuído sob a Licença MIT. Para mais detalhes, consulte o arquivo `LICENSE`.
