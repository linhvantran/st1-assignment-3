from datetime import datetime, timezone

import pytest 

from smartcare.domain import ( 
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)

WHEN = datetime(2026, 11, 10, 9, 0)

def make_participants() -> tuple[Patient, Practitioner]: 
    """Create synthetic participants."""
    return ( 
        Patient("P1", "Alice Example"),
        Practitioner("D1", "Dr Sample", "GP"), 
    ) 

def test_patient_stores_trimmed_id_and_name() -> None: 
    """T-01"""
    patient = Patient(" P1 ", "Alice Example")
    assert patient.patient_id == "P1"
    assert patient.name == "Alice Example" 

def test_blank_patient_id_is_rejected() -> None: 
    """T-02"""
    with pytest.raises(ValueError):
        Patient("", "Alice Example") 

def test_whitespace_only_patient_name_is_rejected() -> None: 
    """T-03""" 
    with pytest.raises(ValueError):
        Patient("P1", "   ")

def test_practitioner_requires_id_name_and_specialty() -> None: 
    """T-04"""
    practitioner = Practitioner(" D1 ", " Dr Sample ", " GP ")
    assert practitioner.practitioner_id == "D1"
    assert practitioner.name == "Dr Sample"
    assert practitioner.specialty == "GP"
    with pytest.raises(ValueError):
        Practitioner("D1", "Dr Sample", "   ")

def test_new_appointment_starts_scheduled() -> None: 
    """T-05"""
    patient, practitioner = make_participants()
    appointment = Appointment("A1", patient, practitioner, WHEN)
    assert appointment.status is AppointmentStatus.SCHEDULED

def test_cancel_changes_status() -> None: 
    """T-06"""
    patient, practitioner = make_participants() 
    appointment = Appointment("A1", patient, practitioner, WHEN)
    appointment.cancel() 
    assert appointment.status is AppointmentStatus.CANCELLED

def test_repeated_cancellation_is_rejected() -> None: 
    """T-07"""
    patient, practitioner = make_participants()
    appointment = Appointment("A1", patient, practitioner, WHEN) 
    appointment.cancel() 
    with pytest.raises(ValueError):
        appointment.cancel() 
    assert appointment.status is AppointmentStatus.CANCELLED

def test_cancel_completed_appointment_is_rejected() -> None: 
    """T-08"""
    patient, practitioner = make_participants() 
    appointment = Appointment( 
        "A1", patient, practitioner, WHEN, 
        status=AppointmentStatus.COMPLETED,
    )
    with pytest.raises(ValueError):
        appointment.cancel()
    assert appointment.status is AppointmentStatus.COMPLETED

def test_datetime_with_seconds_or_timezone_is_reacted() -> None:
    """T-09""" 
    patient, practitioner = make_participants() 
    with pytest.raises(ValueError):
        Appointment( 
            "A1", patient, practitioner, datetime(2026, 11, 10, 9, 0, 30),
        )
    with pytest.raises(ValueError):
        Appointment(
            "A1", patient, practitioner, 
            datetime(2026, 11, 10, 9, 0, tzinfo=timezone.utc),
        )