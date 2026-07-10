from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
import sqlite3
import re

app = Flask(__name__)

DATABASE = "mental_health.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def valid_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email)


def valid_password(password):
    # At least 8 characters, one uppercase, one lowercase, one number
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    return re.match(pattern, password)


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"message": "Please fill in all fields."}), 400

    if not valid_email(email):
        return jsonify({"message": "Invalid email format."}), 400

    if not valid_password(password):
        return (
            jsonify(
                {
                    "message": "Password must contain at least 8 characters, one uppercase letter, one lowercase letter and one number."
                }
            ),
            400,
        )

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))

    user = cursor.fetchone()

    if user:
        conn.close()
        return jsonify({"message": "Email already registered."}), 400

    hashed_password = generate_password_hash(password)

    cursor.execute(
        """
        INSERT INTO users(name,email,password)
        VALUES(?,?,?)
    """,
        (name, email, hashed_password),
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Registration successful."}), 201


if __name__ == "__main__":
    app.run(debug=True)
