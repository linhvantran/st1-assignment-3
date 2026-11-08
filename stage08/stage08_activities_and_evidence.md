# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [Mon 9:30-11:30 Group 1]
Members and UG/PG cohorts: [Van Tran (@linhvantran), Xi Chen (@cz1295768-ui), Chars (@charatwukki), Thomas Pollock (@CrowdedGolf)]
Record owner / contribution links for each member: 

charatwukki and chara3kki [Chars]: Sections B, E and F for F8-01, K, J, and F8-01 repair 18f0173e614a76da644ebf57e02b8d012b368d2d; Created issues for F8-02 and F8-01 https://github.com/linhvantran/st1-assignment-3/issues/14 and https://github.com/linhvantran/st1-assignment-3/issues/13 respectively. 

Use concise results and accessible artefact links rather than copying entire logs. Keep human-first entries before consulting GitHub Copilot. Link shared evidence once; do not repeat it across sections. No entries below are specimen answers or claimed results.

## A. Tutorial activities

### A.1 Classify all five statements
For each, choose symptom, evidence or hypothesis/opinion, and explain your reason. These are discussion statements, not confirmed diagnoses.
- Appointment disappears after cancellation.
  - Symptom: This is what happens when the problem occurs, it might not be the root cause of the problem.
- The data-store removal path is probably being called.
  - Hypothesis/opinion: This is what is thought to be happening, this statement does not prove it.
- The failing test shows store.find_appointment('A1') returns None.
  - Evidence: The failing pytest points to the fact that somthing is going wrong with the lookup function.
- The service layer is badly designed.
  - Hypothesis/opinion: Does not point out what specific parts are badly designed and how it is badly designed.
- Traceback points to smartcare/services.py line 42 in the example.
The example line number is illustrative; inspect the actual line in your run. The removal hypothesis must be tested against the current project, which has no public delete operation.
  - Evidence: Tracebacks point towards where the program is erroring out.

### A.2 Build a debugging record
Choose the cancelled-history scenario or a same-practitioner/time booking. Before changing code, record expected behaviour, observed behaviour, minimal reproduction, a hypothesis and evidence to inspect. Use a requirement to justify the expectation. Keep the initial hypothesis even if later evidence disproves it.

Scenario: Cancelled history:

#### Expected bahiviour:
- Cancelled appointment is retained in datastore with `AppointmentStatus.SCHEDULED` becoming `AppointmentStatus.CANCELLED` after cancellation.

#### Observed behaviour:
- Test `test_cancelled_appointment_is_retained_and_listed` fails with `LookupError: Appointment not found`.
  - This test fails with this LookupError when using the `find_appointment()` function after cancelling a previously valid appointment.
- `test_repeated_cancellation_via_service_is_rejected` fails with `LookupError: Appointment not found`.
  - This test fails with this LookupError when using the `cancel_appointment()` function on a previously cancelled appointment that was previously valid.

#### Minimal reproduction:
- Previously valid appointment cannot be found via the `find_appointment()` function after using the `cancel_appointment()` function on the previously valid appointment.

#### Hypothesis:
- When an appointment is being cancelled using the `cancel_appointment()` function it is being deleted from the datastore instead of changing `AppointmentStatus.SCHEDULED` to `AppointmentStatus.CANCELLED`.

#### Evidence:
- Both failing tests raise a LookupError when referencing the datastore for a previously cancelled appointment ID that was once valid.

### A.3 Test defect or product defect
A test expects cancelled appointments to be deleted, but FR-07 says history must be retained. What should be changed? Explain why. Also decide whether a test expecting different practitioners at the same time to conflict reflects AC-04.2. Do not assume every failing test is correct.

The test should be changed as "history must be retianed" is a functional requirement that the program must follow while the test should follow those requirements to test if the code also folows those requirements.

