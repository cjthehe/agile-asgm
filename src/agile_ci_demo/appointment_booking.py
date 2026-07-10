from datetime import datetime

# Dummy Counselor Data

counselors = [
    {
        "id": 1,
        "name": "Dr. Sarah",
        "specialization": "Anxiety",
        "available_slots": [
            "10 July 2026 10:00 AM",
            "10 July 2026 2:00 PM",
            "11 July 2026 9:00 AM",
        ],
    },
    {
        "id": 2,
        "name": "Dr. John",
        "specialization": "Depression",
        "available_slots": [
            "10 July 2026 11:00 AM",
            "11 July 2026 3:00 PM",
        ],
    },
    {
        "id": 3,
        "name": "Dr. Emily",
        "specialization": "Stress Management",
        "available_slots": [
            "12 July 2026 10:00 AM",
            "12 July 2026 2:00 PM",
        ],
    },
]


# Temporary appointment storage
# Later replace with database
appointments = []


# Display Appointment Form


def display_booking_form():
    print("\n================================")
    print("      Appointment Booking Form")
    print("================================")


# Search Counselor


def search_counselor():

    keyword = input("\nSearch counselor name/specialization: ").lower()

    results = []

    for counselor in counselors:
        if keyword in counselor["name"].lower() or keyword in counselor["specialization"].lower():
            results.append(counselor)

    if len(results) == 0:
        print("\nNo counselor found.")
        return None

    print("\n========== Counselor Results ==========")

    for counselor in results:
        print(f"{counselor['id']}. " f"{counselor['name']} - " f"{counselor['specialization']}")

    while True:

        try:
            choice = int(input("\nSelect counselor ID: "))

            for counselor in results:
                if counselor["id"] == choice:
                    return counselor

            print("Invalid counselor.")

        except ValueError:
            print("Please enter a number.")


# Retrieve Counselor Slots


def retrieve_slots(counselor):

    print(f"\nAvailable slots for " f"{counselor['name']}")

    if len(counselor["available_slots"]) == 0:
        print("No available slots.")
        return None

    for index, slot in enumerate(counselor["available_slots"], start=1):
        print(f"{index}. {slot}")

    while True:

        try:
            choice = int(input("\nSelect slot: "))

            if choice >= 1 and choice <= len(counselor["available_slots"]):
                return counselor["available_slots"][choice - 1]

            print("Invalid slot.")

        except ValueError:
            print("Please enter a number.")


# Validate Duplicate Booking


def check_duplicate_booking(patient_name, selected_slot):

    for appointment in appointments:

        if (
            appointment["patient"].lower() == patient_name.lower()
            and appointment["slot"] == selected_slot
            and appointment["status"] == "Booked"
        ):
            return True

    return False


# Create Appointment Record


def create_appointment(patient_name, counselor, selected_slot):

    appointment_id = f"APT{len(appointments)+1:03d}"

    appointment = {
        "appointment_id": appointment_id,
        "patient": patient_name,
        "counselor": counselor["name"],
        "specialization": counselor["specialization"],
        "slot": selected_slot,
        "status": "Booked",
        "booking_date": datetime.now().strftime("%d %B %Y"),
    }

    appointments.append(appointment)

    return appointment


# Lock Booked Slot


def lock_slot(counselor, selected_slot):

    counselor["available_slots"].remove(selected_slot)


# Display Confirmation


def display_confirmation(appointment):

    print("\n================================")

    print("   Appointment Confirmed")

    print("================================")

    print(f"Appointment ID : " f"{appointment['appointment_id']}")

    print(f"Patient        : " f"{appointment['patient']}")

    print(f"Counselor      : " f"{appointment['counselor']}")

    print(f"Specialization : " f"{appointment['specialization']}")

    print(f"Date & Time    : " f"{appointment['slot']}")

    print(f"Status         : " f"{appointment['status']}")

    print("================================")


# Main Booking Process


def book_appointment():

    display_booking_form()

    patient_name = input("\nEnter patient name: ")

    if patient_name.strip() == "":
        print("Patient name cannot be empty.")
        return

    counselor = search_counselor()

    if counselor is None:
        return

    selected_slot = retrieve_slots(counselor)

    if selected_slot is None:
        return

    # Validate slot still exists

    if selected_slot not in counselor["available_slots"]:

        print("Slot is no longer available.")
        return

    # Prevent duplicate booking

    if check_duplicate_booking(patient_name, selected_slot):

        print("You already booked this slot.")
        return

    # Create appointment

    appointment = create_appointment(patient_name, counselor, selected_slot)

    # Lock slot

    lock_slot(counselor, selected_slot)

    display_confirmation(appointment)


# Program Start

while True:

    print("\n================================")
    print(" Appointment Booking System")
    print("================================")
    print("1. Book Appointment")
    print("2. Exit")

    choice = input("Choose option: ")

    if choice == "1":

        book_appointment()

    elif choice == "2":

        print("System closed.")
        break

    else:

        print("Invalid option.")
