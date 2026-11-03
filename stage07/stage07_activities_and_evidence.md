# Stage 7 Testing and Verification Record

Group/tutorial: [complete]  Members/cohorts: [complete]
Requirements baseline: SmartCare A3 Requirements Baseline 2026, revision 2.
Use the same project/. Link actual evidence; keep responses concise. Blank fields are for your group. Copy rows only as needed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage07/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions.

## A Tutorial Activities

### Activity 1 Requirement to test

For each requirement, propose one positive test, one negative test and the key assertion.

| Requirement | Positive test | Negative test | Key assertion |
|---|--|---|---|
| FR-01 Register patient | register_patient("P1", "Alice Example") on a fresh store | Registering a second patient with ID “P1” | The returned patient is the stored one (find_patient("P1") is patient). The duplicate raises ValueError and the stored patient’s name is unchanged. |
| FR-05 Prevent practitioner conflict | The same time with a different practitioner is booked successfully | The same practitioner at the same exact time while the first booking is SCHEDULED | The conflict raises ValueError and list_appointments() still holds only the first booking. |
| FR-06 Cancel appointment | Cancel a SCHEDULED appointment | Cancel the same appointment again | After the first cancel, the returned object is the stored one with status CANCELLED. The repeat raises ValueError and the status stays CANCELLED. |
| FR-07 Retain cancelled history | After cancellation, find_appointment and list_appointments still return the appointment | Cancel an unknown appointment ID | The appointment is still found by is identity with status CANCELLED. The unknown ID raises LookupError and leaves stored records untouched. |

### Activity 2 Strong or weak assertion

For each, select Strong for stated behaviour or Weak/unclear and explain why. State the behaviour and limits.

`assert True`
Judgement: [Weak/unclear]  Why: It can never fail, so it doesn’t check any behaviour.

`assert appointment is not None`
Judgement: [Weak/unclear]  Why: It shows an object exists but not which one, its status or its values. It would pass for a wrong or uncancelled appointment.

`assert appointment.status == AppointmentStatus.CANCELLED`
Judgement: [Strong for stated behaviour]  Why: It checks the required result of cancelling (AC-05.1). Its limits are that it doesn’t prove the appointment was retained or is the same stored object, and it only means something if the test started from SCHEDULED.

`assert len(results) > 0`
Judgement: [Weak/unclear]  Why: It doesn’t say which results come back or how many. Wrong or extra items would still pass.

`assert data_store.find_appointment('A1') is appointment`
Judgement: [Strong for stated behaviour]  Why: It proves the store holds that exact object, which supports retention (AC-05.2) and booking. Its limit is that it says nothing about the status, so it should be paired with a status assertion.

### Activity 3 Boundary thinking

Design boundary or edge cases for blank identifiers, whitespace-only names, same-time practitioner bookings, cancelled appointments and invalid status transitions.
For each input/state, expected result and supporting contract: 

| Input/state | Expected result | Supporting Contract |
|-------------|-----------------|--------------|
|Blank, whitespace-only or non-string patient ID|ValueError, and nothing stored| required_text in domain.py |
|Whitespace-only patient or practitioner name|ValueError| required_text|
|ID with surrounding spaces, such as “ P1 “|Stored as trimmed “P1”. “p1” is a different ID|IDs are trimmed and case-sensitive|
|Same practitioner, same exact datetime, existing SCHEDULED appointment|ValueError, existing state unchanged|has_practitioner_conflict and the book_appointment contract|
|Same practitioner one minute later, or a different practitioner at the same time|Booking succeeds| A conflict needs the same practitioner and the exact datetime|
|Booking a slot held by a CANCELLED appointment|Booking succeeds|Only SCHEDULED appointments conflict|
|Cancel a CANCELLED appointment|ValueError, status stays CANCELLED|Appointment.cancel guard|
|Cancel a COMPLETED appointment (built with that status)|ValueError, status stays COMPLETED|Appointment.cancel guard|
|Datetime with seconds or a timezone|ValueError|validate_date_time|
|Blank ID at the store, versus a valid unknown ID at the store and at the service|ValueError; None; LookupError|Store find_* methods and the service lookup contracts|

### Activity 4 Critique GitHub Copilot tests

GitHub Copilot generates five tests, all of which pass. Two only assert that objects are not None, one asserts True, and two assume SMS notifications exist. Identify what is wrong and rewrite the test intentions.

