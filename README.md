
# API FastAPI + Oracle

Esta API serve como ponte entre um banco de dados Oracle e um frontend moderno.

## Stack

- FastAPI
- SQLAlchemy
- cx_Oracle
- Pydantic
- Python-dotenv
- Uvicorn

## Como rodar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Configure o `.env` com as credenciais Oracle.
