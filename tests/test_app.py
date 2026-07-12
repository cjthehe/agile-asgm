import pytest

from agile_ci_demo.app import app
from agile_ci_demo.appointment_booking import appointments
from agile_ci_demo.dummy_data import counselors


@pytest.fixture
def client():
    """
    Create Flask test client.
    """

    app.config["TESTING"] = True

    return app.test_client()


def setup_function() -> None:
    """
    Reset data before every test.
    """

    appointments.clear()

    # Reset dummy counselor slots
    counselors[0]["available_slots"] = [
        "10 July 2026 10:00 AM",
        "10 July 2026 2:00 PM",
        "11 July 2026 9:00 AM",
    ]

    counselors[1]["available_slots"] = [
        "10 July 2026 11:00 AM",
        "11 July 2026 3:00 PM",
    ]


def test_home_page(client):
    """
    Scenario:
      Given the Flask application is running
      When user accesses homepage
      Then homepage loads successfully
    """

    response = client.get("/")

    assert response.status_code == 200


def test_booking_page(client):
    """
    Scenario:
      Given patient wants to book appointment
      When patient opens booking page
      Then booking form is displayed
    """

    response = client.get("/book")

    assert response.status_code == 200


def test_select_counselor(client):
    """
    Scenario:
      Given counselors exist
      When patient selects a counselor
      Then available slots are retrieved
    """

    response = client.post(
        "/book",
        data={
            "counselor": "1",
        },
    )

    assert response.status_code == 200

    assert b"10 July 2026 10:00 AM" in response.data


def test_view_appointments(client):
    """
    Scenario:
      Given appointment records exist
      When patient views appointments
      Then appointment page is displayed
    """

    response = client.get("/appointments")

    assert response.status_code == 200


def test_cancel_appointment(client):
    """
    Scenario:
      Given an appointment exists
      When user cancels appointment
      Then cancellation request is successful
    """

    appointments.append(
        {
            "appointment_id": "APT001",
            "patient": "John Doe",
            "counselor": "Dr. Sarah",
            "slot": "10 July 2026 10:00 AM",
            "status": "Booked",
        }
    )

    response = client.get("/cancel/APT001")

    assert response.status_code == 302
