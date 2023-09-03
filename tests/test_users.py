from fastapi.testclient import TestClient
from api.fastapi_app import app

client = TestClient(app)

def test_list_users():
    response = client.get('/users')

    assert response.status_code == 200