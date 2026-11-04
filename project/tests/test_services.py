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
    with pytest,raises(ValueError): 
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

def test_find_pracittioner_returns_stored_or_raises() -> None:
    """"-14"""
    _, _, practitioners, _ = make_services() 
    practitioner = practitioners.register_practitioner("D1", "Dr Sample", "GP")
    assert practitioners.find_practitioenr("D1") is practitioner 
    with pytest.raises(LookupError):
        practitioners.