### A.4 Refactoring smell hunt
Consider a hypothetical 70-line AppointmentService method containing duplicate status strings, direct collection manipulation, printing, validation and four nested conditionals. Identify the smells and propose small refactorings that preserve required behaviour. The direct collection work replaces the old storage-specific scenario; use the existing SmartCareDataStore boundary. Do not implement an extra architecture.
Classify these proposed changes as refactoring, repair or feature: rename appt to appointment; extract a repeated conflict helper; add rescheduling; restore retained cancellation lookup; replace a magic status string with the existing enum. Explain the behaviour that must remain unchanged.

#### Rename appt to appointment:
- Refactoring. Functionality of appt must remain the same but the name and all references will be changed to appointment.

#### Extract a repeated conflict helper:
- Repair. The repeated conflict helper will need to be extracted and repaired. All other unrelated parts of the program remain the same.

#### Add rescheduling:
- Feature. Most of the underlying scheduling code will remain the same but a new feature to handle rescheduling will need to be created to interact with the existing scheduling code.

#### Restore retained cancellation lookup:
- Repair. The part of the code causing the cancellation infromation to need to be restored will need to be repaired to stop this issue.

#### Replace a magic status string with existing enum:
- Refactoring. Fuctionality based on the states and the states themselves remain the same but how the states are stored changes.

### A.5 Traceback and hypothesis ranking
Using one actual failure, identify its exception/assertion, expected and observed values, test line, application call path and supporting requirement. List three plausible causes and rank them by fit with the available evidence. For each cause, name a check that could distinguish it from the others. Explain why a traceback alone does not establish the cause.

#### Failure:
- Test `test_cancelled_appointment_is_retained_and_listed` from `test_services.py`

#### Exception / assertion:
- `LookupError: Appointment not found`

#### Expected values:
- `appointment == ("A1", "P1", "D1", datetime(2026, 11, 10, 9, 0), AppointmentStatus.SCHEDULED)` and `appointments.find_appointment("A1") == ("A1", "P1", "D1", datetime(2026, 11, 10, 9, 0), AppointmentStatus.CANCELLED)`
- pytest asserts that `appointment` is `appointments.find_appointment("A1")` meaning that `appointment` and `appointments.find_appointment("A1")` are both the same object despite the cancellation.

#### Observed values:
- `appointment == ("A1", "P1", "D1", datetime(2026, 11, 10, 9, 0), AppointmentStatus.SCHEDULED)` is still true as the program was successful in creating and storing the appointment using the `appointments.book_appointment()` function as the `appointments.cancel_appointment()` function successfully found and cancelled "A1" as there were no errors raised during cancellation. `appointments.find_appointment("A1") == ("A1", "P1", "D1", datetime(2026, 11, 10, 9, 0), AppointmentStatus.CANCELLED)` is no loger true as the `appointments.find_appointment()` function can no longer find "A1" and raises a LookupError.
- pytest cannot assert that `appointment` is `appointments.find_appointment("A1")` as `appointments.find_appointment("A1")` raises a LookupError.

#### Test line:
- line `142` in `test_services.py`

#### Application call path and supporting requirement:
- Path: `test/test_services`
- Supporting requirements: FR-07 (Retain cancelled history) and AC-05.1 (Cancelling a SCHEDULED appointment changes it to CANCELLED)

#### Plausable causes:
1. Cancelled appointment was deleted.
  - Distingusihing check: Check if appointment "A1" still exists in datastore after using `appointments.cancel_appointment()`. If appointment "A1" no longer exists in the datastore after running `appointments.cancel_appointment("A1")`, the cancel function or one of its downstream functions is deleting the appointment.

2. Cancelling an appointment overwrites the wrong part of the list.
  - Distinguishing check: Check whether parts of appointment "A1" get overwritten in the datastore after using `appointments.cancel_appointment()`. If parts of appointment "A1" are overwritten or jumbled in unexpected ways after using `appointments.cancel_appointments("A1")`, there is likely a problem with how the cancel function and its downstream functions interact with the datastore.

3. There is an issue with the lookup system.
  - Distinguishing check: Check whether appointment "A1" is intact in the datastore and try looking it up using `appointments.find_appointment("A1")`. If this fails despite appointment "A1" being correct in the datastore, there is likely an issue with the lookup system.

