from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import AppointmentStatus
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

NINE_AM = datetime(2026, 11, 10, 9, 0)
EIGHT_AM = datetime(2026, 11, 10, 8, 0)
TEN_AM = datetime(2026, 11, 10, 10, 0)


@pytest.fixture
def services():
    """Create one isolated in-memory store and its services per test."""
    data_store = SmartCareDataStore()
    patient_service = PatientService(data_store)
    practitioner_service = PractitionerService(data_store)
    appointment_service = AppointmentService(data_store)

    patient_service.register_patient('P1', 'Alice Example')
    practitioner_service.register_practitioner('D1', 'Dr One', 'GP')
    practitioner_service.register_practitioner('D2', 'Dr Two', 'Dentist')

    return (
        data_store,
        patient_service,
        practitioner_service,
        appointment_service,
    )


def snapshot(data_store):
    """Capture stored state as plain, immutable values."""
    patients = tuple(sorted(
        (patient.patient_id, patient.name)
        for patient in data_store.list_patients()
    ))
    practitioners = tuple(sorted(
        (
            practitioner.practitioner_id,
            practitioner.name,
            practitioner.specialty,
        )
        for practitioner in data_store.list_practitioners()
    ))
    appointments = tuple(sorted(
        (
            appointment.appointment_id,
            appointment.patient.patient_id,
            appointment.practitioner.practitioner_id,
            appointment.date_time,
            appointment.status.value,
        )
        for appointment in data_store.list_appointments()
    ))
    return patients, practitioners, appointments


def test_same_practitioner_same_time_booking_is_rejected_without_state_change(
    services,
):
    data_store, _, _, appointment_service = services
    appointment_service.book_appointment('A1', 'P1', 'D1', NINE_AM)
    before = snapshot(data_store)

    with pytest.raises(ValueError):
        appointment_service.book_appointment('A2', 'P1', 'D1', NINE_AM)

    assert snapshot(data_store) == before
    with pytest.raises(LookupError):
        appointment_service.find_appointment('A2')


def test_different_practitioner_can_be_booked_at_the_same_time(services):
    data_store, _, _, appointment_service = services

    first = appointment_service.book_appointment('A1', 'P1', 'D1', NINE_AM)
    second = appointment_service.book_appointment('A2', 'P1', 'D2', NINE_AM)

    assert first.date_time == second.date_time == NINE_AM
    assert first.practitioner.practitioner_id == 'D1'
    assert second.practitioner.practitioner_id == 'D2'
    assert {
        appointment.appointment_id
        for appointment in data_store.list_appointments()
    } == {'A1', 'A2'}


def test_duplicate_ids_and_unknown_participants_are_rejected_without_state_change(
    services,
):
    data_store, patient_service, _, appointment_service = services
    appointment_service.book_appointment('A1', 'P1', 'D1', NINE_AM)

    before = snapshot(data_store)
    with pytest.raises(ValueError):
        appointment_service.book_appointment('A1', 'P1', 'D2', TEN_AM)
    assert snapshot(data_store) == before

    with pytest.raises(ValueError):
        patient_service.register_patient('P1', 'Duplicate Patient')
    assert snapshot(data_store) == before

    with pytest.raises(LookupError):
        appointment_service.book_appointment('A2', 'UNKNOWN', 'D1', TEN_AM)
    assert snapshot(data_store) == before

    with pytest.raises(LookupError):
        appointment_service.book_appointment('A2', 'P1', 'UNKNOWN', TEN_AM)
    assert snapshot(data_store) == before

    # A failed booking must not reserve its appointment ID.
    appointment_service.book_appointment('A2', 'P1', 'D1', TEN_AM)
    assert appointment_service.find_appointment('A2').appointment_id == 'A2'
    assert len(data_store.list_appointments()) == 2


def test_cancellation_keeps_the_same_appointment_findable(services):
    _, _, _, appointment_service = services
    booked = appointment_service.book_appointment('A1', 'P1', 'D1', NINE_AM)

    cancelled = appointment_service.cancel_appointment('A1')
    found = appointment_service.find_appointment('A1')

    assert cancelled is booked
    assert found is booked
    assert found.status is AppointmentStatus.CANCELLED


def test_repeated_cancellation_and_unknown_appointment_leave_state_unchanged(
    services,
):
    data_store, _, _, appointment_service = services
    appointment_service.book_appointment('A1', 'P1', 'D1', NINE_AM)
    appointment_service.cancel_appointment('A1')
    before = snapshot(data_store)

    with pytest.raises(ValueError):
        appointment_service.cancel_appointment('A1')
    assert snapshot(data_store) == before

    with pytest.raises(LookupError):
        appointment_service.cancel_appointment('MISSING')
    assert snapshot(data_store) == before


def test_practitioner_appointment_listing_filters_orders_and_isolates_results(
    services,
):
    _, _, _, appointment_service = services
    appointment_service.book_appointment('A3', 'P1', 'D1', NINE_AM)
    appointment_service.book_appointment('A2', 'P1', 'D1', EIGHT_AM)
    appointment_service.cancel_appointment('A2')
    appointment_service.book_appointment('A1', 'P1', 'D1', EIGHT_AM)
    appointment_service.book_appointment('B1', 'P1', 'D2', EIGHT_AM)

    all_for_d1 = appointment_service.list_practitioner_appointments('D1')
    scheduled_for_d1 = appointment_service.list_practitioner_appointments(
        'D1', AppointmentStatus.SCHEDULED
    )
    all_for_d2 = appointment_service.list_practitioner_appointments('D2')

    assert [
        appointment.appointment_id for appointment in all_for_d1
    ] == ['A1', 'A2', 'A3']
    assert all_for_d1[1].status is AppointmentStatus.CANCELLED
    assert [
        appointment.appointment_id for appointment in scheduled_for_d1
    ] == ['A1', 'A3']
    assert [
        appointment.appointment_id for appointment in all_for_d2
    ] == ['B1']
    assert all(
        appointment.practitioner.practitioner_id == 'D1'
        for appointment in all_for_d1 + scheduled_for_d1
    )
    assert all(
        appointment.practitioner.practitioner_id == 'D2'
        for appointment in all_for_d2
    )


def test_practitioner_appointment_listing_validates_inputs(services):
    _, _, _, appointment_service = services

    assert appointment_service.list_practitioner_appointments('D2') == []
    with pytest.raises(LookupError):
        appointment_service.list_practitioner_appointments('UNKNOWN')
    with pytest.raises(ValueError):
        appointment_service.list_practitioner_appointments(' ')
    with pytest.raises(ValueError):
        appointment_service.list_practitioner_appointments('D1', 'scheduled')


def test_cancelling_an_appointment_frees_its_slot(services):
    data_store, _, _, appointment_service = services
    appointment_service.book_appointment('A1', 'P1', 'D1', NINE_AM)
    appointment_service.cancel_appointment('A1')

    replacement = appointment_service.book_appointment('A2', 'P1', 'D1', NINE_AM)

    assert replacement.appointment_id == 'A2'
    assert replacement.status is AppointmentStatus.SCHEDULED
    assert [
        appointment.appointment_id
        for appointment in data_store.list_appointments()
    ] == ['A1', 'A2']
    assert (
        appointment_service.find_appointment('A1').status
        is AppointmentStatus.CANCELLED
    )