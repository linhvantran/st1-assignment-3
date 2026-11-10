# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: [Mon 9:30-11:30 Group 1]
Members and responsibilities: CrowdedGolf [Thomas]: Sections A and B. linhvantran [Van Tran]:the sort key (#16), select_appointments (#17) with their tests, Section C and F.

charatwukki and chara3kki [Chars]: Created test_workflows.py, Created the issues, Filled out Copilot information and suggestions, Filled out the formative questions, Created AppointmentService.list_practitioner_appointments in services.py. Filled out F and H. Created the MD file, run instructions, and scope. 

Stage 8 integrated SHA, command, working directory and actual result: 8afc0166acf3610ced7521d2ff3eacda38c3ebd8, 'python -m pytest -q in project/; ......................................                                             [100%]
38 passed in 0.11sS

## A. Tutorial activities

### A1 Session state classification

| Information | Required session/domain or transient state? | Requirement or reason |
|---|---|---|
| Patient identity | Required | A valid patient ID value is required for most of the functions to link to the correct patient. |
| Appointment history | Required | FR-07 requires history to be retained. |
| Temporary menu choice | Transient / Debug | This is only a temporary state as a user will change their menu choice. |
| Practitioner specialty | Required | This is a required part of the Practitioner element. |
| Debug print output | Transient / Debug | Print outputs with debug information are not needed for the final product and are only used for testing. |
| Appointment status | Required | Appointment status is a required part of the appointment class so we can know if an appointment is scheduled, cancelled, or completed. |

What is intentionally lost on exit? 
The program currently intentionally loses patient data apon exiting the program.

### A2 Interface and domain data plan

Plan before AI. This replaces schema/key design; no database tables are required.

| Function or component | Explicit inputs and types | Outputs | Responsibility and validation | Domain source / existing constraint |
|---|---|---|---|---|
| appointment_sort_key | Appointment: tuple | Elements arranged as specified in the key. Type: tuple | Provide a key to order appointment so datetime or ID is the first element based off what the appointments need to be sorted by. Validated by checking that an appointment put through this key retains all the same data but with datetime as the first element. | `Appointment` |
| select_appointments | appointments: list, practitioner_id: str, status: enum | The selected appointments. Type: list | Retrieve the correct appointment objects from datastore and return them as a list. Verified by checking retrieved objects against expected values from datastore. | `Appointment` |
| AppointmentService.list_practitioner_appointments | practitioner_id: str, status: enum | List of practitioners appointmetns. | Collect all appointments a specific practitioner is assigned to and return it as a list. Verified by checking that the returned list contains all appointments assigned to that practitioner. | `Practitioner` |
| Console | user_input: str, AppiontmentService: class, PractitionerService: class, and PatientService: class | Prints a TUI that displays various options the user can interact with. | Prompt, parse, call services, display results and recover from expected input errors. Validated by checking that all the function of the TUI properly call the connected functions. | `Appointment` |

Relate patient ID/name, practitioner ID/name/specialty, and appointment ID/actual participants/date_time/status to the existing contracts:
- `ID/name` releated to `Patient`
- `ID/name/specialty` related to `Practitioner`
- `appointment ID/ actual participants/date_time/status` related to `Appointment`

### A3 Responsibility violations

| Conceptual case | Violation | Correct boundary and reason |
|---|---|---|
| Appointment.cancel reads input | `appointment.cancel()` should only be cancelling the appointment. A confirmation should not be within the cancel function itself. | `appointment.cancel()` instantly cancels the appointment when called. The confirmation message is moved to happen within another function (likely in console) before the code actually runs the cancel function. |
| Service prints/reads the menu | The `AppointmentService` class is only responsible for appointment data. It should not be printing a console menu or reading a console command as those tasks are for `console.py` | The console calls `AppointmentService` to provide the appointment data to the console so it can print the relevant menu with it. The console will also call the `AppointmentService` if the command read requires AppointmentService to be called. |
| Query sorts its source in place | `select_appointments` should only be selecting some appointments and returning a list of those selected appointments. It should not be calling a sort function. | `select_appointment` retrieves specific appointments with the appointments list retrieved being used in a separate sort function. |
| Store prints Appointment saved | The datastore itself should return the saved appointment object itself. It should not just return ‘Appointment saved’ | The datastore returns the appointment object and another function (potentially within console) prints ‘Appointment Saved’ to the UI when a appointment is saved correctly. |

### A4 Sorting comparison

For `appointments.sort(key=appointment_sort_key)` and `result = sorted(appointments, key=appointment_sort_key)`, predict source order, return value and result identity. Give a meaningful mutation check:
The first bit of code will change the source order as it is modifying the original list while the second code will not because it creates a new list. The first will not return anything but the original list would have been modified per the sorting key. The second line of code will return the sorted list as a new list “result” while retaining the original “appointments” list. Assertion: Check that the values within an element parsed through one of these key functions matches are the same as the original element but in a different order.

Score-example prediction and explanation of passing the named key:
- From previous knowledge of python, the predictions are likely accurate as `thing1.function` modifies thing1 while `thing2 = thing1()` creates a copy where the opperation is saved.
- Passing the named key in the key argument will use that key as the template for how the program should sort the list.

### A5 Exit question

Explain cancellation versus deletion, and checks for same-session lookup, all-status listing and SCHEDULED-only exclusion:
- A cancellation changes a retained appointment's status rather than removing the appointment because FR-07 requires history to be retained. So, the appointment status is changed to CANCELLED instead of deleting the entry so that the deleted appointment data is still accessible. 
- To ensure this requirement is fulfilled throughout our program, there are multiple tests in place that test to make sure cancelled appointments are retained using the CANCELLED status rather than being deleted. Most of the checks cancel an appointment and check if it is still acessible from the datastore or through the service.
- Having this different CANCELLED status allows us to have a SCHEDULED-only list that omits cancelled objects without deleting the cancelled object. This SCHEDULED-only list should omit the CANCELLED objects because if you are trying to view a timetable of upcoming appointments you only need to worry about the appointments that are currently scheduled.

## B. Human design and contracts

Complete before GitHub Copilot. Record any interface/integrity decision and its reasoning: <!-- response -->

| Requirement | Input / session data | Operation and responsible component | Expected result or error | Test / evidence |
|---|---|---|---|---|
| QRY-01 | Sample appointments assigned to various practitioners and a single desired practitioner ID for testing | Operation: `AppointmentService.list_practitioner_appointments()` in `services.py` Respoinsible component: `select_appointments()` in `queries.py` | Only the required practitioner's appointments are shown. | Test a list of multiple appointments through `select_appointment()` and ensure that the appointments for the tested practitioner are the only appointments being returned. |
| QRY-02 | Sample appointments with varying statuses. | Operation: [complete] Responsible component: `select_appointments()` in `queries.py` | By default, collects all statuses each with a explicit enum. If the enum does not match a known status, produce an empty result. | Check that all possible status of appointments are collected and produce an empty result for an unknown enum. |
| QRY-03 | Sample appointments with some having the same time but different appointment ID. | Operation: `appointment_sort_key()` Respoinsible component: `console.py` | Appointments ordered by date/time with same-time appointments being "tie broken" by their appointment ID without changing the source fields. | Check appointments in datastore has not been modified, appointments are ordered by time, and same-time appointments are ordered by ID (accending). |
| FP-01 | User's console inputs. | Operation: [complete] Responsible component: `console.py` | Unchanged inputs are repeated, codes is inspected for hidden state, input, output, and side effects. | Ensure that user's inputs execute the required functions. |
| FP-02 | Sample appointments and previously sorted lists | Operation: [complete] Responsible component: `console.py` | A destinct returned list for empty, already-sorted, and unsorted inputs. The contained objects remain unchanged. | [complete] |
| FP-03 | Sample appointments with various times. | Operation: [complete] Responsible component: `appointment_sort_key()` in `queries.py` | Sorting uses named key. | Test the key and test that sorting actually uses the key. |

Cover QRY-01–04, FP-01–03, UI-01–02 and relevant FR-01–09. Explain empty versus unknown versus invalid, enum conversion, actual object identity, error handling and unchanged state on rejection: 
- Empty means that the there is no value for that element within the object, unknown means that the value is not defined, and invalid means that the value is wrong for that element e.g. completed status on a cancelled appointment.
- Enum convention describes the standard ways enums are created and formatted. The enum class like other classes is in Pascel Case (TestName) and the enums themselves are in Upper Snake Case (TEST_NAME).
- The Actual Object Identity is the memory address where the object is stored. For a given object, this is fixed and will not change within the lifespan of the program.
- Error handling is how a program recovers from somthing going instead of completely crashing. This allows a known error to be made into a more human readable format to display to the user to give them feedback on what they did that causes an error. E.g. entering a string into a field that only excepts integers will crash the program if error handing was not used but with error handling this error would be expected to happen and we can then display a message to the user asking them to only enter integers with a box to try again.
- An objects state reamins unchanged on rejection by a query as the queries job is to lookup objects not modify their contents. The query should just ignore the rejected object and move on with pulling other objects.

## C. Implementation and query verification

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link                                                                                           |
|---|---|---|---|---------------------------------------------------------------------------------------------------------|
| QRY-03, FP-03 / Q-01 | `project/smartcare/queries.py::appointment_sort_key`; `project/tests/test_queries.py::test_sort_key_returns_date_time_and_appointment_id` | The key returns the date/time and appointment ID for one appointment: `key == (NINE_AM, 'A1')` | Passed. `python -m pytest` from `project/`: 42 passed (38 existing + 4 new) | (https://github.com/linhvantran/st1-assignment-3/pull/20) SHA: 3b968e201f8abe83232736a5954f6941a49a426a |
| QRY-03 / Q-02 | `project/smartcare/queries.py::appointment_sort_key`; `project/tests/test_queries.py::test_equal_time_appointments_sort_by_appointment_id` | Two appointments at the same time, A2 created before A1, sort as `[a1, a2]`, so the ID breaks the tie | Passed (same run as Q-01) | (https://github.com/linhvantran/st1-assignment-3/pull/20) SHA: 3b968e201f8abe83232736a5954f6941a49a426a                                                                  |
| FP-03 / Q-03 | `project/smartcare/queries.py::appointment_sort_key`; `project/tests/test_queries.py::test_sort_key_orders_by_time_before_id` | The earlier appointment has the larger ID. `sorted(..., key=appointment_sort_key)` puts it first, so the test fails if the key used ID before time | Passed (same run as Q-01) | (https://github.com/linhvantran/st1-assignment-3/pull/20) SHA: 3b968e201f8abe83232736a5954f6941a49a426a                                                                  |
| FP-03 / Q-04 | `project/smartcare/queries.py::appointment_sort_key`; `project/tests/test_queries.py::test_sort_key_does_not_change_the_appointment` | After the call, the appointment's ID, date/time and status are unchanged, and `patient` and `practitioner` are the same objects (`is`) | Passed (same run as Q-01) | (https://github.com/linhvantran/st1-assignment-3/pull/20) SHA: 3b968e201f8abe83232736a5954f6941a49a426a                                                                  |
| QRY-01 / Q-05 | `project/smartcare/queries.py::select_appointments`; `project/tests/test_queries.py::test_select_returns_only_requested_practitioner` | Only practitioner D1's appointment is returned when a D2 appointment is in the source list as a control: `result == [mine]` | Passed. `python -m pytest` from `project/`: 50 passed (38 existing + 12 in test_queries.py) | (https://github.com/linhvantran/st1-assignment-3/pull/23) SHA: 93fb8af777674bfd913352baf7d5fddf6d845e6d |
| QRY-02 / Q-06 | `project/smartcare/queries.py::select_appointments`; `project/tests/test_queries.py::test_select_without_status_returns_every_status` | With no status, SCHEDULED, CANCELLED and COMPLETED appointments are all returned in date/time order: `result == [scheduled, cancelled, completed]` | Passed (same run as Q-05) | (https://github.com/linhvantran/st1-assignment-3/pull/23) SHA: 93fb8af777674bfd913352baf7d5fddf6d845e6d |
| QRY-02 / Q-07 | `project/smartcare/queries.py::select_appointments`; `project/tests/test_queries.py::test_select_with_status_returns_only_that_status` | An explicit `CANCELLED` returns only the cancelled appointment and an explicit `SCHEDULED` returns only the scheduled one, so cancelled history is kept but can be excluded | Passed (same run as Q-05) | (https://github.com/linhvantran/st1-assignment-3/pull/23) SHA: 93fb8af777674bfd913352baf7d5fddf6d845e6d |
| QRY-01, QRY-02 / Q-08 | `project/smartcare/queries.py::select_appointments`; `project/tests/test_queries.py::test_select_returns_empty_list_when_nothing_matches` | An unregistered practitioner ID, and a status with no matches, each return `[]` and no error | Passed (same run as Q-05) | (https://github.com/linhvantran/st1-assignment-3/pull/23) SHA: 93fb8af777674bfd913352baf7d5fddf6d845e6d |
| QRY-03 / Q-09 | `project/smartcare/queries.py::select_appointments`; `project/tests/test_queries.py::test_select_orders_equal_time_appointments_by_id` | Two appointments at the same time, A2 listed first, come back as `[a1, a2]`, so the named key breaks the tie through the query | Passed (same run as Q-05) | (https://github.com/linhvantran/st1-assignment-3/pull/23) SHA: 93fb8af777674bfd913352baf7d5fddf6d845e6d |
| FP-02 / Q-10 | `project/smartcare/queries.py::select_appointments`; `project/tests/test_queries.py::test_select_returns_new_list_and_leaves_source_unchanged` | The result is a different list from the source (`is not`), the source order is unchanged, the result holds the same objects (`is`), and the appointment fields are unchanged | Passed (same run as Q-05) | (https://github.com/linhvantran/st1-assignment-3/pull/23) SHA: 93fb8af777674bfd913352baf7d5fddf6d845e6d |
| FP-01 / Q-11 | `project/smartcare/queries.py::select_appointments`; `project/tests/test_queries.py::test_select_repeated_calls_give_same_result` | Two calls with the same inputs return equal lists, and they are separate list objects | Passed (same run as Q-05) | (https://github.com/linhvantran/st1-assignment-3/pull/23) SHA: 93fb8af777674bfd913352baf7d5fddf6d845e6d |
| FP-02 / Q-12 | `project/smartcare/queries.py::select_appointments`; `project/tests/test_queries.py::test_select_returns_fresh_list_for_empty_sorted_and_unsorted_input` | An empty, an already-sorted and an unsorted source each give a fresh list equal to the sorted source | Passed (same run as Q-05) | (https://github.com/linhvantran/st1-assignment-3/pull/23) SHA: 93fb8af777674bfd913352baf7d5fddf6d845e6d |

Rows for list_practitioner_appointments (#18) are added once that code is written and tested. They need: known-empty, unknown and invalid service cases, practitioner and status validation, fresh list from the store, the exact stored objects, and retained cancelled history.

Replace the purity explanation with:

Purity explanation from code inspection, including absence of hidden state and I/O: appointment_sort_key reads appointment.date_time and appointment.appointment_id and returns a new tuple. select_appointments takes the list, the practitioner ID and the status as arguments, builds a new list with a comprehension, and returns sorted(...) of that new list using the named key. Neither function assigns to its inputs, uses module-level or global state, calls print or input, calls a service, or touches a data store, so the same arguments always give an equal result. sorted returns a new list, unlike list.sort, so the source list is never reordered, and the result holds references to the same Appointment objects, so nothing is copied.

Replace "What the tests do and do not establish" with:

What the tests do and do not establish: The twelve tests show that the key has the right shape and values, that equal-time appointments are ordered by ID, that practitioners and statuses are filtered correctly, that no status returns every status including CANCELLED, that no match gives an empty list, that a fresh list is returned for empty, sorted and unsorted inputs, that the source order and fields are unchanged, and that repeated calls give the same result. They do not prove purity by themselves, because a test cannot show the absence of printing or hidden state, so that comes from reading the code. They also do not test validation, because select_appointments assumes valid inputs: an unknown practitioner or a non-enum status such as 'scheduled' would just return an empty list, and rejecting them with LookupError or ValueError is the service's job in #18.

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow |Get-Content ..\stage09\UI01_inputs.txt | python -u main.py --interactive 2>&1 | Tee-Object -FilePath ..\stage09\UI01_outputs.txt | Register/find P1, D1, D2, book A1, reject conflict, book A2 with D2, cancel, find, list, book freed slot, exit.  | Verified registrations and lookups correct. A1 booked. A-CONFLICT rejected and flind A-CONFLICT gave "Appointment not found (not stored)> A2 booked for D2 at the same time. Not run: stopped at the first listing, so cancel, retrieval, filters, freed slot and exit were not reached.  | UI01_inputs.txt and UI01_outputs.txt |
| UI-02 invalid-input recovery | Get-Content ..\stage09\UI02_inputs.txt | python -u main.py --interactive 2>&1 | Tee-Object -FilePath ..\stage09\UI02_outputs.txt | Each rejection prints a message and returns to the menu. Leaves state unchanged, and successful action follows. | Verified all rejections gave a message with no traceback. P1 still Alex Example. A9 and A8 "Appointment not found" after failed bookings. A1 unchanged after the duplicate booking. A1 still cancelled after repeated cancellation. | UI02_inputs.txt and UI02_outputs.txt |
| Automated service workflow | cd project, then python -m pytest -q tests/test_workflows.py, then python -m pytest -q | Rejections leave state unchanged. Different practitioner allowed, cancellation retained, filters work, and freed slot bookable. | 8 passed in 0.55s. Passing: conflict rejection, duplicate ID/unkonwn participants ID (ID not reserved), different-practitioner booking, cancellation keeps the same object findable, repeated/unknown cancellation, freed slot. State is checked with before/after snapshot() comparisons.| tests/test_workflows.py |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: b14a02aa80d34ed27bd5e4ae9a71cbc22dd9081e. This is the SHA before I used AI. 
Actual prompt/context supplied: https://github.com/copilot/share/ca094108-0aa4-82d4-9900-264aa083409a
Actual response: https://github.com/copilot/share/ca094108-0aa4-82d4-9900-264aa083409a

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| Listing test books A1 and A2 for D1 at EIGHT_AM while A2 is still SCHEDULED, causing a same-practitioner conflict | test_practitioner_appointment_listing_filters_orders_and_isolates_results in tests/test_workflows.py | Important | Modify: Cancel A2 before booking A1 so the equal time fixture does not break the conflict rule.  | Reordered the setup. | Test now books all five appointments and fails only at NotImplementError |

| snapshot() uses list_patients() and list_practitioners(). | snapshot() helper in tests/test_workflows.py | Optional | Accept: Both methods exist in the store. | No change. | 8 passed in 0.55s | 

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: Appointment owns its domain rules, including guarded cancellation (a repeated cacnel was rejected with "Only SCHEDULED appointments may be cancelled" and the record stayed cancelled). SmartCareDataStore only holds the in-memory collections and looks up registered patients, practitioners and appointments. The services coordinate registraction, booking, conflict checks, cancellation and validated listing, and they call the queries. queries.py selects the sorts the lists it is given using the named key; it has no input/output, global store, services call or mutation. Console.py only prompts, parses, calls the services, prints, and catches ValueError and LookupError, so no domain rules are duplicated there. In the console runs, rejected requests returned to the menu and the stored records were unchanged. In tests/test_workflows.py, before/after snapshot comparisons passed for conflict, duplicate ID, unknown participant and repeated cancellation cases. 



## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? Deciding where each responsibility lives. The pure querly only selects and sorts what it is given, while the service validates the practitioner. The console only parses input and displays results, and it creates one store and one set of services for the whole session, so data persists between menu choices. Getting that wiring right mattered more than the filtering or sorting itself. 
2. Which Copilot suggestion did you reject as over-engineering, and why? Both findings in E were accepted or modified, and neither was over-engineering. The 
3. How did you prove cancelled appointments remain retrievable and listable in the same session? test_cancellation_keeps_the_same_appointment_findable cancels an appointment and checks it is still found with CANCELLED status. The listing test cancels A2, then lists D1 with the default status and confirms the cancelled appointment is still included. A SCHEDULED only list leaves it out, and all 8 workflow tests passed. 

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? It only uses what you pass in (that being the appointmetns, practitioner ID and status) and gives back a new list, with no hidden state or I/O. Sorting the original list in place, printing, or reaching into a global store would break that. 
2. Which explicit inputs are needed, and why avoid a global store? The appointmentslist, the practitioner ID and the status filter. A global store means the result depends on a hidden state, so the same arguments could give different results and it's much harder to test with small synthetic data. 
3. How can a new list reuse Appointment objects safely? The new list can just hold references to the same Appointment objects with no copying needed. That's fine as long as the query only reads them and never modifies them. Changing the new list doesn't touch the source list either. 
4. Why use a named key, and what breaks equal-time ties? A named key gives one reusable rule you can test directly. If two appointments share a date/time, the appointment ID breaks the tie, so the key is (date_time, appointment_id)
5. How do default and explicit status filters differ? No status (None) returns every status, including CANCELLED and COMPLETED, so history stays visible. An explicit AppointmentStatus returns only that status. The console converts the typed tesxt to the enum, while direct callers must pass the enum or None. 
6. How do empty, unknown practitioner and invalid filter cases differ? A known practitioner wiht no matches gets an empty list and no error. An unregistered practitioner ID raises LookupError, and a blank or invalid ID raises ValueError. a non enum status like the string 'scheduled' also raises ValueError, because it's bad input and not "not matches". 
7. Which console errors recover, and how is unchanged state checked? Expected ValueError and LookupError cases, like an unknown menu choice, bad or duplicate IDs, a malformed date, an invalid status or a repeated cancellation. The console shows a message and returns to the menu, without catching and ignoring every Exception. To check state, look up or list the records before and after the failure and confirm the next action still works. 
8. What is data integrity for registered participants, conflicts and history? Appointment only link to real registered patients and practitioenrs, same practitioenr SCHEDULED conflicts get rejected, and cancelled appointments stay in the store. A rejected action leaves the data unchanged. 
9. What is Copilot's review role, and who verifies findings? It suggests things to check, but its findings are only hypotheses. The team verifies each one against the code, requirements and tests, then accepts, modifies or rejects it, and another member does the human review. 
10. How do pure functions and OOP responsibilities work together? The pure queries select and sort what they're given. Appointment owns cancellation, the store holds the collections and the services coordinate and validate. The console only handles input and output and calls the services, so the domain rules stay out of it. 

## H. Review, completion and common handover

Issues and bounded branches: UI-01 and UI02: run_menu in console.py [https://github.com/linhvantran/st1-assignment-3/issues/19], QRY-04: AppointmentService.list_practitioner_appointments in services.py [https://github.com/linhvantran/st1-assignment-3/issues/18], QRY-01, QRY-02, QRY-02, FP-01, FP-02: select_appointments in queries.py [https://github.com/linhvantran/st1-assignment-3/issues/17], QRY-03, FP-03: appointment_sort_key in queries.py [https://github.com/linhvantran/st1-assignment-3/issues/16]. https://github.com/linhvantran/st1-assignment-3/tree/feature/16-sort-key, https://github.com/linhvantran/st1-assignment-3/tree/feature/17-select-appointments
PR/diff and another-member human reviewer: Merge Stage09 to main https://github.com/linhvantran/st1-assignment-3/pull/22 [reviewed by charatwukki] 
Review responses and Copilot comparison: This was merged after all of the tests passed so there was nothing to respond to. Copilot assisted in checking over the code and raised suggestions. There is nothing to compare as copilot and I came to the same conclusions, and there were no errors in the code. 
Integrated common Stage 9 SHA: 9690e687ba3dec28ce1b0fdd925445ebe5a7ebc1 [SHA after merge into main] 
Full regression command, working directory, actual count/result and evidence: python -m pytest -q in project/ on 9690e687ba3dec28ce1b0fdd925445ebe5a7ebc1, ..........................................................                         [100%]
58 passed in 0.11s [this is the evidence and actual count/result]
README run instructions and scope/limitations: https://github.com/linhvantran/st1-assignment-3/blob/main/README.md [this is the group introductions but that is also where i added the instructions]
Unresolved issues and support/action: None 
UG common candidate / PG future branch plan: 9690e687ba3dec28ce1b0fdd925445ebe5a7ebc1 

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
