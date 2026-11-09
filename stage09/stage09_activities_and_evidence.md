# Stage 9 activities and evidence

Common UG and PG record. All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage09/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Use the Stage 9 handout and Overview/revision 2 baseline. Keep responses concise and link accessible artefacts; do not paste entire logs or private peer ratings.

Group: <!-- complete -->
Members and responsibilities: <!-- complete -->
Stage 8 integrated SHA, command, working directory and actual result: <!-- complete -->

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
| appointment_sort_key | Appointment: tuple | Elements arranged as specified in the key. Type: tuple | Provide a key to order appointment so datetime or ID is the first element based off what the appointments need to be sorted by. Validated by checking that an appointment put through this key retains all the same data but with datetime as the first element. | [complete] |
| select_appointments | appointments: list, practitioner_id: str, status: enum | The selected appointments. Type: list | Retrieve the correct appointment objects from datastore and return them as a list. Verified by checking retrieved objects against expected values from datastore. | [complete] |
| AppointmentService.list_practitioner_appointments | practitioner_id: str, status: enum | List of practitioners appointmetns. | Collect all appointments a specific practitioner is assigned to and return it as a list. Verified by checking that the returned list contains all appointments assigned to that practitioner. | [complete] |
| Console | user_input: str, AppiontmentService: class, PractitionerService: class, and PatientService: class | Prints a TUI that displays various options the user can interact with. | Prompt, parse, call services, display results and recover from expected input errors. Validated by checking that all the function of the TUI properly call the connected functions. | [complete] |

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

| Requirement / test ID | Code location | Case and meaningful assertion | Actual result | Evidence link |
|---|---|---|---|---|
| | | | | |

Include practitioner isolation, every enum status/default all, equal-time ID tie-break, named-key reuse, repeated calls, empty/already-sorted fresh lists, unchanged source order/fields, known-empty/unknown/invalid service cases and retained history.

Purity explanation from code inspection, including absence of hidden state and I/O: <!-- response -->
What the tests do and do not establish: <!-- response -->

## D. Integrated console and workflow evidence

| Scenario / acceptance ID | Reproducible inputs / artefact | Expected result | Observed result and state check | Evidence link |
|---|---|---|---|---|
| UI-01 full menu workflow | | | | |
| UI-02 invalid-input recovery | | | | |
| Automated service workflow | | | | |

Include registration/find, booking, conflict rejection, different-practitioner booking, cancellation, retrieval, listing/filtering, freed slot and exit; duplicate/unknown/blank IDs, malformed/impossible date, invalid status, unknown choice and repeated cancellation. Identify before/after state and subsequent successful action.

## E. GitHub Copilot review and human decisions

Human design completed before AI: <!-- reference -->
Actual prompt/context supplied: <!-- paste or accessible reference -->
Actual response: <!-- accessible reference -->

| AI finding | Code/test evidence | Severity | Accept/Modify/Reject and reason | Change or no change | Actual verification |
|---|---|---|---|---|---|
| | | | | | |

Responsibility check: explain how domain invariants, shared-store collections, service coordination, pure queries and console effects remain separate: <!-- response -->

## F. Required reflections

1. Which integration concern was architectural rather than a filtering/sorting detail? <!-- response -->
2. Which Copilot suggestion did you reject as over-engineering, and why? <!-- response -->
3. How did you prove cancelled appointments remain retrievable and listable in the same session? <!-- response -->

## G. Ten formative answers

1. What makes select_appointments pure, and what side effect breaks purity? <!-- response -->
2. Which explicit inputs are needed, and why avoid a global store? <!-- response -->
3. How can a new list reuse Appointment objects safely? <!-- response -->
4. Why use a named key, and what breaks equal-time ties? <!-- response -->
5. How do default and explicit status filters differ? <!-- response -->
6. How do empty, unknown practitioner and invalid filter cases differ? <!-- response -->
7. Which console errors recover, and how is unchanged state checked? <!-- response -->
8. What is data integrity for registered participants, conflicts and history? <!-- response -->
9. What is Copilot's review role, and who verifies findings? <!-- response -->
10. How do pure functions and OOP responsibilities work together? <!-- response -->

## H. Review, completion and common handover

Issues and bounded branches: <!-- links -->
PR/diff and another-member human reviewer: <!-- actual links/name -->
Review responses and Copilot comparison: <!-- links -->
Integrated common Stage 9 SHA: <!-- complete -->
Full regression command, working directory, actual count/result and evidence: <!-- complete -->
README run instructions and scope/limitations: <!-- link -->
Unresolved issues and support/action: <!-- complete -->
UG common candidate / PG future branch plan: <!-- complete -->

- [ ] Query contracts, purity, new lists and named-key ordering verified.
- [ ] Service empty/unknown/invalid cases and cancellation history verified.
- [ ] Every console command and invalid-input recovery demonstrated.
- [ ] Query and workflow tests plus all previous tests pass; actual evidence linked.
- [ ] Human design, Copilot critique, review and integration recorded honestly.
- [ ] Reflections and ten formative responses completed.
- [ ] README updated; earlier code/tests/records preserved.
- [ ] Common SHA protected for UG Stage 12; PG Stage 10/11 work deferred until approved.

No persistence, rescheduling or assurance implementation is part of Stage 9. UG: 6→7→8→9→12. PG: 6→7→8→9→10→11→12. Mixed groups keep one repository and protect the common candidate.