| Candidate | What is wrong | Rewritten test intention |
|---|---|---|
| 1 | It only asserts the object isn’t None, so it passes for a wrong or uncancelled appointment and doesn’t prove any requirement. | Book an appointment and assert the stored object is returned, with the expected patient, practitioner, date and SCHEDULED status. |
| 2 | The same weakness, in a different place. It doesn’t check values or state. | Register a patient and assert the stored object has the trimmed ID and name, and appears once in list_patients(). |
| 3 | assert True can’t fail, so it has no link to any requirement. | Replace it with a test of cancelling a SCHEDULED appointment, asserting status CANCELLED and the same object returned. |
| 4 | It assumes SMS notifications exist. No requirement defines them, so the test invents a business rule. | Drop it, or replace it with a test of a documented behaviour such as a conflicting booking raising ValueError and leaving state unchanged. |
| 5 | It also assumes SMS notifications, and any mock would hide whether real behaviour is correct. | Test what is documented: a cancelled appointment is retained and listed. Don’t test notifications.|

### Tutorial exit question

Why can 100% code coverage coexist with poor software verification?
Code coverage is a metric measured in percentage that represents the amount of code executed in a test. Poor software verification is caused by test cases that fail to catch logical errors. They coexist because their goals do not collide with each other. Code coverage is a metric while poor software verification is caused by poor programming. 

## B Requirement to Test Traceability Matrix

Assign TEST IDs before implementation or generation. Use canonical AC IDs with their actual meaning; quote supporting revision 2 contracts when no canonical AC is assigned. Blank-ID validation is not AC-01.2. Identify supplied versus student-authored evidence.

