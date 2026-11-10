"""Console helpers and a small runnable starting demonstration."""


import re
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Appointment, AppointmentStatus 
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)
# this is a test

def parse_date_time(text: str) -> datetime:
    """Parse YYYY-MM-DD HH:MM; raise ValueError for invalid input."""
    if (
        not isinstance(text, str)
        or re.fullmatch(
            '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}', text
        ) is None
    ):
        raise ValueError('Use date/time format YYYY-MM-DD HH:MM')
    try:
        return datetime.strptime(text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError(
            'Invalid calendar date/time; use YYYY-MM-DD HH:MM',
        ) from None


def format_appointment(appointment: Appointment) -> str:
    """Return readable synthetic appointment details without changing
    state.
    """
    return (
        f'{appointment.appointment_id}: '
        f'{appointment.patient.patient_id} with '
        f'{appointment.practitioner.practitioner_id}, '
        f'{appointment.date_time:%Y-%m-%d %H:%M}, {appointment.status.value}'
    )


def run_demo() -> None:
    """Demonstrate supplied registration and booking using synthetic
    records.
    """
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)
    patients.register_patient('P1', 'Alex Example')
    practitioners.register_practitioner(
        'DR1',
        'Taylor Example',
        'General practice',
    )
    try:
        appointments.book_appointment(
            'A1',
            'P1',
            'DR1',
            parse_date_time('2026-10-01 09:00'),
        )
        print(format_appointment(appointments.find_appointment('A1')))
    except (ValueError, LookupError) as error:
        print(f'Error: {error}')
    print('Session-only data: records are lost on exit.')

menu = """
Main Menu
-----------------------------------------------------------
[1] Register a patient
[2] Find a patient
[3] Register a practitioner
[4] Find practitioner
[5] Book appointment
[6] Cancel appointment 
[7] Find appointment
[8] List practitioner appointments
[0] Exit 
-----------------------------------------------------------
"""

def run_menu() -> None:
    """Run the interactive console menu until the user chooses to exit.
    Uses a new in-memory store, so all records are lost on exit. Service 
    errors are printed and the menu continues."""
    data_store = SmartCareDataStore()
    patients = PatientService(data_store)
    practitioners = PractitionerService(data_store)
    appointments = AppointmentService(data_store)

    def register_patient() -> None:
        patient = patients.register_patient(
            input("Patient ID: "), input("Patient name: ")
        )
        print("Patient registered successfully.")
        print(f"{patient.patient_id}: {patient.name}")

    def find_patient() -> None: 
        patient = patients.find_patient(input("Patient ID: "))
        print(f"Patient found. {patient.patient_id}: {patient.name}")

    def register_practitioner() -> None: 
        practitioner = practitioners.register_practitioner(
            input("Practitioner ID: "),
            input("Practitioner name: "), 
            input("Specialty: "), 
        )
        print("Practitioner registered successfully.")
        print( 
            f"{practitioner.practitioner_id}: {practitioner.name}. "
            f"{practitioner.specialty}"
        )

    def find_practitioner() -> None: 
        practitioner = practitioners.find_practitioner( 
            input("Practitioner ID: ")
        )
        print(
                f"Practitioner found. {practitioner.practitioner_id}: "
                f"{practitioner.name}, {practitioner.specialty}"
        )

    def book() -> None: 
        appointment_id = input("Appointment ID: ")
        patient_id = input("Patient ID: ")
        practitioner_id = input("Practitioner ID: ")
        when = parse_date_time(input("Date/Time [YYYY-MM-DD HH:MM]: "))
        appointment = appointments.book_appointment(
            appointment_id, patient_id, practitioner_id, when, 
        )
        print("Appointment booked successfully.")
        print(format_appointment(appointment))

    def cancel() -> None: 
        appointment = appointments.cancel_appointment(
            input("Appointment ID: ")
        ) 
        print("Appointment cancelled successfully.")
        print(format_appointment(appointment))

    def find_appointment() -> None: 
        appointment = appointments.find_appointment(
        input("Appointment ID: ")
        )
        print("Appointment found.")
        print(format_appointment(appointment))

    def list_appointments() -> None: 
        practitioner_id = input("Practitioner ID: ")
        text = input( 
            "Status filter [scheduled/cancelled/completed, blank = all]: "
        ).strip().lower()

        if text == "":
            status = None
        else:
            try:
                status = AppointmentStatus(text)
            except ValueError:
                raise ValueError(
                    "Status must be scheduled, cancelled or completed"
                ) from None
        found = appointments.list_practitioner_appointments(
                practitioner_id, status, 
        )
        if not found:
            print("No appointments found.") 
            return
        for number, appointment in enumerate(found, start=1):
            print(f"{number}. {format_appointment(appointment)}") 
        print(f"{len(found)} appointments found.")

    handlers = {
        "1": register_patient, 
        "2": find_patient,
        "3": register_practitioner,
        "4": find_practitioner, 
        "5": book, 
        "6": cancel,
        "7": find_appointment,
        "8": list_appointments,
    } 

    print ("Smartcare Interactive Console")
    print("Session data is temporary and will be discarded when you exit.")

    while True: 
        print(menu)
        choice = input("Select an option: ").strip()
        if choice == "0":
                print("Goodbye. Session data discarded.")
                return 
        handler = handlers.get(choice)
        if handler is None: 
            print("Unknown choice. Choose a number from 0 to 8.")
            continue
        try:
            handler()
        except (ValueError, LookupError) as error:
                print(f"Error: {error}")