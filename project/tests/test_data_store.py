import pytest 

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import Patient

def test_added_patient_is_found_and_listed() -> None: 
    store = SmartCareDataStore()
    patient = Patient("P1", "Alice Example")
    store.add_patient(patient)
    assert store.find_patient("P1") is patient
    assert store.list_patients() == [patient]

def test_unknown_patient_id_returns_none() -> None:
        store = SmartCareDataStore() 
        assert store.find_patient("P9") is None 

def test_blank_patient_id_is_rejected_by_find() -> None: 
    store = SmartCareDataStore() 
    with pytest.raises(ValueError):
        store.find_patient("   ")

def test_duplicate_patient_id_is_rejected() -> None: 
    store = SmartCareDataStore() 
    first = Patient("P1", "Alice Example")
    store.add_patient(first) 
    with pytest.raises(ValueError):
        store.add_patient(Patient("P1", "Replacement"))
    assert store.find_patient("P1") is first
    assert store.list_patients() == [first]