#### Why can't a traceback alone establish the cause of an issue?
A traceback alone cannot establish the cause of an issue becasue, 

### A.6 Exit question
Why is changing code immediately after seeing a failure often a poor debugging strategy?

Changing code immediately after seeing a failure is a poor debugging stratergy as this approach does not let you think deeply about what could have gone wrong, what the likely causes are, and stratergies that could be used to fix the problem.

## B. Stage 7 baseline and safe preparation

- Stage 7 code SHA and requirement baseline: baac2416c93ca8fdf426580ceb94ed3c31118d74

- Baseline test command / working directory / observed result / evidence: python -m pytest -q / project/ / 5 failed, 32 passed in 0.66s / ================================ short test summary info ================================
FAILED tests/test_services.py::test_same_practitioner_same_time_conflict_is_rejected - Failed: DID NOT RAISE <class 'ValueError'>
FAILED tests/test_services.py::test_different_practitioner_same_time_is_allowed - ValueError: Practitioner already has a SCHEDULED appointment at this time
FAILED tests/test_services.py::test_cancelled_appointment_is_retained_and_listed - LookupError: Appointment not found
FAILED tests/test_services.py::test_repeated_cancellation_via_service_is_rejected - LookupError: Appointment not found
FAILED tests/test_starter.py::test_conflict_rule_and_different_practitioner - Failed: DIDNOT RAISE <class 'ValueError'>
5 failed, 32 passed in 0.34s

- Clean preparation SHA if a record-only commit followed Stage 7: No record-only commit came between Stage 7 and preparation. 

- Branch and preparer / how teammates obtained this branch: git switch main, git fetch origin, git switch --track origin/debug/stage08. Chars and Pranav Gupta prepared the branch and before are the commands taht allow teammates to obtain this branch. 

- Downloaded tool version, source SHA256 and --check outcome: Stage 8 tool 1.1, 986c5445532ffd1d85e88639b6b6f34b84e15b2bbfc1882511a96938c3b641f6, CHECK ONLY: project unchanged; both proposed fault signatures verified in a temporary copy 

- --apply and --verify output summaries / artefact references: 
- --apply output: Stage 8 tool 1.1, 986c5445532ffd1d85e88639b6b6f34b84e15b2bbfc1882511a96938c3b641f6,PREPARED: F8-01 practitioner conflict; F8-02 retained-history lookup. Verified expected failures: test_f8_01_conflict; test_f8_02_history. 
- --verify output: VERIFIED: exactly 2 expected failures; both approved symtom signatures present. 

- Bounded diff inspected and recovery location (not committed): Inspect using "git show --stat dc66e56",  project/smartcare/data_store.py | 29 +++++++++++------------------
 1 file changed, 11 insertions(+), 18 deletions(-). Recovery backup and hash record are in project/.stage8_faults/, which is a local recovery metadata ignored by the .gitignore file and not commited. 

- Prepared faulty-state commit SHA: dc66e5633e6c32453e46b24999270e2c02cfa137

- Preparation or recovery issues and resolution, if any: 
None. --check, --apply and --verify all ran successfully, and --restore was not needed. 

- Initial prepared full-suite command / result / key failures: 
python -m pytest -q in project/ on dc66e5633e6c32453e46b24999270e2c02cfa137

RESULT: 

