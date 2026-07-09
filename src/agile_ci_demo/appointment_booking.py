# ==========================================
# Book Appointment Module (Dummy Data)
# Sprint 1 - Day 2
# ==========================================

# Dummy counselor data
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
        "available_slots": ["10 July 2026 11:00 AM", "11 July 2026 3:00 PM"],
    },
]

# Store booked appointments
appointments = []


def display_counselors():
    print("\n========== Available Counselors ==========")

    for counselor in counselors:
        print(f"ID : {counselor['id']}")
        print(f"Name : {counselor['name']}")
        print(f"Specialization : {counselor['specialization']}")
        print("---------------------------------------")


def find_counselor(counselor_id):
    for counselor in counselors:
        if counselor["id"] == counselor_id:
            return counselor
    return None


def display_slots(counselor):
    print(f"\nAvailable Slots for {counselor['name']}")

    if len(counselor["available_slots"]) == 0:
        print("No available slots.")
        return False

    for i, slot in enumerate(counselor["available_slots"], start=1):
        print(f"{i}. {slot}")

    return True


def book_appointment():

    print("\n========= Book Appointment =========")

    patient_name = input("Enter Patient Name: ")

    display_counselors()

    try:
        counselor_id = int(input("\nSelect Counselor ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    counselor = find_counselor(counselor_id)

    if counselor is None:
        print("Counselor not found.")
        return

    if not display_slots(counselor):
        return

    try:
        slot_choice = int(input("\nChoose Slot Number: "))
    except ValueError:
        print("Invalid choice.")
        return

    if slot_choice < 1 or slot_choice > len(counselor["available_slots"]):
        print("Invalid slot.")
        return

    selected_slot = counselor["available_slots"][slot_choice - 1]

    # Create appointment
    appointment = {
        "patient": patient_name,
        "counselor": counselor["name"],
        "specialization": counselor["specialization"],
        "slot": selected_slot,
    }

    appointments.append(appointment)

    # Remove booked slot
    counselor["available_slots"].remove(selected_slot)

    print("\n========== Booking Successful ==========")
    print(f"Patient        : {appointment['patient']}")
    print(f"Counselor      : {appointment['counselor']}")
    print(f"Specialization : {appointment['specialization']}")
    print(f"Appointment    : {appointment['slot']}")


# -------------------
# Main Program
# -------------------

while True:

    print("\n===================================")
    print("      Appointment Booking")
    print("===================================")
    print("1. Book Appointment")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_appointment()

    elif choice == "2":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")
