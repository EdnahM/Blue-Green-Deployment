import pytest
from app import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Blue-Green Deployment Demo" in response.data

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "healthy"
    assert "version" in json_data

def test_api_endpoint(client):
    response = client.get("/api/greeting")
    assert response.status_code == 200
    json_data = response.get_json()
    assert "message" in json_data
    assert "timestamp" in json_data