ERROR project/tests/test_data_store.py
ERROR project/tests/test_domain.py
ERROR project/tests/test_services.py
ERROR project/tests/test_starter.py

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: Booking a second SCHEDULED appointment for the same practitioner at the same datetime with with distinct appointment IDs and registered patients is not rejected. Booking a different practitioner at the same datetime is wrongly rejected showing "ValueError: Practitioner already has a SCHEDULED appointment at this time."
- Expected behaviour and requirement: A same practitioner SCHEDULED conflict at the same time must be rejected with ValueError (FR-05 / AC-04.1). A different practitioner at the same time must be allowed (AC-04.2). 
- Minimal synthetic reproduction steps: 1. Register in the patients P1 and P2, and practitioners D1 and D2. 2. Book A1 (P1, D1) at 2026-11-10 09:00, expected it succeeds. Book A2 (P2, D1) at the same time, Expected: ValueError. Book A3 (P2, D2) at the same time, Expected: succeeds. Check that the stored appointments are unchanged after the rejected booking. 
- Meaningful failing test path/name and exact relevant failure: project/tests/test_services.py::test_same_practitioner_same_time_conflict_is_rejected, "Failed: DID NOT RAISE <class 'ValueError'>"
- Human hypothesis and intended checks: I believe that the practitioner/time conflict check compares the wrong thing. It matches different practitioners instead of the same one. Intended checks: Inspect the conflict check in book_appointment and the store method that find a practitioner's appointments, and call that store method directly with two practitioners at the same time. 
- Supported root cause and inspected code/runtime evidence: In project/smartcare/data_store.py, has_practitioner_conflict compares 'appointment.practitioenr.practitioner_id != practitioner_id', so only other practitioners' appointments count as conflicts. This reverses FR-05 / AC-04.1 and AC-04.2. Evidence: git diff fb81c4 dc66e56 shows == changed to !=, services.py passes the correct practitioner ID, and the two practitioner tests fail in opposite directions. 
- Smallest justified fix / diff / why other behaviour is preserved: Changed != back to == on the practitioner comparison in has_practitioner_conflict. Nothing else was edited. The other behaviours were preserved because we just fixed one comparison and nothing else was changed. 
- Repair SHA / focused verification result: 18f0173e614a76da644ebf57e02b8d012b368d2d; python -m pytest tests/test_services.py -k "practitioner" in project/: 3 passed, 13 deselected in 0.05s

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: `LookupError: Appointment not found` when referencing a previously valid appointment that has been cancelled with `cancel_appointment()`
- Expected behaviour and requirement: Referencing a previously valid cancelled appointment returns the same appointment object with `AppointmentStatus.CANCELLED`. There should be no LookupError if the appointment number was vaild before the cancellation.
- Minimal synthetic reproduction steps: Previously valid appointment cannot be found via the `find_appointment()` function after using the `cancel_appointment()` function on the previously valid appointment.
- Meaningful failing test path/name and exact relevant failure:
  - Test: `test_cancelled_appointment_is_retained_and_listed`, Path: `tests\test_services.py:142`, Exact relevant failure: `LookupError: Appointment not found`
  - Test: `test_repeated_cancellation_via_service_is_rejected`, Path: `tests\test_services.py:154`, Exact relevant failure: `LookupError: Appointment not found`
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: A conditional statement inside the `find_appointment()` function within `data_store.py` has a conditional statement that results in the function returning `LookupError: Appointment not found` if the appointment has the status CANCELLED.
- Smallest justified fix / diff / why other behaviour is preserved: Removal of `and appointment.status.value != "cancelled"` from the conditional `if (appointment.appointment_id == appointment_id.strip() and appointment.status.value != "cancelled"):` on line 94 of `data_store.py`. Other behaviour will be preserved as this conditional will become `if appointment.appointment_id == appointment_id.strip():` which still checks if the appointment id is the stripped version of the input id without inclduing the part that filtered out cancelled appointments.
- Repair SHA / focused verification result: SHA: 7093bb114650416377726f7f8461fedb4a34c820 Result: 0 errors (3 non-relevant / out of scope).

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: I believe the practitioner/time conflict check comapres the wrong thing. It matches different practitioners instead of the same one. This is plausible because it explains both symptoms (a same practitioner double booking is not rejected, and a different practitioner booking at the same time is rejected.)
Evidence intended to inspect / competing explanation / discriminating check: I will inspect the conflict check in book_appointment and the data store method that find a practitioner's appointments at a time. Competing explanation: The store returns the right appoinjtments but the service applies the wrong condition to them. Discriminating check: Call the store method directly with D1 and D2 at the same datetime. If it returns the wrong appointments, the fault is in the store. If it returns the right ones, the fault is in the service. 
Member and saved sequence/time or commit showing this preceded consultation: [complete]

