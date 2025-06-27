import pytest
from ..app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data == b'OK'


def test_data_endpoint(client):
    response = client.get('/data')
    assert response.status_code == 200
    assert response.json == {"message": "Hello from DevOps!"}
