# Stage 12 activities and evidence

BLANK student response template. Supplied from the beginning in stage12/ in your EXISTING repository; complete it only when you reach Stage 12 after the previous applicable stage is integrated, verified and recorded; preserve project/, tests, earlier records and Git history. UG/common and PG/extended scope must be explicit. Use concise results and versioned links, not copied logs or source. No staff answers or fabricated approvals.

Group/tutorial: 9:30-11:30 Monday Group 1
Members and UG/PG applicability: 


## A Release scope and starting SHA

Release label/version and requirements baseline: v1.0. Requirements baseline: FR-01 to FR-09, QRY-01 to QRY-04, FP-01 to FP-03
Common starting SHA / branch / applicable members: 9690e687ba3dec28ce1b0fdd925445ebe5a7ebc1 / debug/Stage12 / Chars, Thomas, Van, Leo 
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
| Complete common | [response] | [response] | [response] | [response] | [response] |
| Complete PG if applicable | [response] | [response] | [response] | [response] | [response] |
| Affected focused checks after correction | [response] | [response] | [response] | [response] | [response] |
| Full integrated recheck | [response] | [response] | [response] | [response] | [response] |
Prior assertions preserved / reviewed test diff: [response]
Remaining failure / limitation: [response]


## D Console and end to end demonstration

| Demo step | Synthetic setup/input | Expected requirement | Observed result | Evidence/link |
|---|---|---|---|---|
| Problem and stakeholders | [response] | [response] | [response] | [response] |
| Register and find Patient and two Practitioners | [response] | [response] | [response] | [response] |
| Valid booking | [response] | [response] | [response] | [response] |
| Same practitioner exact-time conflict rejected | [response] | [response] | [response] | [response] |
| Different practitioner same time allowed | [response] | [response] | [response] | [response] |
| Cancel SCHEDULED and retain/find CANCELLED object | [response] | [response] | [response] | [response] |
| Invalid/repeated cancellation rejected | [response] | [response] | [response] | [response] |
| Default all-status listing | [response] | [response] | [response] | [response] |
| Explicit filtering / empty vs unknown / deterministic order | [response] | [response] | [response] | [response] |
| Invalid date/status/menu/lookup recovery and continued operation | [response] | [response] | [response] | [response] |
| Session-only limitation and normal exit | [response] | [response] | [response] | [response] |
| One meaningful requirement-linked pytest test explained | [response] | [response] | [response] | [response] |
| Architecture and one actual AI decision / known limitation | [response] | [response] | [response] | [response] |
| PG reschedule identity/participants/time and no-op | [response] | [response] | [response] | [response] |
| PG conflict/invalid status/failure non-mutation | [response] | [response] | [response] | [response] |
| PG old slot / current lookup/list ordering / assurance risks | [response] | [response] | [response] | [response] |
Stable demo owner / fresh process / command: [response]
PG demonstrations through service/tests or not applicable: [response]


## E Final code quality and AI review

| Review area | Code/evidence location | Finding or no finding | Correction/no change and recheck |
|---|---|---|---|
| OOP responsibilities and pure-query boundaries | [response] | [response] | [response] |
| PascalCase and snake_case naming | [response] | [response] | [response] |
| Useful type hints and meaningful docstrings | [response] | [response] | [response] |
| Four-space indentation and imports/layout | [response] | [response] | [response] |
| Focused methods / duplication / dead or commented code | [response] | [response] | [response] |
| Globals / leakage / unnecessary inheritance or frameworks | [response] | [response] | [response] |
| No SQLite/persistence/repository ABCs/speculative features | [response] | [response] | [response] |
| Synthetic data / secrets / dependencies / provenance | [response] | [response] | [response] |
| Significant common Copilot contributions and human verification | [response] | [response] | [response] |
| PG plan/diff/test approvals and Stage 11 VERIFY/TRUST | [response] | [response] | [response] |

| AI claim | Affected requirement/code | Human check | Accept/Modify/Reject and reason | Actual outcome/action or no change |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Access route or approved equivalent / limitations: [response]
Available AI evidence and missing evidence honestly disclosed: [response]


## F README and reproducibility check

| README item | Location | Verifier | Result/gap |
|---|---|---|---|
| Purpose and included common/PG scope | [response] | [response] | [response] |
| Out-of-scope capabilities and known limitations | [response] | [response] | [response] |
| Confirmed teaching Python version and dependency installation | [response] | [response] | [response] |
| Working directory / demo / interactive / test commands | [response] | [response] | [response] |
| Repository structure and architecture responsibilities | [response] | [response] | [response] |
| Responsible AI summary / synthetic-data rule | [response] | [response] | [response] |
| Release label/version and SHA links | [response] | [response] | [response] |
Root README index and project/README verified: [response]
Fresh clone or extracted ZIP / candidate identity: [response]
Verifier and clean environment / actual version: [response]
Setup/run/test commands and observed results: [response]
Missing local file or setup gap / remedy and recheck: [response]


## G Known limitations debt and release notes