### F8-02 human entry
Likely cause and why plausible: `cancel_appointment()` function or one of its downstream functions deletes the appointment instead of changing `AppointmentStatus.SCHEDULED` to `AppointmentStatus.CANCELLED`. This is plausible because any function in our tests that needs to look up "A1" in the datastore fails with `LookupError: Appointment not found` after cancelling the appointment despite there being no error before cancelling the appointment.
Evidence intended to inspect / competing explanation / discriminating check:
- Evidence: Both failing tests raise `LookupError: Appointment not found` when trying to complete an opperation on "A1" after it has been cancelled with `cancel_appointment()`.
- Competing explanation(s): Somthing goes wrong with retrieving appointments via `find_appointment()` after cancellation. Cancelling appointment overwrites the wrong part of the list and error with lookup system.
- Discriminating check: To distinguish if it is an accidental deletion check if appointment "A1" still exists in the datastore itself to bypass the `find_appointment()` function after using `appointments.cancel_appointment()`. If appointment "A1" no longer exists in the datastore after running `appointments.cancel_appointment("A1")`, the cancel function or one of its downstream functions is deleting the appointment instead of setting `AppointmentStatus.CANCELLED`.
Member and saved sequence/time or commit showing this preceded consultation: Thomas (@CrowdedGolf / u3325015) [complete]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: "Observed behaviour: Booking a second SCHEDULED appointment for the same practitioner at the same datetime is not rejected. A different practitioner at that time is wrongly rejected with "Practitioner already has a SCHEDULED appointment at this time".
Expected behaviour: Same-practitioner conflicts raise ValueError (FR-05 / AC-04.1); a different practitioner at the same time is allowed (AC-04.2).
Steps to reproduce: <your reproduction steps from C>
Failing test: tests/test_services.py::test_same_practitioner_same_time_conflict_is_rejected - Failed: DID NOT RAISE <class 'ValueError'>
My hypothesis: The practitioner/time conflict check compares the wrong thing and matches different practitioners instead of the same one.

Task:
Rank the three most likely causes. For each, identify
the evidence I should inspect to distinguish it from
the other possible causes.
Do not rewrite the entire application.
Do not invent requirements.
Treat all suggested explanations as hypotheses.

Information is in the @linhvantran/st1-assignment-3 repo

Branch: debug/stage08, SHA: dc66e5633e6c32453e46b24999270e2c02cfa137"

Output reference: https://github.com/copilot/share/4a7d520a-0ba0-8c64-a110-744fe42048e6

Member: Chars (@charatwukki) 

  1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: The practitioner-ID comparison in has_practitioner_conflict is inverted (!= instead of ==), which would flag different practitioners and miss the same one. / git diff shows 'practitioner_id == practitioner_id' changed to '!= practitioner_id'; tests: 2 failed, 1 passed (same practitioner not rejected, different practitioner rejected). / Correct ? Accept: the line and the reversed behaviour both confirm it.

2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: book_appointment passes an unexpected practitioner ID to the conflict check. / Read the calls has_practitioner_conflict(practitioner.practitioner_id, date_time), so it passes the looked-up practitioner's ID and the booking datetime. dc66e56 changed only data_store.py, so the service is unchanged from Stage 7. Verdict: Wrong. Decision: Reject. The service passes the correct arguments, and the fault is the '!=" in the store's practitioenr comparison. 

