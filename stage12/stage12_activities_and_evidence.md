# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: 9:30-11:30 Monday Group 1
Members and UG/PG applicability: 
CrowdedGolf [Thomas]: Sections B, G, and AI relection in E. linhvantran[Van]: Section D, H and K
charatwukki and chara3kki [Chars]: Sections C, E, and M. 


## A Release scope and starting SHA

Release label/version and requirements baseline: v1.0. Requirements baseline: FR-01 to FR-09, QRY-01 to QRY-04, FP-01 to FP-03
Common starting SHA / branch / applicable members: 9690e687ba3dec28ce1b0fdd925445ebe5a7ebc1 was found to be based on an outdated commit. Main was merged in to update it, therefore the common starting SHA is 8715fa689410af2b8d80b3612a63b5fcb76e81b0 / debug/Stage12 / Chars, Thomas, Van, Leo 
PG starting SHA / branch / applicable members or not applicable: NOT APPLICABLE. NO POSTGRADS. 
Working-state review and approved integration: git status --short, git diff and git diff --cached at the starting SHA. All three returned no output, so there were no staged or untracked local changes. Nothing was discaded. No new work was integrated other than the previous 6 - 9 stages.  
Protected common candidate and PG differences: The common candidate is the starting SHA 9690e687ba3dec28ce1b0fdd925445ebe5a7ebc1. There are no PG differences because there are no PG's
Feature freeze / owner / verifier: 


## B Requirements and release readiness matrix

Tutorial activity 1: All tests pass, README setup is incomplete, one dependency is unreviewed and a known limitation is undocumented. Decide Release / Release with conditions / Do not release and justify: 
- Do not release. There are parts of the program that are unreviewed and there is an undocumented knowen limitation. Ignoring these issue can lead to the program having problems and users running into knowen limitations that should have been documented.

Tutorial activity 2 and actual readiness matrix. Add exact requirement/acceptance IDs, evidence and reviewer; distinguish common/PG applicability.

| Release claim / requirement / scope | Evidence | Location/link and SHA | Reviewer | Sufficient? | Gap/action |
|---|---|---|---|---|---|
| Cancellation history works | pytests that check for retained history post cancellation pass. | tests starting on lines 125, 135 in `test_services.py` pass | CrowdedGolf | Yes, all testing cases confirm that the cancelled appointment is retained. | None |
| Architecture responsibilities are appropriate | Each part of the architecture plays a key and destinct role. For example, `console.py` calls the service functions inside `services.py` which then pull data in and out of the datastore through `data_store.py` as required. | function starting line 142 in `console.py` calls a service once the input handling is done. | CrowdedGolf | Yes, each section of the code architecture plays a distinct role wihtout any responsiblity overlap. | None |
| AI use is responsible — common recheck / PG assurance | AI only used in the sections specified and in complience with the guidelines. | Section H stage 6, Section H stage 7, Section F stage 8, and Section E: stage 9 | CrowdedGolf | All evidence recorded within these md files supports that AI was used appropriately. | None |
| System is maintainable | The system follows object oriented principles with logical function names and responsibilities. | `test_services.py`, `console.py` | CrowdedGolf | Yes, our following these principles makes it easier to maintain. But there are not many code comments. | Lack of code comments. Improve documentation with a futre revision. |
| FR-01–03 register/find and validation | Tests for finding and registering both patients and practitioners pass. | tests starting on lines 30, 37, 47, 53, and 63 in `test_services.py` pass | CrowdedGolf | Yes, the tests confirm that patient and practitioner data can successfully be created and looked up. | None |
| FR-04–05 booking/conflict rules | relevant pytests pass to show that valid bookings are successfully created and creating a booking for the same practitioner and time as an existing SCHEDULED booking is cancelled. | tests starting on lines 71, 83, 94 and 104 in `test_services.py` pass | CrowdedGolf | Yes, these tests have been designed to test for possible failures to prove that the appointment booking functions are working as intended if it passes. | None |
| FR-06–08 cancellation/history/find | relevant pytests pass to show that only scheduled appointments can be cancelled and the same appointment object with CANCELLED status is retained in history. | Tests starting on lines 125 and 135 in `test_services.py` pass | CrowdedGolf | Yes, these tests have checked the program to make sure that CANCELLED appointments are retained in the datastore with the CANCELLED status | None |
| FR-09 and QRY/FP listing/filter/order/purity | Relevant pytests pass to show that the required practitioners appointments are returned, results are sorted using the working key, and query, filter, and ordering guidelines are followed. | tests in `test_queries.py` pass. | CrowdedGolf | Yes, the tests have passed. The tests have been formulated to check and make sure that all aspects of the queries are functioning as expected | None |
| UI full console sequence and error recovery | Testing of various usecases in the console does not produce any unexpected behaviour. | `console.py` | CrowdedGolf | Yes, no issues were found in testing of the console. | None |

Tutorial Activity 3: Practice answering these questions using your own artefacts:
- Why use one shared SmartCareDataStore with services and pure queries?
  - It is a good idea to use one shared datastore because it reduces the likelyhood of data mutations and outdated data existing due to data moving between multiple datastores. The central datastore also reduces the dificulty of running two subsquent functions from sections of the code. If there were two datastores, before the second part could execute it would have to pull the updated data from one database into the other while having one database means it can execute off the same database directly after the other has finnished writing.
- Show a test establishing that a cancelled appointment remains retrievable.
  - Tests starting on line 135 in `test_services.py`. This test creates a valid appointment and saves the object as a variable appointment. Then the appointment is cancelled and the test asserts that the data from the old appointment object previously saved in the appointment variable is the same object returned from `appointments.find_appointment()`. it also checks that the same pre-cancellation appointment object is in `store.list_appointments()` and that the status of the post-cancellation appointment is `AppointmentStatus.CANCELLED`.