| Requirement | Acceptance criterion | Test ID | Test type | Test name / location | Expected behaviour | Result / observed status | Supplied or student-authored |
|---|---|---|---|---|---|---|---|
| FR-01 | AC-01.1 (partial evidence: construction only) | T-01 | Domain, positive | `test_domain.py::test_patient_stores_trimmed_id_and_name` | Valid patient keeps the trimmed ID and name | Not yet run | Student-authored |
| FR-01 | Validation contract (not AC-01.2): blank patient ID raises ValueError | T-02 | Domain, negative | `test_domain.py::test_blank_patient_id_is_rejected` | Blank patient ID raises ValueError | Not yet run | Student-authored |
| FR-01 | Validation contract: required patient name | T-03 | Domain, boundary | `test_domain.py::test_whitespace_only_patient_name_is_rejected` | Whitespace-only name raises ValueError | Not yet run | Student-authored |
| FR-03 | Supporting contract: practitioner ID, name and specialty are required | T-04 | Domain, positive and negative | `test_domain.py::test_practitioner_requires_id_name_and_specialty` | Valid values are stored trimmed; a blank specialty raises ValueError | Not yet run | Student-authored |
| FR-04 | AC-03.1 (partial evidence: construction only) | T-05 | Domain, positive | `test_domain.py::test_new_appointment_starts_scheduled` | A new appointment has status SCHEDULED | Not yet run | Student-authored |
| FR-06 | AC-05.1 | T-06 | Domain, positive | `test_domain.py::test_cancel_changes_status` | Cancelling a SCHEDULED appointment gives CANCELLED | Not yet run | Student-authored |
| FR-06 | AC-05.3 | T-07 | Domain, negative | `test_domain.py::test_repeated_cancellation_is_rejected` | Second cancel raises ValueError; status stays CANCELLED | Not yet run | Student-authored |
| FR-06 | Supporting contract: Appointment.cancel guard (only SCHEDULED may be cancelled) | T-08 | Domain, negative | `test_domain.py::test_cancel_completed_appointment_is_rejected` | COMPLETED appointment raises ValueError; status stays COMPLETED | Not yet run | Student-authored |
| FR-04 | Supporting contract: validate_date_time (local naive datetime, minute precision) | T-09 | Domain, boundary | `test_domain.py::test_datetime_with_seconds_or_timezone_is_rejected` | Seconds or timezone raises ValueError | Not yet run | Student-authored |
| FR-01 | AC-01.1 (complete evidence: stored through the workflow) | T-10 | Service, positive | `test_services.py::test_register_patient_stores_and_returns_same_object` | Registered patient is stored and find_patient returns the same object | Not yet run | Student-authored |
| FR-01 | AC-01.2 | T-11 | Service, negative | `test_services.py::test_duplicate_patient_id_is_rejected_without_overwrite` | Duplicate ID raises ValueError; original patient unchanged | Not yet run | Student-authored |
| FR-02 | AC-02.1 | T-12 | Service, positive | `test_services.py::test_find_patient_returns_stored_patient` | Lookup returns the same registered object | Not yet run | Student-authored |
| FR-02 | AC-02.2 | T-13 | Service, negative | `test_services.py::test_find_unknown_patient_raises_lookup_error` | Valid unknown ID raises LookupError; blank ID raises ValueError | Not yet run | Student-authored |
| FR-03 | Supporting contract: practitioner lookup over registered objects | T-14 | Service, positive and negative | `test_services.py::test_find_practitioner_returns_stored_or_raises` | Registered ID returns the stored object; unknown ID raises LookupError | Not yet run | Student-authored |
| FR-04 | AC-03.1 (complete evidence) | T-15 | Service, positive | `test_services.py::test_book_appointment_stores_scheduled_appointment` | Booking with registered participants stores a SCHEDULED appointment | Not yet run | Student-authored |
| FR-04 | AC-03.2 | T-16 | Service, negative | `test_services.py::test_booking_unknown_participant_is_rejected` | Unknown patient or practitioner raises LookupError; nothing stored | Not yet run | Student-authored |
| FR-05 | AC-04.1 | T-17 | Service, negative | `test_services.py::test_same_practitioner_same_time_conflict_is_rejected` | Conflict raises ValueError; only the first booking remains | Not yet run | Student-authored |
| FR-05 | AC-04.2 | T-18 | Service, positive | `test_services.py::test_different_practitioner_same_time_is_allowed` | Booking succeeds for a different practitioner at the same time | Not yet run | Student-authored |
| FR-05 | Supporting contract: only SCHEDULED appointments conflict | T-19 | Service, boundary | `test_services.py::test_cancelled_booking_does_not_block_slot` | Rebooking a cancelled slot succeeds | Not yet run | Student-authored |
| FR-06 | AC-05.1 | T-20 | Service, positive | `test_services.py::test_cancel_returns_same_object_with_cancelled_status` | Same stored object returned with status CANCELLED | Not yet run | Student-authored |
| FR-07 | AC-05.2 | T-21 | Service, positive | `test_services.py::test_cancelled_appointment_is_retained_and_listed` | Found by find_appointment and present in list_appointments | Not yet run | Student-authored |
| FR-06 | AC-05.3 | T-22 | Service, negative | `test_services.py::test_repeated_cancellation_via_service_is_rejected` | Second cancel raises ValueError; status unchanged | Not yet run | Student-authored |
| FR-06 | Supporting contract: unknown ID raises LookupError; blank ID raises ValueError | T-23 | Service, negative | `test_services.py::test_cancel_unknown_appointment_raises_lookup_error` | Valid unknown ID raises LookupError; blank ID raises ValueError; stored records unchanged | Not yet run | Student-authored |
| FR-08 | AC-06.1 | T-24 | Service, positive | `test_services.py::test_find_appointment_returns_known_appointment` | The same stored appointment is returned | Not yet run | Student-authored |
| FR-04 | Supporting contract: duplicate appointment ID is rejected | T-25 | Service, negative | `test_services.py::test_duplicate_appointment_id_does_not_overwrite` | ValueError; original appointment unchanged | Not yet run | Student-authored |

## C Test Design

Use descriptive test names such as test_cancel_changes_status() or test_blank_patient_id_is_rejected(). Explain what new evidence each case adds.

