from datetime import datetime

import pytest 

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService, 
    PatientService,
    PractitionerService, 
)

WHEN = datetime(2026, 11, 10, 9, 0)

def make_services() -> tuple[
    SmartCareDataStore,
    PatientService,
    PractitionerService, 
    AppointmentService, 
]:
    """Fresh store and three services sharing it."""
    store = SmartCareDataStore()
    return ( 
        store,
        PatientService(store),
        PractitionerService(store),
        AppointmentService(store),
    )

def test_register_patient_stores_and_returns_same_object() -> None:
    """T-10"""
    store, patients, _, _ = make_services()
    patient = patients.register_patient("P1", "Alice Example")
    assert store.find_patient("P1") is patient
    assert store.list_patients() == [patient]

def test_duplicate_patient_id_is_rejected_without_overwrite() -> None:
    """T-11"""
    store, patients, _, _ = make_services()
    original = patients.register_patient("P1", "Alice Example")
    with pytest.raises(ValueError): 
        patients.register_patient("P1", "Replacement")
    assert store.find_patient("P1") is original 
    assert original.name == "Alice Example" 
    assert store.list_patients() == [original] 

def test_find_patient_returns_stored_patient() -> None: 
    """T-12"""
    _, patients, _, _ = make_services()
    patient = patients.register_patient("P1", "Alice Example")
    assert patients.find_patient("P1") is patient

def test_find_unknown_patient_raises_lookup_error() -> None: 
    """T-13"""
    store, patients, _, _ = make_services()
    patient = patients.register_patient("P1", "Alice Example") 
    with pytest.raises(LookupError):
        patients.find_patient("P9")
    with pytest.raises(ValueError): 
        patients.find_patient("   ")
    assert store.list_patients() == [patient]

def test_find_practitioner_returns_stored_or_raises() -> None:
    """T-14"""
    _, _, practitioners, _ = make_services() 
    practitioner = practitioners.register_practitioner("D1", "Dr Sample", "GP")
    assert practitioners.find_practitioner("D1") is practitioner 
    with pytest.raises(LookupError):
        practitioners.find_practitioner("D9")

def test_book_appointment_stores_scheduled_appointment() -> None: 
    """T-15"""
    store, patients, practitioners, appointments = make_services() 
    patient = patients.register_patient("P1", "Alice Example")
    practitioner = practitioners.register_practitioner("D1", "Dr Sample", "GP")
    appointment = appointments.book_appointment ("A1", "P1", "D1", WHEN)
    assert store.find_appointment("A1") is appointment
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner
    assert appointment.date_time == WHEN
    assert appointment.status is AppointmentStatus.SCHEDULED

def test_booking_unknown_participant_is_rejected() -> None: 
    """T-16"""
    store, patients, practitioners, appointments = make_services() 
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP") 
    with pytest.raises(LookupError):
        appointments.book_appointment("A1", "P9", "D1", WHEN) 
    with pytest.raises(LookupError):
        appointments.book_appointment("A1", "P1", "D9", WHEN)
    assert store.list_appointments() == [] 

def test_same_practitioner_same_time_conflict_is_rejected() -> None: 
    """T-17"""
    store, patients, practitioners, appointments = make_services()
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP")
    first = appointments.book_appointment("A1", "P1", "D1", WHEN)
    with pytest.raises(ValueError):
        appointments.book_appointment("A2", "P1", "D1", WHEN)
    assert store.list_appointments() == [first]

def test_different_practitioner_same_time_is_allowed() -> None: 
    """T-18"""
    store, patients, practitioners, appointments = make_services()
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP")
    practitioners.register_practitioner("D2", "Dr Other", "GP")
    first = appointments.book_appointment("A1", "P1", "D1", WHEN)
    second = appointments.book_appointment("A2", "P1", "D2", WHEN)
    assert store.list_appointments() == [first, second] 

def test_cancelled_booking_does_not_block_slot() -> None: 
    """T-19"""
    store, patients, practitioners, appointments = make_services() 
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP")
    appointments.book_appointment("A1", "P1", "D1", WHEN) 
    appointments.cancel_appointment("A1")
    second = appointments.book_appointment("A2", "P1", "D1", WHEN)
    assert store.find_appointment("A2") is second
    assert second.status is AppointmentStatus.SCHEDULED

def test_cancel_returns_same_object_with_cancelled_status() -> None: 
    """T-20"""
    _, patients, practitioners, appointments = make_services() 
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP")
    appointment = appointments.book_appointment("A1", "P1", "D1", WHEN) 
    result = appointments.cancel_appointment("A1")
    assert result is appointment
    assert result.status is AppointmentStatus.CANCELLED

def test_cancelled_appointment_is_retained_and_listed() -> None:
    """T-21"""
    store, patients, practitioners, appointments = make_services()
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP")
    appointment = appointments.book_appointment("A1", "P1", "D1", WHEN)
    appointments.cancel_appointment("A1")
    assert appointments.find_appointment("A1") is appointment
    assert appointment in store.list_appointments()
    assert appointment.status is AppointmentStatus.CANCELLED

def test_repeated_cancellation_via_service_is_rejected() -> None: 
    """T-22"""
    store, patients, practitioners, appointments = make_services()
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP")
    appointment = appointments.book_appointment("A1", "P1", "D1", WHEN) 
    appointments.cancel_appointment("A1")
    with pytest.raises(ValueError):
        appointments.cancel_appointment("A1")
    assert appointment.status is AppointmentStatus.CANCELLED
    assert store.list_appointments() == [appointment]

def test_cancel_unknown_appointment_raises_lookup_error() -> None: 
    """T-23""" 
    store, patients, practitioners, appointments = make_services()
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP")
    appointment = appointments.book_appointment("A1", "P1", "D1", WHEN)
    with pytest.raises(LookupError):
        appointments.cancel_appointment("A9")
    with pytest.raises(ValueError):
        appointments.cancel_appointment("   ")
    assert appointment.status is AppointmentStatus.SCHEDULED
    assert store.list_appointments() == [appointment]

def test_find_appointment_returns_known_appointment() -> None: 
    """T-24"""
    _, patients, practitioners, appointments = make_services() 
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP") 
    appointment = appointments.book_appointment("A1", "P1", "D1", WHEN)
    assert appointments.find_appointment("A1") is appointment

def test_duplicate_appointment_id_does_not_overwrite() -> None: 
    """T-25"""
    store, patients, practitioners, appointments = make_services()
    patients.register_patient("P1", "Alice Example")
    practitioners.register_practitioner("D1", "Dr Sample", "GP")
    first = appointments.book_appointment("A1", "P1", "D1", WHEN)
    with pytest.raises(ValueError):
        appointments.book_appointment(
            "A1", "P1", "D1", datetime(2026, 11, 10, 10, 0),
        )
    assert store.find_appointment("A1") is first
    assert first.date_time == WHEN
    assert store.list_appointments() == [first]