============================= test session starts =============================
platform win32 -- Python 3.14.5, pytest-8.3.5, pluggy-1.7.0
rootdir: C:\Users\chars\st1-assignment-3\project
collected 16 items / 13 deselected / 3 selected

tests\test_services.py .FF                                               [100%]

================================== FAILURES ===================================
____________ test_same_practitioner_same_time_conflict_is_rejected ____________

    def test_same_practitioner_same_time_conflict_is_rejected() -> None:
        """T-17"""
        store, patients, practitioners, appointments = make_services()
        patients.register_patient("P1", "Alice Example")
        practitioners.register_practitioner("D1", "Dr Sample", "GP")
        first = appointments.book_appointment("A1", "P1", "D1", WHEN)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

tests\test_services.py:100: Failed
______________ test_different_practitioner_same_time_is_allowed _______________

    def test_different_practitioner_same_time_is_allowed() -> None:
        """T-18"""
        store, patients, practitioners, appointments = make_services()
        patients.register_patient("P1", "Alice Example")
        practitioners.register_practitioner("D1", "Dr Sample", "GP")
        practitioners.register_practitioner("D2", "Dr Other", "GP")
        first = appointments.book_appointment("A1", "P1", "D1", WHEN)
>       second = appointments.book_appointment("A2", "P1", "D2", WHEN)

tests\test_services.py:111: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <smartcare.services.AppointmentService object at 0x00000162BD21F750>
appointment_id = 'A2', patient_id = 'P1', practitioner_id = 'D2'
date_time = datetime.datetime(2026, 11, 10, 9, 0)

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
>           raise ValueError(
                'Practitioner already has a SCHEDULED appointment at this time',
            )
E           ValueError: Practitioner already has a SCHEDULED appointment at this time

smartcare\services.py:137: ValueError
=========================== short test summary info ===========================
FAILED tests/test_services.py::test_same_practitioner_same_time_conflict_is_rejected
FAILED tests/test_services.py::test_different_practitioner_same_time_is_allowed
================= 2 failed, 1 passed, 13 deselected in 0.12s ==================