| Test ID | Requirement | Acceptance criterion | Positive / Negative / Boundary | Test intention | Observable result expected | Added evidence beyond supplied tests |
|---|---|---|---|---|---|---|
| T-01 | FR-01 | AC-01.1 (partial: construction only) | Positive | A valid Patient keeps its trimmed ID and its name | `patient_id == "P1"` and `name == "Alice Example"` when built from " P1 " and a valid name | Checks the actual stored values and trimming, not just that an object exists |
| T-02 | FR-01 | Validation contract (not AC-01.2) | Negative | A blank patient ID is rejected at construction | `ValueError` is raised | Checks the specific exception for a blank ID |
| T-03 | FR-01 | Validation contract: required name | Boundary | A whitespace-only patient name is rejected | `ValueError` is raised | Covers the whitespace boundary, not just an empty string |
| T-04 | FR-03 | Supporting contract: practitioner fields required | Positive and negative | A Practitioner stores valid trimmed ID, name and specialty; a blank specialty is rejected | Stored values match; blank specialty raises `ValueError` | Covers practitioner validation, which the patient tests do not |
| T-05 | FR-04 | AC-03.1 (partial: construction only) | Positive | A new Appointment starts in the SCHEDULED state | `status is AppointmentStatus.SCHEDULED` | Checks the initial status explicitly |
| T-06 | FR-06 | AC-05.1 | Positive | Cancelling a SCHEDULED appointment changes its status | `status is AppointmentStatus.CANCELLED` after `cancel()` | Starts from a known SCHEDULED state, so the change is proven |
| T-07 | FR-06 | AC-05.3 | Negative | Cancelling twice is rejected | Second `cancel()` raises `ValueError`; status stays CANCELLED | Checks the status after rejection, not only the exception |
| T-08 | FR-06 | Supporting contract: Appointment.cancel guard | Negative | A COMPLETED appointment cannot be cancelled | `ValueError` is raised; status stays COMPLETED | Uses the COMPLETED-at-construction option to test the guard |
| T-09 | FR-04 | Supporting contract: validate_date_time | Boundary | A datetime with seconds, or with a timezone, is rejected | `ValueError` is raised for each | Tests the minute-precision and naive-time boundary |
| T-10 | FR-01 | AC-01.1 (complete: through the workflow) | Positive | Registering a patient through the service stores it and returns the same object | Returned patient is the stored one (`find_patient("P1") is patient`); appears once in `list_patients()` | Proves storage through the workflow, not construction alone |
| T-11 | FR-01 | AC-01.2 | Negative | A second registration with an existing ID is rejected without overwriting | `ValueError`; the original patient and its name are unchanged; one patient in the list | Verifies unchanged state after rejection |
| T-12 | FR-02 | AC-02.1 | Positive | Looking up a registered patient returns the stored object | `find_patient("P1") is patient` | Checks object identity, not equality or existence |
| T-13 | FR-02 | AC-02.2 | Negative | An unknown valid ID reports absence; a blank ID is invalid | `LookupError` for the unknown ID; `ValueError` for blank; no patient added | Separates absence from invalid input |
| T-14 | FR-03 | Supporting contract: practitioner lookup | Positive and negative | A registered practitioner is returned; an unknown ID reports absence | Same stored object; `LookupError` for unknown | Covers practitioner lookup alongside patient lookup |
| T-15 | FR-04 | AC-03.1 (complete) | Positive | Booking registered participants stores a SCHEDULED appointment | Returned appointment is the stored one, with the right patient, practitioner, time and SCHEDULED status | Checks the full booking result through the service |
| T-16 | FR-04 | AC-03.2 | Negative | Booking an unknown patient or practitioner is rejected | `LookupError`; `list_appointments()` stays empty | Shows nothing is stored when the booking fails |
| T-17 | FR-05 | AC-04.1 | Negative | The same practitioner at the same exact time as a SCHEDULED appointment is rejected | `ValueError`; only the first appointment remains | Checks both the rejection and the unchanged state |
| T-18 | FR-05 | AC-04.2 | Positive | A different practitioner at the same time is allowed | Booking succeeds; both appointments are stored | Shows the conflict rule is specific to the practitioner |
| T-19 | FR-05 | Supporting contract: only SCHEDULED appointments conflict | Boundary | A cancelled booking does not block its slot | Rebooking the same practitioner and time succeeds after cancellation | Links the conflict rule to cancellation |
| T-20 | FR-06 | AC-05.1 | Positive | Cancelling through the service returns the same appointment with CANCELLED status | Returned object is the stored one; status CANCELLED | Checks identity and status through the service |
| T-21 | FR-07 | AC-05.2 | Positive | A cancelled appointment is still retrievable and listed | `find_appointment(id) is appointment`; it appears in `list_appointments()`; status CANCELLED | Proves history is retained |
| T-22 | FR-06 | AC-05.3 | Negative | A repeated cancellation through the service is rejected | `ValueError`; status stays CANCELLED; appointment still stored | Verifies the state after the service-level rejection |
| T-23 | FR-06 | Supporting contract: unknown and blank IDs | Negative | An unknown ID reports absence; a blank ID is invalid | `LookupError` for unknown; `ValueError` for blank; stored records unchanged | Covers the error contract at the service boundary |
| T-24 | FR-08 | AC-06.1 | Positive | A known appointment ID returns that appointment | `find_appointment("A1") is appointment` | Checks the exact stored object |
| T-25 | FR-04 | Supporting contract: duplicate appointment ID | Negative | A duplicate appointment ID does not overwrite the original | `ValueError`; the original appointment keeps its details | Verifies no overwrite on duplicate IDs |

