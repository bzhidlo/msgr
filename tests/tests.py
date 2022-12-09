
from fastapi.testclient import TestClient
from main import app;

client = TestClient(app)

def test_login():
    response = client.get("/users/login")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