Delivered features: [response]
Important fixes: [response]
Architecture/quality improvements: [response]
Known limitations: [response]
AI-assisted development note: [response]

| Debt item | Impact | Priority | Future action | Accepted? / release rationale |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |
Session-only synthetic data and minute-precision local time: [response]
Production auth/roles, portal, notifications, billing/insurance, clinical AI exclusions: [response]
Scale/concurrency, timezone policy, operations/monitoring, accessibility/usability limitations: [response]
Difference between accepted scope limit and unresolved required behaviour: [response]
PG assurance residual risks / owner / status or not applicable: [response]


## H Release findings and corrective action

| Requirement/claim | Reproduction/observation | Impact/severity | Owner/action | Corrective diff | Focused/full recheck | Residual limit |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |
Justified no-change conclusion if no defect found: [response]
Release blockers still open / status: [response]


## I Git review and integration evidence

Issue / PR / diff links and reviewed SHA: [response]
Independent reviewer / feedback / response: [response]
Integration commit / full recheck: [response]
Tracked and untracked file inspection / cleanliness: [response]
Secrets/staff material/caches/tool-metadata exclusion check: [response]
Candidate recovery plan / known-good SHA: [response]
Named substantive contributions: [response]


## J Human release decision

Decision — READY FOR COURSE RELEASE / READY WITH DOCUMENTED LIMITATIONS / NOT YET READY: [response]
Approver / date / rationale and evidence: [response]
What risks remain / conditions / owners: [response]
Can the team explain the system: [response]
Can a change be recovered: [response]
Common decision / PG decision where different: [response]


## K Final tested release SHA

Exact common tested SHA: [response]
Exact PG tested SHA or not applicable: [response]
Final submitted SHA / repository URL: [response]
Evidence-only later commit and difference explanation: [response]
Executable changes after testing and re-verification: [response]
Source ZIP name / SHA correspondence / extracted comparison: [response]


## L Submission package verification

- [ ] Feature freeze and scoped requirements traced.
- [ ] Applicable full regressions, integrated demo and invalid paths verified.
- [ ] Architecture/code quality and final AI/dependency checks complete.
- [ ] Root README and project/README reproduced by another verifier.
- [ ] Release notes, technical debt and limitations visible.
- [ ] Independent human review, integration and release decision recorded.
- [ ] Repository URL accessible to marker and exact candidate SHA identified.
- [ ] One source ZIP from submitted commit with root README.md and .gitignore.
- [ ] project/ source and all accumulated applicable tests included.
- [ ] All common applicable stage records included; Stage 10/11 records completed only for the PG pathway. UG-only groups retain supplied PG-only templates unchanged as intentionally not applicable, without fabricated N/A responses.
- [ ] No .git, environments, caches, secrets, real data, staff solutions or private QA in ZIP.
- [ ] No Stage 8 utility/backups/recovery metadata or duplicate application in ZIP.
- [ ] Mixed-group common protection and candidate upload routing checked.
- [ ] Group reflection, confidential individual peer forms and common team viva routed separately.

Confirmed assessment item/upload route: [response]
Deadline/timezone: [response]
Repository access arrangement: [response]
Mixed-candidate upload arrangement: [response]
Oral/video recording/accessibility arrangements: [response]
Remaining administration or release dependency: [response]


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

Strongest evidence SmartCare is ready: [response]
Weakest area: [response]
How AI use changed from Stage 1 to Stage 12: [response]
Start doing — engineering and AI use: [response]
Stop doing — engineering and AI use: [response]
Continue doing — engineering and AI use: [response]
What worked / caused rework / future delivery improvement: [response]
One paragraph — If AI can write code why do we still need software engineers: [response]

| Preparation item | Own explanation and evidence link |
|---|---|
| Problem and stakeholders | [response] |
| Two requirements and acceptance criteria | [response] |
| Domain model and architecture | [response] |
| Design trade-off | [response] |
| Meaningful test and its limits / 100 percent coverage | [response] |
| Diagnosed defect and verification | [response] |
| Shared store and session-state/query responsibilities | [response] |
| What would break if session-state lookup/query responsibilities changed? | [response] |
| Why cancellation is domain behaviour / conflict coordination is service behaviour | [response] |
| FR-07 retained history test | [response] |
| Actual AI change rejected/modified or honestly accepted with verification | [response] |
| Unresolved limitation / future production work | [response] |
| Personal implementation contribution | [response] |
| Personal test/review/design/integration contribution | [response] |
| PG agentic change and rescheduling verification | [response] |
| PG responsible-AI risk/remediation or supported no finding | [response] |

Optional bounded-change practice only: validation rule, focused test, safe error-message change, explicit-input query or agreed status rule with test. Explain expected impact before editing, make a small change, run the test, and identify evidence to inspect if unsure. No live AI unless explicitly permitted. Preserve the submitted candidate.

Practice question/change and reasoning: [response or not undertaken]
Separate reflection / peer / common team viva evidence links and routing: [response]
No further coding stage. Later corrections use the published assessment process.