## D Arrange Act Assert Record

Arrange test data; act on one meaningful behaviour; assert the required observable outcome. Use the specific current exception with pytest.raises where needed.

Fixed synthetic data used throughout: patient "P1" / "Alice Example", practitioner "D1" / "Dr Sample" / "GP", appointment "A1", date and time `datetime(2026, 11, 10, 9, 0)`. Each service test creates a fresh `SmartCareDataStore` and the three services on that same store.

| Test ID | Arrange | Act | Assert | Why meaningful / why assertion proves criterion |
|---|---|---|---|---|
| T-01 | Valid ID with surrounding spaces (" P1 ") and a valid name | Construct `Patient(" P1 ", "Alice Example")` | `patient.patient_id == "P1"` and `patient.name == "Alice Example"` | Compares the stored values with the expected ones, so it fails if trimming or storage is wrong. It is partial evidence for AC-01.1 because it does not involve the store. |
| T-02 | A blank ID string | Construct `Patient("", "Alice Example")` inside `pytest.raises(ValueError)` | `ValueError` is raised | The contract names ValueError for invalid fields, so the specific exception shows the blank ID is rejected for the right reason. |
| T-03 | A valid ID and a whitespace-only name | Construct `Patient("P1", "   ")` inside `pytest.raises(ValueError)` | `ValueError` is raised | Tests the whitespace boundary, which an `if not name` check alone would miss. |
| T-04 | Valid practitioner values, and a second set with a blank specialty | Construct both | Valid one has trimmed stored values; the blank specialty raises `ValueError` | Shows required fields are validated and valid values are kept exactly. |
| T-05 | Patient, practitioner and a valid datetime | Construct an `Appointment` without a status argument | `appointment.status is AppointmentStatus.SCHEDULED` | Proves the initial state the cancellation tests depend on. |
| T-06 | A new SCHEDULED appointment | Call `appointment.cancel()` | `appointment.status is AppointmentStatus.CANCELLED` | Starting from SCHEDULED, the status change can only come from the cancellation, so it proves AC-05.1. |
| T-07 | An appointment already cancelled once | Call `cancel()` a second time inside `pytest.raises(ValueError)` | `ValueError` is raised, then `status is AppointmentStatus.CANCELLED` | The second assertion proves the failed operation left the state unchanged, which is the AC-05.3 requirement. |
| T-08 | An appointment built with `status=AppointmentStatus.COMPLETED` | Call `cancel()` inside `pytest.raises(ValueError)` | `ValueError` is raised, then `status is AppointmentStatus.COMPLETED` | Exercises the guard for the only other non-SCHEDULED state and shows no state change. |
| T-09 | One datetime with non-zero seconds and one with a timezone | Construct an `Appointment` with each inside `pytest.raises(ValueError)` | `ValueError` is raised for each | Covers both parts of the documented naive, minute-precision rule with the specific exception. |
| T-10 | Fresh store and `PatientService` | `patient = patient_service.register_patient("P1", "Alice Example")` | `store.find_patient("P1") is patient` and `store.list_patients() == [patient]` | Identity plus the list shows the patient was really stored through the workflow, so it is complete evidence for AC-01.1. |
| T-11 | A registered patient "P1" | Register "P1" again with a different name inside `pytest.raises(ValueError)` | `ValueError`, then the stored patient's name is still "Alice Example" and there is one patient | Proves AC-01.2 and that the duplicate did not overwrite the original. |
| T-12 | A registered patient | `found = patient_service.find_patient("P1")` | `found is patient` | Identity shows the real stored object is returned, not a new one. |
| T-13 | A fresh store with one registered patient | Look up "P9" (valid, unknown) and a blank ID, each inside `pytest.raises` | `LookupError` for "P9"; `ValueError` for the blank ID; `list_patients()` unchanged | Separates absence from invalid input, as the contracts require, and checks no record was created. |
| T-14 | A registered practitioner | Look up "D1" and an unknown "D9" | "D1" returns the stored object; "D9" raises `LookupError` | Shows lookup returns the real object and reports absence correctly. |
| T-15 | Registered patient and practitioner | `appointment = appointment_service.book_appointment("A1", "P1", "D1", when)` | `store.find_appointment("A1") is appointment`; its patient and practitioner are the registered objects; `status is SCHEDULED`; the time matches | Checks every field of the AC-03.1 outcome through the real workflow. |
| T-16 | Registered practitioner only, then registered patient only | Book with an unknown patient, then an unknown practitioner, each inside `pytest.raises(LookupError)` | `LookupError` each time, then `list_appointments() == []` | The empty list proves the rejected bookings stored nothing, which is AC-03.2. |
| T-17 | A SCHEDULED booking for "D1" at the chosen time | Book "A2" for "D1" at the same time inside `pytest.raises(ValueError)` | `ValueError`, then `list_appointments() == [first]` | Shows the conflict is rejected and the existing state is unchanged, which is AC-04.1. |
| T-18 | A SCHEDULED booking for "D1"; a second registered practitioner "D2" | Book "A2" for "D2" at the same time | Booking succeeds and both appointments are stored | Shows the rule applies to the same practitioner only (AC-04.2). |
| T-19 | A booking for "D1" that has been cancelled | Book "A2" for "D1" at the same time | Booking succeeds and "A2" is stored | Shows a cancelled booking does not occupy the slot, which matches the conflict definition. |
| T-20 | A SCHEDULED appointment stored through the service | `result = appointment_service.cancel_appointment("A1")` | `result is appointment` and `result.status is AppointmentStatus.CANCELLED` | Identity shows the stored object was cancelled, not a copy. |
| T-21 | A cancelled appointment | Call `find_appointment("A1")` and `list_appointments()` | `found is appointment`, it is in the list, and `status is CANCELLED` | Directly proves AC-05.2, because the history is still available after cancelling. |
| T-22 | A cancelled appointment | Cancel again through the service inside `pytest.raises(ValueError)` | `ValueError`, then the status is still CANCELLED and the appointment is still stored | Proves AC-05.3 at the service level, including unchanged state. |
| T-23 | A fresh store with one SCHEDULED appointment | Cancel "A9" (unknown) and a blank ID, each inside `pytest.raises` | `LookupError` for "A9"; `ValueError` for blank; "A1" is still SCHEDULED | Checks the error contract and that existing records are untouched. |
| T-24 | A stored appointment | `found = appointment_service.find_appointment("A1")` | `found is appointment` | Identity proves AC-06.1 returns the exact stored appointment. |
| T-25 | A stored appointment "A1" | Book another appointment with ID "A1" inside `pytest.raises(ValueError)` | `ValueError`, then `find_appointment("A1") is first` and the list has one item | Shows the duplicate did not overwrite the original record. |