3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: The datetime or status condition selects the wrong stored appointment. / Compared the datetime and status conditions before and after in git diff fb8f1c4 dc66e56, and printed AppointmentStatus.SCHEDULED.value. / The datetime condition is unchanged. The status check changed from 'is AppointmentStatus.SCHEDULED' to '.value == "scheduled"', and AppointmentStatus.SCHEDULED.value is 'scheduled', so it still selects only scheduled appointments. The reversed behaviour in both tests comes from the practitioner comparison. Verdict: Partly correct (the status line was changed, but it is not the cause). Decidsion: Modify. Not the cause of F8-01; leave unchanged in the repair, and note the magic string as a possible refactor smell. 
Final human conclusion and comparison with initial hypothesis: The root cause is in project/smartcare/data_store.py, has_practitioner_conflict. The practitioner comparison was changed from '==' to '!=', so only other practitioners' appointments count as conflicts. That reverses the reule in FR-05 / AC-04.1 and AC-04.2. This matches my initial hypothesis, which was that the check matches different practitioners instead of the same one. This is evident when checking the diff between fb8f1c4 and dc66e56 [might be cheating but this was literally the easiest way] and the reserved results of the two practitioner rests. Copilot suggestion 1 is correct and is the cause. Copilot suggestion 2 is wrong, because services.py passes the correct ID. Copilot suggestion 3 was partly correct as the status check was rewritten but still selects schedules appointments, so it is not the cause. 

### F8-02 Copilot review
Actual prompt / output reference and member:
- Prompt:
  - Observed behaviour: `LookupError: Appointment not found` when referencing a previously valid appointment that has been cancelled with `cancel_appointment()`
  Expected behaviour: Referencing a previously valid cancelled appointment returns the same appointment object with `AppointmentStatus.CANCELLED`. There should be no LookupError if the appointment number was vaild before the cancellation. 
  Steps to reproduce: Create a valid appointment and then cancel it with `cancel_appointment` then try to lookup the previously cancelled appointment.
  Failing tests: `test_cancelled_appointment_is_retained_and_listed`, Path: `tests\test_services.py:142`, Exact relevant failure: `LookupError: Appointment not found` and `test_repeated_cancellation_via_service_is_rejected`, Path: `tests\test_services.py:154`, Exact relevant failure: `LookupError: Appointment not found`
  My hypothesis: Somthing has gone wrong with either the `cancel_appointment()` function under AppointmentServices or one of its downstream functions which is causing a cancelled appointment to be deleted instead of being changed to CANCELLED.
  Relevant code: project/tests/test_services.py, project/smartcare/services.py, project/smartcare/domain.py, and project/smartcare/datastore.py

  Task:
  Rank the three most likely causes. For each, identify the evidence I should inspect to distinguish it from the other possible causes. Do not rewrite the entire application. Do not invent requirements. Treat all suggested explanations as hypotheses.
- Output reference:
  - https://github.com/copilot/share/824642ac-4ba4-8014-9012-da0dc00261e4
- Member:
    - Thomas (@CrowdedGolf / u3325015) 

Suggestions:
1. Cancelled appointments are filtered out during lookup — very likely.
In data_store.py, find_appointment returns a matching appointment only if its status is not "cancelled". The service delegates to that lookup and raises LookupError when it gets None (services.py, services.py).
To distinguish it: inspect whether the record remains in _appointments and whether the same ID is found before and after cancellation. The current code’s list method returns all stored values (data_store.py), while the finder filters by status.
  - accept, modify, or reject: Accept. This explination is the likely cause as it is similar to my first competing idea. I have checked the code and there is infact a secion in `lookup_appointment()` in `data_store.py` that makes the lookup function return a LookupError if an appointment's status is CANCELLED. This is also supported by my findings in `test_regressions.py` where I found that the cancelled appointment still exists in the datastore itself but it is not found when using the lookup function.

2. Cancellation removes or replaces the stored record — possible, but not supported by the code shown.
This would also cause lookup to fail after cancellation. However, the current service calls appointment.cancel() and returns that object without removing it, and the domain method changes only the status (services.py, domain.py).
To distinguish it: check whether "A1" is still a key in _appointments after cancellation, and whether list_appointments() still contains the original object. The test itself checks retention at test_services.py.
  - accept, modify, or rejcet: Reject. From my testing in `test_regressions.py` as the cancelled appointment still exists in the datastore post cancellation but it cannot be found when using the lookup function.

