from flask import Blueprint, request, jsonify
from uuid import uuid4

auth = Blueprint(
    "auth",
    __name__,
)


# Dummy patient data
patients = {
    "patient@example.com": {
        "password": "password123",
        "name": "John Doe",
    }
}


# Temporary session storage
sessions: dict[str, str] = {}


@auth.route("/login", methods=["POST"])
def login():

    login_data = request.json

    email = login_data.get("email")
    password = login_data.get("password")

    if email not in patients:

        return jsonify({"message": "Invalid email or password"}), 401

    if patients[email]["password"] != password:

        return jsonify({"message": "Invalid email or password"}), 401

    session_id = str(uuid4())

    sessions[session_id] = email

    return jsonify(
        {
            "message": "Login successful",
            "session_id": session_id,
        }
    )


@auth.route("/logout", methods=["POST"])
def logout():

    logout_data = request.json

    session_id = logout_data.get("session_id")

    if session_id not in sessions:

        return jsonify({"message": "Invalid session"}), 401

    del sessions[session_id]

    return jsonify(
        {
            "message": "Logout successful",
            "redirect": "/login",
        }
    )