## E Domain Test Evidence

Cover Patient/Practitioner construction and validation; Appointment construction, initial status, cancellation and illegal/repeated transitions. Preserve the four reference intentions described in handout Part C.

The four reference intentions are T-02 (blank patient ID rejected), T-05 (new appointment starts SCHEDULED), T-06 (cancellation changes status) and T-07 (repeated cancellation rejected).

| Test ID | Behaviour | Test file/function | Result |
|---|---|---|---|
| T-01 | Patient keeps the trimmed ID and name | `project/tests/test_domain.py::test_patient_stores_trimmed_id_and_name` | Not yet run |
| T-02 | Blank patient ID is rejected with ValueError (reference intention) | `project/tests/test_domain.py::test_blank_patient_id_is_rejected` | Not yet run |
| T-03 | Whitespace-only patient name is rejected with ValueError | `project/tests/test_domain.py::test_whitespace_only_patient_name_is_rejected` | Not yet run |
| T-04 | Practitioner stores valid trimmed fields; blank specialty is rejected | `project/tests/test_domain.py::test_practitioner_requires_id_name_and_specialty` | Not yet run |
| T-05 | New appointment starts SCHEDULED (reference intention) | `project/tests/test_domain.py::test_new_appointment_starts_scheduled` | Not yet run |
| T-06 | Cancelling a SCHEDULED appointment gives CANCELLED (reference intention) | `project/tests/test_domain.py::test_cancel_changes_status` | Not yet run |
| T-07 | Repeated cancellation is rejected and status stays CANCELLED (reference intention) | `project/tests/test_domain.py::test_repeated_cancellation_is_rejected` | Not yet run |
| T-08 | Cancelling a COMPLETED appointment is rejected and status stays COMPLETED | `project/tests/test_domain.py::test_cancel_completed_appointment_is_rejected` | Not yet run |
| T-09 | Datetime with seconds or a timezone is rejected | `project/tests/test_domain.py::test_datetime_with_seconds_or_timezone_is_rejected` | Not yet run |

