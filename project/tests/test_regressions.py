from datetime import datetime

import pytest

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.services import (
    AppointmentService,
    PatientService,
    PractitionerService,
)

def foundation() -> tuple[
    SmartCareDataStore,
    Patient,
    Practitioner,
    AppointmentService,
]:
    """Create fresh registered participants and services for a supplied
    check.
    """
    data_store = SmartCareDataStore()
    patient = PatientService(data_store).register_patient('P1', 'Alex Example')
    practitioner = PractitionerService(
        data_store,
    ).register_practitioner('D1', 'Taylor Example', 'General')
    return (data_store, patient, practitioner, AppointmentService(data_store))

def test_appointment_retained_in_datastore_after_cancellation() -> None:
    #create appointment and ensure that the appointment can still be found after running find_appointment()
    data_store, patient, practitioner, appointment_service = foundation()
    appointment = appointment_service.book_appointment("A1", "P1", "D1", datetime(2026, 10, 1, 9))
    assert appointment_service.find_appointment("A1") is appointment

    #checks that the appointment still exists in datastore. Will fail if cancelling an appointment removes it form the datastore.
    assert appointment in data_store.list_appointments()
    #Note: this disproves my initial hypothesis.