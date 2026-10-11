"""Simple workflows using a shared SmartCareDataStore object."""


from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)


class PatientService:
    """Coordinate patient registration and lookup through the shared store."""

    def __init__(self, data_store: SmartCareDataStore) -> None:
        """Use the shared store to coordinate patient operations."""
        self.data_store = data_store

    def register_patient(self, patient_id: str, name: str) -> Patient:
        """Validate and register a patient, returning the stored object.

        Raise ValueError for invalid fields or an existing patient ID.
        """
        patient = Patient(patient_id, name)
        self.data_store.add_patient(patient)
        return patient

    def find_patient(self, patient_id: str) -> Patient:
        """Stage 6 TODO: return the stored patient for a valid patient ID.

        Completion must raise LookupError for absence and ValueError for
        a blank/invalid ID. It must not create a replacement patient.
        The starter deliberately raises NotImplementedError.
        """
        raise NotImplementedError('Stage 6: patient lookup')


class PractitionerService:
    """Coordinate practitioner registration and lookup through the shared
    store.
    """

    def __init__(self, data_store: SmartCareDataStore) -> None:
        """Use the shared store to coordinate practitioner operations."""
        self.data_store = data_store

    def register_practitioner(
        self,
        practitioner_id: str,
        name: str,
        specialty: str,
    ) -> Practitioner:
        """Validate and register a practitioner, returning the stored
        object.

        Raise ValueError for invalid fields or an existing practitioner
        ID.
        """
        practitioner = Practitioner(practitioner_id, name, specialty)
        self.data_store.add_practitioner(practitioner)
        return practitioner

    def find_practitioner(self, practitioner_id: str) -> Practitioner:
        """Stage 6 TODO: return the stored practitioner for a valid ID.

        Completion must raise LookupError for absence and ValueError for
        a blank/invalid ID. It must not create a replacement
        practitioner. The starter deliberately raises
        NotImplementedError.
        """
        raise NotImplementedError('Stage 6: practitioner lookup')


class AppointmentService:
    """Coordinate booking, lookup and cancellation using the shared store."""

    def __init__(self, data_store: SmartCareDataStore) -> None:
        """Use the shared store to coordinate appointment operations."""
        self.data_store = data_store

    def book_appointment(
        self,
        appointment_id: str,
        patient_id: str,
        practitioner_id: str,
        date_time: datetime,
    ) -> Appointment:
        """Book registered participant IDs and return the stored
        appointment.

        Raise LookupError for absent participants. Raise ValueError for
        invalid values, duplicate appointment IDs or a practitioner
        conflict.
        """
        patient = self.data_store.find_patient(patient_id)
        practitioner = self.data_store.find_practitioner(practitioner_id)
        if patient is None:
            raise LookupError('Patient not found')
        if practitioner is None:
            raise LookupError('Practitioner not found')
        appointment = Appointment(
            appointment_id,
            patient,
            practitioner,
            date_time,
        )
        if self.data_store.find_appointment(
            appointment.appointment_id,
        ) is not None:
            raise ValueError('Appointment ID already exists')
        if self.data_store.has_practitioner_conflict(
            practitioner.practitioner_id,
            date_time,
        ):
            raise ValueError(
                'Practitioner already has a SCHEDULED appointment at this time',
            )
        self.data_store.add_appointment(appointment)
        return appointment

    def find_appointment(self, appointment_id: str) -> Appointment:
        """Return the stored appointment; raise LookupError when absent.

        Reject a blank or invalid ID with ValueError; do not create
        records.
        """
        appointment = self.data_store.find_appointment(appointment_id)
        if appointment is None:
            raise LookupError('Appointment not found')
        return appointment

    def cancel_appointment(self, appointment_id: str) -> Appointment:
        """Stage 6: cancel through the domain method and retain the
        appointment.

        Return the cancelled object. Unknown IDs raise LookupError;
        invalid transitions raise ValueError and leave state unchanged.
        """
        raise NotImplementedError('Stage 6: appointment cancellation')

    def list_practitioner_appointments(
        self,
        practitioner_id: str,
        status: AppointmentStatus | None = None,
    ) -> list[Appointment]:
        """Stage 9: new ordered list; default includes every status.

        Unknown practitioner raises LookupError, invalid status
        ValueError; a known practitioner with no matches returns an
        empty list.
        """
        raise NotImplementedError('Stage 9: practitioner appointments')