## F Service Test Evidence

Use fresh shared SmartCareDataStore state, registered objects and completed Stage 6 services.

| Test ID | Behaviour | Requirement / criterion | Test file/function | Result |
|---|---|---|---|---|
| T-10 | Registered patient is stored and returned as the same object | FR-01 / AC-01.1 | `project/tests/test_services.py::test_register_patient_stores_and_returns_same_object` | Not yet run |
| T-11 | Duplicate patient ID is rejected and the original is not overwritten | FR-01 / AC-01.2 | `project/tests/test_services.py::test_duplicate_patient_id_is_rejected_without_overwrite` | Not yet run |
| T-12 | Known patient lookup returns the stored patient | FR-02 / AC-02.1 | `project/tests/test_services.py::test_find_patient_returns_stored_patient` | Not yet run |
| T-13 | Unknown patient raises LookupError; blank ID raises ValueError | FR-02 / AC-02.2 | `project/tests/test_services.py::test_find_unknown_patient_raises_lookup_error` | Not yet run |
| T-14 | Practitioner lookup returns the stored object or raises LookupError | FR-03 / supporting contract (practitioner lookup) | `project/tests/test_services.py::test_find_practitioner_returns_stored_or_raises` | Not yet run |
| T-15 | Booking registered participants stores a SCHEDULED appointment | FR-04 / AC-03.1 | `project/tests/test_services.py::test_book_appointment_stores_scheduled_appointment` | Not yet run |
| T-16 | Booking an unknown patient or practitioner is rejected; nothing stored | FR-04 / AC-03.2 | `project/tests/test_services.py::test_booking_unknown_participant_is_rejected` | Not yet run |
| T-17 | Same practitioner at the same time is rejected; state unchanged | FR-05 / AC-04.1 | `project/tests/test_services.py::test_same_practitioner_same_time_conflict_is_rejected` | Not yet run |
| T-18 | Different practitioner at the same time is allowed | FR-05 / AC-04.2 | `project/tests/test_services.py::test_different_practitioner_same_time_is_allowed` | Not yet run |
| T-19 | A cancelled booking does not block its slot | FR-05 / supporting contract (only SCHEDULED conflicts) | `project/tests/test_services.py::test_cancelled_booking_does_not_block_slot` | Not yet run |
| T-20 | Cancellation returns the same appointment with CANCELLED status | FR-06 / AC-05.1 | `project/tests/test_services.py::test_cancel_returns_same_object_with_cancelled_status` | Not yet run |
| T-21 | Cancelled appointment is still retrievable and listed | FR-07 / AC-05.2 | `project/tests/test_services.py::test_cancelled_appointment_is_retained_and_listed` | Not yet run |
| T-22 | Repeated cancellation is rejected; status and record unchanged | FR-06 / AC-05.3 | `project/tests/test_services.py::test_repeated_cancellation_via_service_is_rejected` | Not yet run |
| T-23 | Unknown appointment ID raises LookupError; blank ID raises ValueError | FR-06 / supporting contract (unknown and blank IDs) | `project/tests/test_services.py::test_cancel_unknown_appointment_raises_lookup_error` | Not yet run |
| T-24 | Known appointment ID returns that appointment | FR-08 / AC-06.1 | `project/tests/test_services.py::test_find_appointment_returns_known_appointment` | Not yet run |
| T-25 | Duplicate appointment ID does not overwrite the original | FR-04 / supporting contract (duplicate appointment ID) | `project/tests/test_services.py::test_duplicate_appointment_id_does_not_overwrite` | Not yet run |

## G Negative and Boundary Cases

Connect cases to actual contracts and verify unchanged state after rejection.

| Behaviour | Boundary/invalid input | Expected result | Test ID |
|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] |

## H GitHub Copilot Test Design

Select ONE real acceptance criterion. Complete human-first fields before using Copilot. Do not require an accepted generated test.

