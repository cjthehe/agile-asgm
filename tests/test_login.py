from fastapi.testclient import TestClient
from agile_ci_demo.app import app

client = TestClient(app)


def test_login_success():
    response = client.post(
        "/login",
        json={"email": "patient@example.com", "password": "password123"},
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"


def test_login_wrong_password():
    response = client.post(
        "/login",
        json={"email": "patient@example.com", "password": "wrong"},
    )

    assert response.status_code == 401


def test_login_unknown_email():
    response = client.post(
        "/login",
        json={"email": "abc@gmail.com", "password": "123456"},
    )

    assert response.status_code == 401
