import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app import app as flask_app, init_db

@pytest.fixture(scope="session")
def app():
    flask_app.config["TESTING"] = True
    with flask_app.app_context():
        init_db()
    yield flask_app

@pytest.fixture(scope="session")
def client(app):
    return app.test_client()

@pytest.fixture(scope="session")
def auth_headers(client):
    # Register a test user
    client.post("/register", json={
        "username": "testuser",
        "password": "testpass123"
    })
    # Login and get token
    response = client.post("/login", json={
        "username": "testuser",
        "password": "testpass123"
    })
    token = response.get_json()["access_token"]
    return {"Authorization": f"Bearer {token}"}