- What AI-generated change did you reject or modify, and why?
  - In stage08 the last two suggestions by the AI were rejected. They were rejected as they were possible explinations that the AI could "think" of as to why there were errors which after inspection, were not the cause. Inspecting the code itself for any obvious logical errors and inspecting/running tests helped prove that these last two suggestions were not the cause.
- What is one unresolved limitation?
  - Lack of presistance. In a real world scenario, there would need to be some sought of propper storage solution as even highly reliable and redundant servers will need to be restarted at some point which would cause data loss since everything in this program is stored in memory.
- What would break if session-state lookup or query responsibilities changed?
  - If responsibilities changed, we could end up with sections of the architecture not communicating with each other in the way expected resulting in errors or communication not being able to make it to all the required functions. 

Tutorial Activity 4:
- See section N.

## C Full regression results

| Suite/scope | Environment/version | Working directory and command | Tested SHA | Actual result | Evidence link |
|---|---|---|---|---|---|
| Complete common | Python 3.14.5, pytest 8.3.5, Windows | st1-assignment-3\project; python -m pytest -q | 8715fa689410af2b8d80b3612a63b5fcb76e81b0 | 58 passed in 0.11s | https://github.com/linhvantran/st1-assignment-3/blob/c20613154832194a475990804f25325f6df754b6/stage12/c_regression_log.txt |
| Complete PG if applicable | Not Applicable | Not Applicable | Not Applicable | Not Applicable | Not Applicable |
| Affected focused checks after correction | Same things as above | Not run separately. The full suite was run on the updated commit (next row) | 5143ef49f3f0a372184110040a5fb59db2cca35e [This is updated from E. It contains the updated Stage 9 material and adjusted changes found in E] | Full run: 58 passed | Just check the full integrated recheck for evidence |
| Full integrated recheck | Python 3.14.5, pytest 8.3.5, Windows | st1-assignment-3\project, python -m pytest -q | 5143ef49f3f0a372184110040a5fb59db2cca35e [updated from E]| 58 passed in 0.11s, 0 failed | https://github.com/linhvantran/st1-assignment-3/blob/c20613154832194a475990804f25325f6df754b6/stage12/c_regression_log.txt |
Prior assertions preserved / reviewed test diff: Earlier assertions are preserved
Remaining failure / limitation: None observed. 


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link                                                          |
|---|---|---|---|------------------------------------------------------------------------|
| Problem and stakeholders | Not a console step. Described from the SmartCare case study and the README. | SmartCare keeps patient, practitioner and appointment records for one session and enforces the booking and cancellation rules. | SmartCare helps a small clinic keep track of patients, practitioners and appointments so that bookings do not clash and cancelled appointments stay on record. Stakeholders: patients, practitioners, reception/administrative staff who book and cancel appointments, and the course staff who assess the system. | README (see Section F)                                                 |
| Register and find Patient and two Practitioners | Menu 1: P1 / Alex Example. Menu 2: P1. Menu 3: D1 / Taylor Example / General practice. Menu 3: D2 / Jordan Example / Cardiology. Menu 4: D1, then D2. | FR-01 to FR-03 register and find with validation | "Patient registered successfully. P1: Alex Example"; "Patient found. P1: Alex Example"; "Practitioner registered successfully" for D1 and D2; "Practitioner found. D1: Taylor Example, General practice" and "Practitioner found. D2: Jordan Example, Cardiology". | D_inputs.txt, D_outputs.txt: d3f100ee66991012523813b0b083270df2b4ac7f  |
| Valid booking | Menu 5: A1 / P1 / D1 / 2026-11-10 09:00 | FR-04 a booking for registered participants is stored as SCHEDULED | "Appointment booked successfully. A1: P1 with D1, 2026-11-10 09:00, scheduled" | same files                                                             |
| Same practitioner exact-time conflict rejected | Menu 5: A2 / P1 / D1 / 2026-11-10 09:00, then menu 7: A2 | FR-05 (AC-04.1) the same practitioner cannot have two SCHEDULED appointments at the same time; a rejected booking stores nothing | "Error: Practitioner already has a SCHEDULED appointment at this time". Menu 7 for A2 then printed "Error: Appointment not found", so the rejected booking was not stored. The menu continued. | same files                                                             |
| Different practitioner same time allowed | Menu 5: A3 / P1 / D2 / 2026-11-10 09:00 | FR-05 (AC-04.2) the conflict rule applies to the same practitioner only | "Appointment booked successfully. A3: P1 with D2, 2026-11-10 09:00, scheduled" | same files                                                             |
| Cancel SCHEDULED and retain/find CANCELLED object | Menu 6: A1, then menu 7: A1 | FR-06 cancel a SCHEDULED appointment; FR-07 and FR-08 the cancelled appointment is retained and can be found | "Appointment cancelled successfully. A1: P1 with D1, 2026-11-10 09:00, cancelled". Menu 7 then printed "Appointment found. A1: P1 with D1, 2026-11-10 09:00, cancelled". | same files                                                             |
| Invalid/repeated cancellation rejected | Menu 6: A1 again (already cancelled) | FR-06 (AC-05.3) only SCHEDULED appointments can be cancelled, and the state is unchanged | "Error: Only SCHEDULED appointments may be cancelled". The menu continued, and the next listing still shows A1 as cancelled. An unknown appointment ID was not part of this console run; it is covered by the automated tests. | same files                                                             |
| Default all-status listing | Menu 5: A4 / P1 / D1 / 2026-11-10 09:00 (freed slot), then menu 8: D1 with a blank status filter | FR-09 and QRY-01 to QRY-03 all statuses are listed, including cancelled history, in date/time then ID order | A4 booked successfully (the cancelled A1 no longer blocks the slot). The listing printed "1. A1: P1 with D1, 2026-11-10 09:00, cancelled", "2. A4: P1 with D1, 2026-11-10 09:00, scheduled" and "2 appointments found." A1 comes before A4 because the times are equal and the ID breaks the tie. | same files                                                             |
| Explicit filtering / empty vs unknown / deterministic order | Menu 8: D1 with `scheduled`, D1 with `cancelled`, D1 with `completed`, D9 with a blank filter | QRY-02 an explicit status returns only that status; QRY-04 a known practitioner with no matches gives an empty result, and an unknown practitioner is an error | `scheduled` printed only A4 ("1 appointments found."); `cancelled` printed only A1; `completed` printed "No appointments found."; D9 printed "Error: Practitioner not found". | same files                                                             |
| Invalid date/status/menu/lookup recovery and continued operation | Menu 8: D1 with `pending`. Menu 5 with the date `10/11/2026 9am`, with `2026-13-45 99:99`, and with unknown patient P9. Menu 7: A5, A6. Menu 1: duplicate P1. Menu 2: blank ID and P9. Menu choice `9`. Then menu 2: P1. | UI-02 expected input errors print a message and return to the menu, stored state is unchanged, and later actions still work | Each printed one message and returned to the menu with no traceback: "Error: Status must be scheduled, cancelled or completed"; "Error: Use date/time format YYYY-MM-DD HH:MM"; "Error: Invalid calendar date/time; use YYYY-MM-DD HH:MM"; "Error: Patient not found"; "Error: Appointment not found" for A5 and A6 (nothing was stored); "Error: Patient ID already exists"; "Error: Value inserted into find_patient is invalid"; "Error: Patient not found"; "Unknown choice. Choose a number from 0 to 8." The final "Patient found. P1: Alex Example" shows that operation continued normally. | same files                                                             |
| Session-only limitation and normal exit | The start-up banner, then menu 0 | The session data is temporary and is discarded on exit (accepted scope limitation) | Start-up printed "Session data is temporary and will be discarded when you exit." Menu 0 printed "Goodbye. Session data discarded." and the program returned to the prompt. | same files                                                             |
| One meaningful requirement-linked pytest test explained | `test_cancelled_appointment_is_retained_and_listed` in `project/tests/test_services.py` | FR-07 a cancelled appointment stays retrievable and listed | Arrange: book A1 for a registered patient and practitioner. Act: cancel A1. Assert: `find_appointment("A1")` returns the same object as before, that object is in `list_appointments()`, and its status is `AppointmentStatus.CANCELLED`. It would fail if cancellation deleted the record, as the Stage 8 defect did. It does not test persistence across sessions, because the data is session-only. | `project/tests/test_services.py`; regression result in Section C       |
| Architecture and one actual AI decision / known limitation | Section E and the Stage 9 Copilot review | Responsibilities are separated: domain rules, shared store, services, pure queries, console | `console.py` only reads input, prints and calls services; services validate and coordinate; `SmartCareDataStore` holds the three in-memory collections; `queries.py` has pure functions. AI decision: in Stage 9 Copilot reported that a listing test booked two SCHEDULED appointments for one practitioner at the same time, and the setup was modified to cancel A2 before booking A1. Known limitation: no persistence, so all data is lost on exit. | Section E; Stage 9 record, Section E                                   |
| PG reschedule identity/participants/time and no-op | Not applicable | Not applicable | Not applicable. There are no postgraduate members. | Not applicable                                                         |
| PG conflict/invalid status/failure non-mutation | Not applicable | Not applicable | Not applicable. There are no postgraduate members. | Not applicable                                                         |
| PG old slot / current lookup/list ordering / assurance risks | Not applicable | Not applicable | Not applicable. There are no postgraduate members. | Not applicable                                                         |

