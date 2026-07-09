from fastapi.testclient import TestClient
from agile_ci_demo.app import app

client = TestClient(app)


def test_logout():

    login = client.post(
        "/login",
        json={"email": "patient@example.com", "password": "password123"},
    )

    session_id = login.json()["session_id"]

    response = client.post(
        "/logout",
        json={"session_id": session_id},
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Logout successful"