3. The service is using a different store or the lookup ID differs — less likely.
Either could make lookup return None independently of status. In the shown test setup, though, all three services share the same store (test_services.py), and the store trims the lookup ID before comparing it (data_store.py).
To distinguish it: verify the store object identity used by booking, cancellation, and lookup, and log the stored appointment ID alongside the exact lookup argument.
  - accept, modify, or reject: Reject. All of the functions refer to the same `SmartCareDataStore` class in `data_store.py`.

Final human conclusion and comparison with initial hypothesis: Evidence from deeper within the code structure disproves my intial hypothesis of `cancel_appointment()` being the cause. Deeper analysis of the code reveals that the root cause is a conditional statement within the `lookup_appointment()` function that causes it to return a `LookupError` if the appointment has been cancelled.

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | dc66e5633e6c32453e46b24999270e2c02cfa137 | python -m pytest tests/test_services.py -k "practitioner" in project/ | Artefact file in stage08 folder 092b434a0ccc54949bddfd1529e3707c8ad9177f |
| F8-01 after repair | 18f0173e614a76da644ebf57e02b8d012b368d2d | python -m pytest tests/test_services.py -k "practitioner" in project/ | Artefact File in stage08 folder dd93f02b4cfac30ee989487b2b17875396d85195 |
| F8-02 before repair | d61d05d757f82622a2c199829e9518e7c3ca0bab | cmd: python -m pytest directory: project | 5 failures (2 relevant to F8-02): `FAILED tests/test_services py::test_cancelled_appointment_is_retained_and_listed - LookupError: Appointment not found` and `FAILED tests/test_services.py::test_repeated_cancellation_via_service_is_rejected - LookupError: Appointment not found` |
| F8-02 after repair | 7093bb114650416377726f7f8461fedb4a34c820 | cmd: python -m pytest directory: project | 3 failures (0 relevant to F8-02): Previous failed tests were fixed. |
| Full suite after both repairs, before refactor | 18f0173e614a76da644ebf57e02b8d012b368d2d | python -m pytest -q in project/ | ......................................                                          [100%]
38 passed in 0.07s |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: The tests assert the requires outcomes from the requirements, not the faulty behaviour. For F8-01 they expect a same practitioner comflict to be rejected and a different practitioner to be allowed. For F8-02 they expect a cancelled appointment to be retained, found and listed, and repeated canceation to be rejected. A wrong result fails an assertion, and the rest of the suite passing shows earlier behaviour was kept. 
Unrelated failures investigated / resolution: No unrelated failures investigated. After both repairs the full suite passed with no failures, so there were no other failures to investigate. 

## H. Refactoring decision and before/after verification