Stable demo owner / fresh process / command: Van TRAN ran the demo in a new PowerShell terminal in PyCharm with the project `.venv` active, on branch `debug/stage12`, at code SHA c3b07b540ca23e268394df431a23d4b38f1be35c. Command, from `project/`: `Get-Content ..\stage12\D_inputs.txt | python -u main.py --interactive 2>&1 | Tee-Object -FilePath ..\stage12\D_outputs.txt`

PG demonstrations through service/tests or not applicable: Not applicable. There are no postgraduate members.

## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | SHA 8715fa689410af2b8d80b3612a63b5fcb76e81b0. In domain.py, Patient/Practitioner validate their one fields (def required_text). Appointment owns status and cancel(). data_store.ppy: SmartCareDataStore holds three in-memory dicts. services.py services look up participants, check conflicts via has_practitioner_conflict, then add the appointment last, and cancel through Appointment.cancel(). In queries.py, appointment_sort_key and select_appointments are plain functions with explicit inputs that return a new sorted list. console.py parses inputs, prints outputs, and calls services only | No finding. The rule "only SCHEDULED appointments conflict" sits in the store's has_practitioner_conflict, which services call | No changes |
| PascalCase and snake_case naming | Using git grep -n -E "^class " returns AppointmentStatus, Patient, Practitioner, Appointment, SmartCareDataStore, PatientService showing all PascalCases. Functions, methods and variables in all five files utilise snake_case. | 'menu' in console.py is lowercase where 'MENU' is more preferable | No changes. This is purely cosmetic and I'm not bothered to fix it |
| Useful type hints and meaningful docstrings | All functions and methods have type hints, including run_menu and its nested handlers. There are some missing docstrings. These include: console.run_menu, data_store.find_appointment, data_store.has_practitioner_conflict. And there are misleading docstrings found in: services.find_patient and find_practitioner as they still contain the starter "raise NotImplementedError" things. Several services docstrings have "Stage 6:", "Stage 9:", and "Completion must..." starter wordings. services.find_appointment's docstring (blank ID raises ValueError) is accurate because data_store.find_appointment raises it | Stale/misleading docstrings and three missing docstrings | Added and edited docstrings in console.py and data_store.py. While looking through the console.py file, I deleted a useless comment that read " This is a test ".  |
| Four-space indentation and imports/layout | Indentations are in multiple of four, but several blocks in console.run_menu are over-indented or not indented consistently. For example, the find_appointment handler arguement, the exit branch and except body. service.py imports the local queries module before the standard library datetime import. There are trailing whitespaces in console.py and servces.py. There are also mixed single/double quote styles | Cosmetic layouts only | Can change except possibly the import order. This is mostly cosmetic so I'm not going to change it |
| Focused methods / duplication / dead or commented code | In services.py, there are 'raise NotImplementedError('Stage 9: practitioner appointments')' after the final return. data_store.Blank ID validation is repeated in services find_* and list_practitioner_appointments. console.run_menu is a long function with nested handlers. data_store.had_practitioner_conflict compared appointment.status.value == "scheduled" instead of AppointmentStatus.SCHEDULED | One unreachable statement, minor duplication, and a long function | Delete the unreachable raise. The rest is left as minor debt. |
| Globals / leakage / unnecessary inheritance or frameworks | [responseNo mutable module-level state. Each session's state lives in a SmartCareDataStore created inside the run_demo | run_menu in console.py. The only module-level non-constant is the "menu" string in console.py, which is never modified. The only inheritance is AppointmentStatus(Enum). Imports are re, datetime, enum and smartcare.*, so no frameworks. services.py contains no input()/print(), queries.py has no I/O, and domain. py does not import the store or services. | No findings. Console.py imports AppointmentStatus only to convert status text into an enum value, which is input parsing and acceptable. THERE ARE NO CHANGES |
| No SQLite/persistence/repository ABCs/speculative features | Storage is in three in-memory dicts in SmartCareDataStore and nothing is written to the disk. No sqlite3, json, ABC or abstractmethod imports, and no reschedule or delete features | No findings. | No changes. |
| Synthetic data / secrets / dependencies / provenance | Demo data in synthetic: P1/Alex Example, DR1/Taylor Example, A1. Applikcation code uses only the Python standard library. The only dev dependency is pytest, pinned in requirements-dev.txt [pytest 8.3.5]. Used git grep for secret-like terms and key patterns, returned no matches. ran git ls-files, showed no environment\, cache, compiled or key files, but did show editor metadata (.idea/, vscode/settings.json). | Editor metadata was tracked | Removed .idea/ and .vscode/ from tracking in commit 38b151852cecfc0ccd763218a7f5145381b7178f. Updated the .gitignore to prevent future problems. I have no idea who set this up but they completely butchered it hahahaha. |
| Significant common Copilot contributions and human verification | Copilot was used for test critique and diagnosis. Stage 7 (FR-07 / AC-05.2): two candidate tests for "cancelled history remains retrievable". One was modified into test_services.py::test_cancelled_appointment_is_retained_and_listed (T-21), one was rejected as duplicate. Stage 8 (F8-01, F8-02): Copilot ranked three possible causes for each injected defect. Stage 9 (QRY/FP, UI): Copilot review of the new tests found a booking order problem in a test_workflows.py listig test (modified) and confirmed that snapshot() uses methods that exist (accepted).| Every suggestion was checked against the code, the requirement and test runs before a decisions. Stage 7: assertion strength checked against the data store and the new test run. Stage 8: git diff between the known-good and injected commits, reading services.py and data_store.py, and test_regressions.py checks. Stage 9: reordered the test setup and re-ran then ran the full suite. | No findings. No copilot output was unchecked, no unreviewed dependancy was added, and no secrets or real data appear in the prompts recorded. Some suggestions were wrong or weak and were rejected with evidence. No change needed beyond the decisions recorded. Final regression after all stages: See C. |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | Not Applicable | Not Applicable | Not Applicable |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| Four tests need to be added to `test_data_store.py` to test datastore | `test_data_store.py` |Chars in `stage06_activities_and_evidence.md` section H | Modify. The test ideas smatched the `data_store.py` contracts, but they needed corrections before they ran. They also only cover patients, not practitioners, appointments or the conflict check | Tests were added with slight modifications. |
| Create a test so that after cancelling A1, assert that `find_appointment("A1")` is not `None` | `test_services.py` | Chars in `stage07_activities_and_evidence.md` section H | Accept. The intention matches AC-05.2, but the assertion proves too little. data_store.py never deletes appointments, so identity, status and list checks acan fall if retention breaks. I replaced theweak assertion with those three checks. | Test was added with modifications. |
| Create a test that cancels an appointment, create a new SmartCareDataStore form saved data, and assert the cancelled appointment still exists. | `test_services.py` | Chars in `stage07_activities_and_evidence.md` section H | Reject. it is a duplicate scenario. The handout tells us to reject duplicates. The new evidence is in T-21, which cancels through the service and checks find_appointment("A1") is appointment. | None. |
| practitioner-ID comparison in has_practitioner_conflict is inverted (!= instead of ==) | `data_store.py` | Chars in `stage08_activities_and_evidence.md` section F | Accept. The line and the reversed behaviour both confirm it. | Use sugestion to help fix behaviour |
| book_appointment passes an unexpected practitioner ID to the conflict check. | `data_store.py` | Chars in `stage08_activities_and_evidence.md` section F | Reject. The service passes the correct arguments, and the fault is the '!=" in the store's practitioner comparison. | None. |
| The datetime or status condition selects the wrong stored appointment. | `data_store.py` | Chars in `stage08_activities_and_evidence.md` section F | Modify Not the cause of F8-01; leave unchanged in the repair, and note the magic string as a possible refactor smell. | Help fix smell. |
| `find_appointment` returns a matching appointment only if its status is not "cancelled". | `data_store.py` | Thomas in `stage08_activities_and_evidence.md` section F | Accept. This explination is the likely cause as it is similar to my first competing idea. I have checked the code and there is infact a secion in `lookup_appointment()` in `data_store.py` that makes the lookup function return a LookupError if an appointment's status is CANCELLED. This is also supported by my findings in `test_regressions.py` where I found that the cancelled appointment still exists in the datastore itself but it is not found when using the lookup function. | Use suggestion to help fix behaviour. |
| Cancellation removes or replaces the stored record | `data_store.py` | Thomas in `stage08_activities_and_evidence.md` section F | Reject. From my testing in `test_regressions.py` as the cancelled appointment still exists in the datastore post cancellation but it cannot be found when using the lookup function. | None. |
| The service is using a different store or the lookup ID differs | `data_store.py` | Thomas in `stage08_activities_and_evidence.md` section F | Reject. All of the functions refer to the same `SmartCareDataStore` class in `data_store.py`. | None. |
| Listing test books A1 and A2 for D1 at EIGHT_AM while A2 is still SCHEDULED, causing a same-practitioner conflict | `test_practitioner_appointment_listing_filters_orders_and_isolates_results` in `tests/test_workflows.py | Chara in `stage09_activities_and_evidence.md` | Modify: Cancel A2 before booking A1 so the equal time fixture does not break the conflict rule. | Reordered the setup. |

Access route or approved equivalent / limitations: GitHub Copilot.
Available AI evidence and missing evidence honestly disclosed: AI evidence has been disclosed per the guidelines in the AI sections.


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [README.md,Group index & Scope and limitations] | [XiChen] | [OK] |
| Out-of-scope capabilities and known limitations | [README.md, Scope and limitations] | [XiChen] | [OK] |
| Confirmed teaching Python version and dependency installation | [README.md, Run] | [XiChen] | [OK] |
| Working directory / demo / interactive / test commands | [README.md, Run] | [XiChen] | [OK] |
| Repository structure and architecture responsibilities | [README.md, Structure] | [XiChen] | [OK] |
| Responsible AI summary / synthetic-data rule | [REAMDME.md, Group index] | [XiChen] | [OK] |
| Release label/version and SHA links | [README.md, Verification] | [XiChen] | [OK] |
Root README index and project/README verified: [Verified, root README.md is the vprimary project documentation]
Fresh clone or extracted ZIP / candidate identity: [Verified, cloned fresh from group GitHub repository]
Verifier and clean environment / actual version: [XiChen,clean venv,Python 3.13.5]
Setup/run/test commands and observed results: [Setup, run snd test commands execute successfully; appointment cancellation works as expected]
Missing local file or setup gap / remedy and recheck: [No missing local files, no blocking setup gaps]


## G Known limitations debt and release notes

Delivered features: A console, services, datastore, and queries that work together to make an appointment management system.
Important fixes: Lack of customisation, management, and persistance.
Architecture/quality improvements: Better documentation of architecture is needed.
Known limitations: Space code comments.
AI-assisted development note: AI has been used throughout the project as noted in the relevant sections of each stage.

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| Limited code comments. | Reduces maintainability of the program. | Low | Add more code comments and other documentation to make the code easier to understand. | Accept. The program is still ready for release in its current state. |
| Session-only synthetic data | Data is lost after restart of system | High | Add a long term storage solution. | Accept. The data is currently only used for demonstartion purposes. |
| Minute-precision local time | Session times can only be stored in local time and with a maximum precision of minute level. | Low | None. | Accept. The program will still be fit for purpose as you are expected to be booking an appointment in the local time of the practice and we don't need more than minute level precision. |

Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: These functions are currently not implemented in our program.
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: This system can currently only be accessed by the one single console at this time. The timezone that appointments are booked in is the same as the practice. Operations and monitoring is not currently implemented. Accessibility / usability limitations include accessibility and ease of use issues around a TUI.
Difference between accepted scope limit and unresolved required behaviour: The scope was more to create the underlying framework for an appointment system while a lot of these other uresolved issues are around the management and individual setup side of things.
PG assurance residual risks / owner / status or not applicable: N/A


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action                                                                 | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|------------------------------------------------------------------------------|---|---|---|
| Maintainability: docstrings are accurate and present (Section E, type hints and docstrings) | Code review of `services.py`, `console.py` and `data_store.py` at SHA 8715fa689410af2b8d80b3612a63b5fcb76e81b0 found docstrings in `services.find_patient` and `find_practitioner` that still describe the starter `NotImplementedError` and carry "Stage 6", "Stage 9" and "Completion must..." wording, and missing docstrings for `console.run_menu`, `data_store.find_appointment` and `data_store.has_practitioner_conflict`. | Low. No behavioural effect, but misleading to a maintainer or marker. | CrowdedWolf [Thomas]. Rewrite the stale docstrings and add the missing ones. | Docstrings added or corrected in `console.py` and `data_store.py`, commit 5143ef49f3f0a372184110040a5fb59db2cca35e. | Full suite after the correction: 58 passed at 5143ef49f3f0a372184110040a5fb59db2cca35e (Section C). | [Say whether the `services.py` docstrings were corrected. If any starter wording remains, record it here as minor debt.] |
| Maintainability: no dead or unreachable code | `list_practitioner_appointments` in `services.py` still had `raise NotImplementedError('Stage 9: practitioner appointments')` after its final return, and `console.py` contained the comment `# this is a test`. | Low. The `raise` could never run, and both lines were confusing leftovers. | CrowdedWolf [Thomas]. Delete both.                                                        | Unreachable `raise` and the stray comment removed, commit 5143ef49f3f0a372184110040a5fb59db2cca35e. | Full suite 58 passed at 5143ef49f3f0a372184110040a5fb59db2cca35e (Section C). | None for these lines. Duplicated blank-ID validation in the services and a long `run_menu` function remain as minor debt (Section G). |
| Release package: no tool metadata or environment files are tracked | `git ls-files` listed `.idea/` and `.vscode/settings.json` as tracked files. The IDE rewrites its `.iml` file on each machine, which also blocked a branch switch during Stage 12. | Medium for the submission package, because the ZIP must not contain tool metadata. No effect on behaviour. | CrowdedWolf [Thomas]. Stop tracking both folders and update `.gitignore`.                 | Commit 38b151852cecfc0ccd763218a7f5145381b7178f removed `.idea/` and `.vscode/` from tracking and updated `.gitignore`. | Full suite 58 passed at 5143ef49f3f0a372184110040a5fb59db2cca35e (Section C). `git ls-files` at the final SHA: [result, expect no `.idea` or `.vscode`]. | Local copies of the folders still exist on each machine but are now ignored by Git. |
| Code quality: status comparison uses the enum | `has_practitioner_conflict` in `data_store.py` compares `appointment.status.value == "scheduled"` instead of `AppointmentStatus.SCHEDULED`. | Low. It works, but a magic string is fragile if the enum value changes. | CrowdedWolf [Thomas]. Left unchanged to keep the release candidate stable.                | None. | Behaviour covered by the conflict tests in `test_services.py`, which pass in the full suite (Section C). | Accepted minor technical debt (Section G). |
| Code quality: layout and naming | `console.run_menu` has some inconsistent indentation, the services import `queries` before the standard-library `datetime`, there is trailing whitespace and mixed quote styles, and the `menu` constant is lowercase. | Low. Cosmetic only. | CrowdedWolf [Thomas]. Left unchanged after feature freeze.                                | None. | Not applicable, because no code changed. | Accepted cosmetic debt. |
| Console wording | In the Section D run, the listing printed "1 appointments found." for a single result. | Low. Cosmetic wording only, with the correct results listed. |CrowdedWolf [Thomas]. Left unchanged.                                                     | None. | Section D console run shows the correct records and counts. | Accepted cosmetic limitation. |

Justified no-change conclusion if no defect found: No functional defect was found against FR-01 to FR-09, QRY-01 to QRY-04 or FP-01 to FP-03. The full suite passed (58 passed, Section C), and the console demonstration (Section D) showed the expected results, error messages and recovery for every step. The findings above are code-quality and housekeeping items. Only the ones with a commit above were changed, and the rest are accepted as minor debt.

Release blockers still open / status: None identified so far. The README reproduction check (Section F) and the human release decision (Section J) are not yet complete, so this line is updated once they are done.


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: https://github.com/linhvantran/st1-assignment-3/pull/15 94693e5a1cec168db46e452976350b52878aabde
Independent reviewer / feedback / response: CrowdedGolf [Thomas]. Stage08 sections have been completed, pytests pass, and no conflicts prevent merge.
Integration commit / full recheck: 9690e687ba3dec28ce1b0fdd925445ebe5a7ebc1
Tracked and untracked file inspection / cleanliness: `.idea` and `.vscode` accidentally included.
Secrets/staff material/caches/tool-metadata exclusion check: `.idea` and `.vscode` accidentally included. No other data included.
Candidate recovery plan / known-good SHA: Fallback to stage08 if failure. 2fe8d58bf4104209e0f7f6caa079b84502c4c553
Named substantive contributions: All programing and responses for stage09.

Issue / PR / diff links and reviewed SHA: https://github.com/linhvantran/st1-assignment-3/issues/1 250f06b144ac6f40a515bed390b3791945192500
Independent reviewer / feedback / response: Chara. Problem solved. Merged the branch adding the Appointment Cancellation feature to resolve this issue.
Integration commit / full recheck: 250f06b144ac6f40a515bed390b3791945192500
Tracked and untracked file inspection / cleanliness: `.idea` accidentally included.
Secrets/staff material/caches/tool-metadata exclusion check: `.idea` accidentally included. No other data included.
Candidate recovery plan / known-good SHA: Fallback to previous non-code commit. b3f8bb7ab3cb2dbc87b4b8c92a04eed191895050
Named substantive contributions: Completion of the `find_patient()` function in `services.py`

## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [READY WITH DOCUMENTED LIMITATIONS]
Approver / date / rationale and evidence: [Whole team, 11 Nov 2026. The system satisfies all core functional requirements for this assessment.Supporting evidence includes test outputs, Git integration review records from section I and demonstration of the core workflow.A small number of secondary features are incomplete and listed below.]
What risks remain / conditions / owners: [1. Mobile responsive layout is not fully refined; owner: team.
                                          2. Full automated UI test suite is not implemented; owner: team.
                                          These items do not break core functions and will not interfere with marking of mandatory requirements.]
Can the team explain the system: [Yes.All team members understand the product purpose, userworkflow and compliance requirements.]
Can a change be recovered: [Yes. We can revert to the stable known-good commit SHA documented in section I]
Common decision / PG decision where different: [N/A]


## K Final tested release SHA

Exact common tested SHA: 7e662f074a0b3cdf1d8287319d40e4a54fb25985. Full suite: 58 passed with `python -m pytest -q` from `project/` (Section C).
Exact PG tested SHA or not applicable: Not applicable. There are no postgraduate members.
Final submitted SHA / repository URL: 25b641b899cf52e3be1f58192afb0d864009d387 / https://github.com/linhvantran/st1-assignment-3
Evidence-only later commit and difference explanation: Commits after the tested SHA only changed the records in `stage12/`. `git diff --stat 5143ef49f3f0a372184110040a5fb59db2cca35e d3f100ee66991012523813b0b083270df2b4ac7f  final SHA  7e662f074a0b3cdf1d8287319d40e4a54fb25985 -- project` printed nothing, so no executable code differs.
Executable changes after testing and re-verification: None. 
Source ZIP name / SHA correspondence / extracted comparison: [zip name] was created with `git archive` from commit 7e662f074a0b3cdf1d8287319d40e4a54fb25985. It was extracted to a clean folder, its file list matched `git ls-tree` for that commit, and `python -m pytest -q` there gave 58 passed.


## L Submission package verification

- [X ] Feature freeze and scoped requirements traced.
- [X ] Applicable full regressions, integrated demo and invalid paths verified.
- [X ] Architecture/code quality and final AI/dependency checks complete.
- [X ] Root README and project/README reproduced by another verifier.
- [X ] Release notes, technical debt and limitations visible.
- [X ] Independent human review, integration and release decision recorded.
- [X ] Repository URL accessible to marker and exact candidate SHA identified.
- [X ] One source ZIP from submitted commit with root README.md and .gitignore.
- [X ] project/ source and all accumulated applicable tests included.
- [X ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [X ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [X ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [X ] Mixed-group common protection and candidate upload routing checked.
- [X ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [Team will submit via the single provided group submission URL]
Deadline/timezone: [13/11/2026]
Repository access arrangement: [Repository is public,accessible to marker]
Mixed-candidate upload arrangement: [Not applicable for this group]
Oral/video recording/accessibility arrangements: [Individual oral assessment,each team member completes their own oral task separately.]
Remaining administration or release dependency: [No outstanding release dependencies.]


## M Formative questions

1. What is a release candidate? A release candidate is an exact version of the software that the team believes is ready to release and is now testing. If a serious problem is found, then it is fixed and a new candidate is tested. 

2. What is feature freeze and why is it used? A feature freezed is the point after which no new or optional features are added. It keeps the code stable so the tests, demo and documentation stay valid for the version being released .

3. What is regression testing in a release context? Regression testing in the release context means re-running the accumulated test suite on the release candidate to confirm that release changes have not broken anything that previously worked. Earlier tests are kept and not replaced to get a working result. 

4. What is a known limitation? A known limitation is a documented thing that the software does not do, or does partially. For example, for the software, the data is lost when the session ends. It isn't a defect because a requirement is not broken, it simply lacks the capability to remember because no storage was added. 

5. What is technical debt? Technical debt are shortcuts or imperfect designs and code choices that work not but make future changes harder or riskier. It is recorded with its impact, priority and a planned fix. 

6. What are release notes? Release notes are short summaries for users and maintainers of what the release contains. This would contain the new features, fixes, quality improvements, limitations, and more. 

7. What is software maintenance? Software maintenance is the work after the release is created. Fixing bugs found after the release, improving code, and adding features. 

8. What is the purpose of the individual demonstration/viva? Utilised to show that each team member understands/comprehends the system, acknowledge their contributions/resposibilities, the design decisions, and the AI decisions if AI is used. Makes sure that the programmers understand the system and aren't mindlessly pushing code from AI.

9. What should the final responsible-AI check establish before release? That AI generated contributions were reviewed and understood by a human, are traceable, don't include unreviewed dependencies and more. Each suggestion is a candidate that was independently checked and accepted, modified or rejected, and any missing evidence is disclosed honestly. 

10. What is the main course conclusion about AI and the role of the software engineer? AI can speed up writing code, but it cannot replace engineers. Engineers remain reponsible for meeting the requirements, creating designs, verification, security and release decisions. The engineers must be able to explain the system and if anything goes wrong, the engineer will be held accountable as AI cannot hold responsibility. 


## N Reflection viva and handover

Strongest evidence SmartCare is ready: The full suite passes (58 tests, shown in section C), and the console demo (Section D) ran the whole required sequence from a frech process. Same-practitioner conflict rejected while a different practitioner was allowed, cancellation retained as CANCELLED, listing with filters and ordering, and recovery from invalid inputs. The tets and demo agree with each other, and all requirements are filled. 
Weakest area: In this project, editor metadata was tracked in the repository, and it was hard to keep every piece of evidence tied to one exact commit. In the code, the comments were thin and the project suffers form a lack of persistence [although that is a deliberate scope limit]. 
How AI use changed from Stage 1 to Stage 12: From Stage 1, we used AI to help understand the code. Mainly using AI to help us understand the syntax and the functionality of programs. Getting it to assist us in learning Python. By Stage 7 to 9, we understood the code and now used the AI to help us propose test cases and and assist in diagnosis when debugging programs, treating every suggestion as a hypothesis. By Stage 12, we utilised the AI to check against the code, critique it and suggestion improvements. 
Start doing — engineering and AI use: Ensure that all of the changes had been pushed before you make branches. This branch initially did not contain the Stage 9 data due to miscommunication and that left me puzzled when I ran tests. When it comes to AI, we must confirm the approved Copilot route with the teaching team, saving prompts and outputs as we go. Sometimes I forget to get the output references and that is bad practice. 
Stop doing — engineering and AI use: Stop letting tool files into the repository. Next time, double check the .gitignore file. I don't know how we went though the project without noticing this but we did. For AI, we need to stop accepting an AI explanation of a failure before reproducing it. When it came to testing, the AI sometimes got things wrong so it's useful to double check and get your own opinion on the matter.
Continue doing — engineering and AI use: Requirement tests, Pull request reviews, and creating test cases. For AI, checking every suggestion independently before accepting, modifying or rejecting with evidence. 
What worked / caused rework / future delivery improvement: What worked: The separation into domain, store, services, queries and console made defects easy to localise (In stage 8, we found the defects by comparing diffs and running the regression tests). Rework: The outdated branch base and the tracked editor files. Improvement: Check and commmunicate more clearly with your teammates. Everything here was caused by a lack of communication and not checking everything. The .gitignore issue should have been caught early. The branch shouldn't have been created before the merge to main.
One paragraph — If AI can write code why do we still need software engineers: AI can produce code quickly, but it cannot be held accountable for whether that code is right. An AI cannot reliably diagnose problems in a program 100% of the time and sometimes it doesn't focus on the requirements. The AI can work on the programming but it doesn't consider the project as a whole. Engineers decide what the software must do for its stakeholders, design it so it can be changed safely in the future, verify it with evidence, and notice what the tests do not prove, taking responsibility for releasing it, explaining it, and recovering it when something goes wrong. 

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | A small clinic needs to keep track of patients, practitioners and appointments so that bookings do not clash and cancelled appointments stay on record. Stake holders include patients, practitioners, and receptionists/administrative staff. Refer back to section D, |
| Two requirements and acceptance criteria | The same practitioner cannot have two SCHEDULED at the same time (AC-04.1), while a different practitioner at that time is allowed (AC-04.2). FR-07: A cancelled appointment is retained and can still be found, as the same object with CANCELLED status (AC-05.2). |
| Domain model and architecture | Patient, Practitioner and Appointment own validated fields. Appointment and AppointmentStatus own status and the guarded cancel(). SmartCareDataStore holds the three in-memory collections. Services coordinate use cases and shared-store checks. Queries.py has pure functions. Console.py handles input and output only. Elaborated on (Evidence) in Section E. |
| Design trade-off | It's really simple and easy to test things in the program, at the cost of no persistence (memory) and concurrency. We accepted this because the release is session-only (Sections B and G) |
| Meaningful test and its limits / 100 percent coverage | test_cancelled_appointment_is_retained_and_listed (test_services.py) asserts that find_appointment returns the same obejct, that is still in list_appointments(), and that its status is CANCELLED. It would fail if cancellation deleted the record. it does not prove anything about persistence across sessions. 100 percent coverage only shows every line ran. It does not show if the behaviour is right or wrong, that all requirements are tested, or that the assertions are strong. |
| Diagnosed defect and verification | F8-01, the practitioner ID comparison in has_practitioner_conflict was inverted (!= instead of ==). F8-02, lookup hid CANCELLED appointments so they could not be found. We confirmed each by comparing the known good and the injected commits, reading data_store.py and running test_regressions.py. Section F |
| Shared store and session-state/query responsibilities | One SmartCareDataStore is created per session and passed to every service, so all services see the same records. Queries take an explicit list and return a new sorted list with no input/output and no changes to the source. Section E |
| What would break if session-state lookup/query responsibilities changed? | If services used different stores, a booking made through one would be invisible to cancellation or the conflict check, so conflicts would be missed and cancellations would fail. if queries read the store directly or changed what they were given, they could no longer be tested on their own, and the filtering and ordering could change without the service noticing. |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | cancel() is in Appointment because only the appointment knows its own status rules (only SCHEDULED can be cancelled). A conflict depends on all appointments for a practitioner, which no single appointment knows about, so a service coordinates it using the shared store.  |
| FR-07 retained history test | test_cancelled_appointment_is_retained_and_listed (T-21): book A1, cancel it, and then check the same object is found, listed and CANCELLED. In the console demo, cancelling A1 and then finding A1 showed "cancelled". Sections B and D. |
| Actual AI change rejected/modified or honestly accepted with verification | Stage 7: Copilot's duplicate persistence style test was rejected and the weak assertion was strengthened. Stage 8: The wrong candidate causes were rejected after checking the code and tests. Stage 9: The listing-test setup was modified to cancel A2 before booking A1. Section E. |
| Unresolved limitation / future production work | No persistence. All data is lost when the process ends. Before any real deployment, there must be durable storage, authentication and roles, privacy and security assessmment and cetification, concurrenty, monitoring and an accessibility evaluation. |
| Personal implementation contribution | Chars: I wrote console.py's run_menu() which is based off the terminal I wrote for Assignment 2. It implements a simple shell-based interface for the user. |
| Personal test/review/design/integration contribution | Chars: For Stage 6: I reviewed all the code for the functions that Thomas and Leo created and pull requested for. I handled in creating the issues for Stage 8 to 12 and verified the pull requests from then on.   |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
