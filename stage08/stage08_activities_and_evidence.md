# Stage 8 activities and evidence

UG and PG | One evolving group project | Complete this blank record using the Stage 8 handout.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage08/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. The Stage 8 preparation utility is supplied or run by teaching staff when Stage 8 begins. Follow your tutor’s controlled workflow and the handout. If temporarily supplied, keep it outside the repository in a sibling Stage_8_Assets/ folder; exclude it from Git and the final submission.

Group/tutorial: [Mon 9:30-11:30 Group 1]
Members and UG/PG cohorts: [Van Tran (@linhvantran), Xi Chen (@cz1295768-ui), Chars (@charatwukki), Thomas Pollock (@CrowdedGolf)]
Record owner / contribution links for each member: [complete]

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

- Stage 7 code SHA and requirement baseline: [complete]
- Baseline test command / working directory / observed result / evidence: [complete]
- Clean preparation SHA if a record-only commit followed Stage 7: [complete]
- Branch and preparer / how teammates obtained this branch: [complete]
- Downloaded tool version, source SHA256 and --check outcome: [complete]
- --apply and --verify output summaries / artefact references: [complete]
- Bounded diff inspected and recovery location (not committed): [complete]
- Prepared faulty-state commit SHA: [complete]
- Preparation or recovery issues and resolution, if any: [complete]
- Initial prepared full-suite command / result / key failures: [complete]

## C. F8-01 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-01.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## D. F8-02 diagnosis and repair

- Symptom / observed behaviour: [complete]
- Expected behaviour and requirement: [complete]
- Minimal synthetic reproduction steps: [complete]
- Meaningful failing test path/name and exact relevant failure: [complete]
- Human hypothesis and intended checks: see E, F8-02.
- Supported root cause and inspected code/runtime evidence: [complete after diagnosis]
- Smallest justified fix / diff / why other behaviour is preserved: [complete]
- Repair SHA / focused verification result: [complete]

## E. Human-first hypotheses

Complete both entries BEFORE Copilot. C/D supply observed/expected/reproduction/test; retain those initial facts and link them here.

### F8-01 human entry
Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

### F8-02 human entry
Likely cause and why plausible: [complete]
Evidence intended to inspect / competing explanation / discriminating check: [complete]
Member and saved sequence/time or commit showing this preceded consultation: [complete]

## F. GitHub Copilot prompts, findings and human decisions

Use the full handout prompt separately for BOTH defects, after E. Keep each actual prompt or accessible reference; include observed behaviour, expected behaviour, reproduction, failing test, human hypothesis, relevant code, three ranked causes and discriminating checks, with the no-rewrite/no-invented-requirements constraints.

### F8-01 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

### F8-02 Copilot review
Actual prompt / output reference and member: [complete]
1. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
2. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
3. Ranked suggestion / evidence check / observed evidence / correct, partly correct or wrong / accept, modify or reject with reason: [complete]
Final human conclusion and comparison with initial hypothesis: [complete]

## G. Failing to passing regression evidence

| Checkpoint | Code SHA or precise diff | Command and working directory | Actual result and artefact reference |
|---|---|---|---|
| F8-01 before repair | [complete] | [complete] | [complete] |
| F8-01 after repair | [complete] | [complete] | [complete] |
| F8-02 before repair | [complete] | [complete] | [complete] |
| F8-02 after repair | [complete] | [complete] | [complete] |
| Full suite after both repairs, before refactor | [complete] | [complete] | [complete] |

Explain how the assertions detect each relevant incorrect result and protect previous behaviour: [complete]
Unrelated failures investigated / resolution: [complete or not applicable with reason]

## H. Refactoring decision and before/after verification

Smell and exact location: [complete]
Small proposed structural change / why justified: [complete before editing]
External behaviour to preserve / relevant tests: [complete]
Before result: see G, full passing suite.
Actual change / diff / separate refactor SHA: [complete]
Focused and full after-refactor commands / working directory / results / evidence: [complete]
Result — accepted, revised or rejected / reason / behaviour-preservation conclusion: [complete]

## I. Git, human review and integration

Issues for both defects / refactor scope and owners: [complete]
Branch / prepared, repair and refactor checkpoints: [link B/C/D/H]
PR link and another member's reviewer identity: [complete]
Key human feedback, difference from Copilot findings and response/outcome: [complete]
Actual review approval / merge evidence: [complete]
Integrated code SHA and team pull/retest command / working directory / result: [complete]
Evidence-only later SHA / explanation if different: [complete or not applicable]
Each member's substantive contribution and artefact: [complete]

## J. Required reflections

1. Which Copilot diagnosis appeared convincing but lacked evidence? [complete; report honestly if none and discuss the least-supported real suggestion]
2. What evidence changed your group's view? [complete]
3. How did regression tests protect the refactoring? [complete]

## K. Ten formative questions

1. What should an engineer do before changing code in response to a failure?

Response: [complete]

2. Where should expected behaviour come from during debugging?

Response: [complete]

3. What is a debugging hypothesis?

Response: [complete]

4. What is a regression test and why is it retained?

Response: [complete]

5. What is meant by root cause?

Response: [complete]

6. What is refactoring?

Response: [complete]

7. What is a swallowed exception?

Response: [complete]

8. What is a code smell?

Response: [complete]

9. How should GitHub Copilot-generated debugging diagnoses be treated?

Response: [complete]

10. What is the Stage 8 engineering rule?

Response: [complete]

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
