# tests/test_api.py

from fastapi.testclient import TestClient
from sobjanta.main import app

client = TestClient(app)

def test_search():
    response = client.get("/search?query=test&api_key=testkey")
    assert response.status_code == 200
    assert response.json() == {"message": "Searching for 'test' with API key 'testkey'"}