Requirement: [complete]
Acceptance criterion: [quote]
Behaviour to test: [complete]
Human-first test idea/categories: [complete]
Prompt and purpose: [complete or link]

For each significant candidate, copy this entry as needed:
- Copilot test idea/candidate: [complete]
- What it claims to verify: [complete]
- Requirement trace: [complete]
- Assertion quality: [complete]
- Human critique: [complete]
- Decision: [Accept / Modify / Reject]
- Reason: [complete]
- Final test reference if accepted/modified: [link or not retained]
- Actual verification result: [complete; do not claim an unrun test passed]

Before accepting: traces to a requirement/criterion; can fail for the right reason; assertion checks required behaviour; no invented business rule; no unnecessary private implementation dependence. Reject/modify weak assertions, invented requirements, excessive mocking, duplicates, wrong exceptions, obsolete architecture and unnecessary dependencies.

## I Weak Copilot Test Reflection

Which Copilot-generated test looked convincing but was weak? [response]
Why was it weak? [response]
How did you strengthen it? [response]
Accepted / modified / rejected test decisions and evidence: [link actual decisions in H]

## J Regression Run

Run python -m pytest from project/. Retain all accumulated tests. Record the tested SHA accurately.

| Command | Working directory | Code SHA | Passed | Failed | Failure summary | Product defect / test defect / unresolved | Evidence and interpretation |
|---|---|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

Individual test runs and changed-order independence evidence: [commands, results, links]
Optional tutor-led demonstration notes: [optional; leave blank if not used]
A meaningful test should detect a relevant incorrect result. Students do not have to perform the demonstration or submit failure/restoration evidence for assessment. The tutor restores the example and reruns its tests. This is not a Stage 8 fault activity.
Requirement → test → failure/observation → diagnosis → change → verification: [concise links where applicable]

## K What the Suite Still Does Not Prove

What does your test suite still not prove? [response]
Coverage if used: [result or not used]
Which uncovered areas matter, and why does coverage percentage alone not establish correctness? [response]
Optional fixtures/parametrisation used and why, if any: [response or not used]

## L Git and Review Evidence

Use links rather than copying GitHub history. Continue the Stage 6 workflow; no commit/PR count, conflict or individual test quota is imposed.

| Issue/task | Branch | PR | Reviewer | Key feedback | Outcome |
|---|---|---|---|---|---|
| [complete] | [complete] | [complete] | [complete] | [complete] | [complete] |

## M Contribution Evidence

Record actual work in test design, implementation, review, traceability, diagnosis, necessary fixes and integration. Do not include confidential peer ratings.

| Member | Actual contribution | Evidence link |
|---|---|---|
| [complete] | [complete] | [complete] |

## N Formative Questions

1. What question does verification answer?
Verification is the process of checking code syntax and design specifications set by the client. It answers the question "Are we building this correctly?" 

2. What question does validation answer?
Checks whether the program satisfies real world needs. This involves checking code and features of the program to ensure they match the required standards for intended use. It answers the question "Are we building the right product?" 

3. What is a unit test?
A unit test is a small automated check that verifies a piece of your code (most commonly a function) works correctly independently. 

4. What is a pytest fixture?
A pytest fixture is a reusable function that sets up test data or resources including but not excluded to objects. Tests receive it by naming it as an argument so it cleans it up afterwards. 

5. What is parametrisation in pytest?
Parametrisation is used to run one test function agains many input/expected outut pairs, which avoids copy-pasted tests. 

6. What is regression testing?
Regression testing is where you re-run existing test after a to confirm that the function works as intended after code changes. 

7. What does code coverage tell us, and what does it not prove?
Code coverage tells us the percentage of code executed during a test. It doesn't prove whether the code is valid and it doesn't perform any test cases. 

8. What makes an assertion weak?
Weak assertion is one that would pass when the code is wrong. 

9. What is the appropriate role of GitHub Copilot as a test assistant?
Using Copilot as a test assistant is helpful when drafting tests/edge case ideas. You must still run, review, and understand the code because you are still responsible for the code. 

10. What is the Stage 7 engineering rule?


## O Stage Completion

Tested Stage 7 main SHA: [complete]
Full-suite result: [complete]
Unresolved defects and effect on baseline: [complete or none]
Clean working tree and integration evidence: [complete]
Stage 8 handover status: [complete; no Stage 8 work assigned]
All tutorial/formative responses and traceability/Copilot decisions complete: [confirm]
