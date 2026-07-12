from agile_ci_demo.auth import router as auth_router

from flask import Flask, render_template, request, redirect

from .dummy_data import counselors

from .appointment_booking import (
    get_all_appointments,
    cancel_appointment,
)

app = Flask(__name__)

app.include_router(auth_router)


# Flask
# HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")


# BOOKING PAGE
@app.route("/book", methods=["GET", "POST"])
def book():

    selected_counselor = None
    available_slots = []

    # When user selects counselor
    if request.method == "POST":

        counselor_id = request.form.get("counselor")

        if counselor_id:

            counselor_id = int(counselor_id)

            for counselor in counselors:

                if counselor["id"] == counselor_id:

                    selected_counselor = counselor

                    available_slots = counselor["available_slots"]

                    break

    return render_template(
        "booking.html",
        counselors=counselors,
        selected_counselor=selected_counselor,
        available_slots=available_slots,
    )


# APPOINTMENT LIST
@app.route("/appointments")
def appointments():

    return render_template(
        "appointments.html",
        appointments=get_all_appointments(),
    )


# CANCEL APPOINTMENT
@app.route("/cancel/<appointment_id>")
def cancel(appointment_id):

    cancel_appointment(appointment_id)

    return redirect("/appointments")