Smell and exact location: Duplicated code in project/smartcare/services.py, AppointmentService.cancel_appointment repeats the LookupError that is already in AppointmentService.find_appointment. 
Small proposed structural change / why justified: This removes duplication so that the check lives in one place. It is a structural change that doesn't fix any defect and adds no feature. 
External behaviour to preserve / relevant tests: cancel_appointment must still return the same stored object with CANCELLED status. Must raise LookupError('Appointment not found') for an unknown ID. Must raise ValueError for an invalid transition without changing state, and keep the appointment in the store (FR-06/07, BR-07, AC-05.2), Relevant tests: The chancellation and retained history tests in tests/test_services.py and tests/test_regressions.py
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: In project/smartcare/services.py, cancel_appointment now calls 'self.find_appointment(appointment_id)' instead of repeating the lookup check. (3 lines replaced by 1). Commit 018f51595f585c20f673b2174b504c9eece8c880
Focused and full after-refactor commands / working directory / results / evidence: python -m pytest tests/test_services.py -k "cancel" and python -m pytest -q, both in project/. ......................................                                          [100%]
38 passed in 0.06s
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: Accepted. The "appointment not found" rule now lives in one place. All functions remain the same and all tests passed. 

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: Issues F8-01 and F8-02 / Repair only. Both issues are owned by chara3kki (charatwukki's different account [Chars])
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: 
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? Suggestion 2 was the least supported. It said book_appointment might pass the wrong practitioner ID to the conflict check, which sounded paulsible because wrong arguments are a common cause of a reversed result. Bout Copilot only said the service "appears" consistent, and it gave no evidence. When I read services.py, the call passes practitioner.practitioner_id and the booking datetime, and the prepared commit changed only data_store.py. So I rejected it was wrong. 

2. What evidence changed your group's view? When checking the copilot suggestions. Reading services.py showed service passed the correct practitioner ID, but copilot suggested that something was wrong with it. This allowed us to reject suggestion 2 with evidence. Looking back, we learned that a plausible explanation is not a diagnosis until we have seen the line of code or run the check ourselves. 

3. How did regression tests protect the refactoring? The suite was fully passing before the refactor, so any new failure would have come from the change itself. The tets check waht the code does and not how it is written, so they showed behaviour stayed the same while the structure changed. The regression tests caught my first attempt taht failed because of a mistyped attribute name, and the suite passed again once I fixed it

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?
An engineer should make observations on the failure. Document the inputs to allow people to reproduce the problem use test cases to state the expected behaviour from a requirement. An engineer must gather evidence before editing so that they can deduce what is wrong with the code. 

2. Where should expected behaviour come from during debugging?
The expected behaviour should come from the requirements as they define what the program should do. If the actual behaviour does not meet the requirements, it does not meet the expected behaviour. 

3. What is a debugging hypothesis?
A debugging hypothesis is a plausable explanation of why a failure occurs. A debugging hypothesis must be paired with a check in order to confirm whether the hypothesis is correct or wrong. 

4. What is a regression test and why is it retained?
A regression test is a test ran to ensure that the software works properly after code changes. Regression tests are retained so that later changes can be checked against previous behaviours and can't silently reintroduce a bug. 

5. What is meant by root cause?
The root cause means the main reason a failure occurs. An example of this would be a faulty implementation in the code. 

6. What is refactoring?
Refactoring means to improve the code without changing its behaviour or functionality. An example of this could be optimising code by changing its implementation. 

7. What is a swallowed exception?
A swallowed exception is when a program fails but it pretends that nothing happened and carries on [error caught and ignored]. An example of this would be using pass instead of having an error message. Doing this makes debugging a harder process as no proper output as to what went wrong is given to the developer. 

8. What is a code smell?
Code smell is a sign in the code that suggests a design problem, but the code works. An example of this would be unused variables or unclear variable names. 

9. How should GitHub Copilot-generated debugging diagnoses be treated?
All GitHub Copilot-generated debugging diagnoses should be treated as a hypotheses rather than confirmed ansswers. Each suggestion must be checked against the requirements, the actual test results and the code before it is accepted, modified or rejected with a reason. Copilot should never replace your own diagnosis by running the test. It can assume but it should never be counted as evidence. 

10. What is the Stage 8 engineering rule?
Diagnose the problem before you fix it. Observe and document the inputs that caused the failure, state the expected behaviour from the requirements, and form a hypothesis. Use evidence to find the root cause and make sure to use regression tests after code changes. 

## L. Completion and handover

- [ ] Existing project, earlier tests and stage records preserved.
- [ ] Passing Stage 7 SHA and safe preparation details recorded.
- [ ] Both defects reproduced with meaningful failing tests.
- [ ] Both human hypotheses recorded before Copilot; actual suggestions evaluated with evidence.
- [ ] Supported causes and minimal repairs explained; focused and full regression results recorded.
- [ ] One genuine refactor verified under passing before/after tests.
- [ ] Human PR review, feedback resolution and integrated retest recorded.
- [ ] Tutorial, three reflections and ten formative responses complete.
- [ ] Local recovery metadata excluded from submitted source.
- [ ] Same project and full suite ready for Stage 9 after Stage 8 integration, verification and recording.

Verified integrated code SHA / result: see I.
Submitted SHA and evidence-only difference if any: [complete]
Unresolved issues or incomplete checks / owner / next action: [complete]
Handover note: [complete]
