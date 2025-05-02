
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_listar_usuarios():
    response = client.get("/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_login_usuario_invalido():
    response = client.post("/auth/login", data={"username": "invalido@test.com", "password": "123456"})
    assert response.status_code == 401

def test_criar_usuario():
    response = client.post("/auth/register", json={
        "nome": "Teste Usuário",
        "email": "teste@exemplo.com"
    })
    assert response.status_code in (200, 400)  # pode ser 400 se ja existir
