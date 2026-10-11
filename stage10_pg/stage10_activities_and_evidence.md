# Stage 10 PG agentic rescheduling activities and evidence

PG-only stage. Undergraduate students are not required to complete this record. UG-only groups retain this supplied template unchanged as intentionally not applicable; do not fabricate N/A responses. Optional UG help is voluntary and unassessed.

All Assignment 3 stage materials are provided from the beginning. Complete this stage only after the previous applicable stage has been integrated, verified and recorded. Use this supplied record in stage10_pg/ in your EXISTING repository. Preserve project/, all earlier tests, records and responses. Do not download another starter or copy staff solutions. Protect the common Stage 9 SHA and UG Stage 12 pathway.

This is a blank student record. Use actual accessible links and concise evidence; do not invent an agent session, test result or approval. Retain this record's headings when linking equivalent issue/PR evidence.

Group/tutorial: [response]
Assessed PG members and roles: [response]
Optional UG contributors: [response or none]

## A Access baseline and recovery

- Confirmed GitHub Copilot feature/mode, version/environment and teaching-team approval reference: [response]
- Actual account access and tool permissions check: [response]
- Live route or convenor-confirmed equivalent staged interaction: [response]
- Access limitation and tutor resolution if applicable: [response]
- Protected Stage 9 common SHA / recoverable reference: [response]
- Common baseline command / project working directory / actual result: [response]
- Clean branch and preparer / recovery baseline: [response]
- Evidence-only later SHA if different / explanation: [response]

## B Tutorial activities

### B1 Rewrite the vague task

“Improve SmartCare appointment scheduling.” Write your bounded goal, requirements, exclusions, constraints, acceptance criteria and Definition of Done: [response]
Predicted changed files and human test intentions: [response]

### B2 Judge every proposed plan step

| Proposed step | Accept / Modify / Reject | Requirement evidence and reason |
|---|---|---|
| Redesign database schema | [response] | [response] |
| Add notifications | [response] | [response] |
| Introduce calendar library | [response] | [response] |
| Modify Patient | [response] | [response] |
| Add rescheduling | [response] | [response] |
| Rewrite all tests | [response] | [response] |

### B3 Six proposed changes

| File or action | Expected? | Review concern and evidence needed |
|---|---|---|
| Appointment in project/smartcare/domain.py | [response] | [response] |
| project/smartcare/services.py | [response] | [response] |
| Proposed sqlite_repository.py / schema change | [response] | [response] |
| Patient fields in project/smartcare/domain.py | [response] | [response] |
| requirements-dev.txt adds calendar package | [response] | [response] |
| Existing appointment assertions weakened | [response] | [response] |

### B4 Approval gate

Agent says “All tests pass.” Give at least SIX distinct checks before approval.
1. [response]
2. [response]
3. [response]
4. [response]
5. [response]
6. [response]
Additional checks if useful: [response]

### B5 Exit question

Why does increasing AI autonomy increase rather than decrease the importance of software engineering discipline? [response]

## C Human task specification before AI

- Goal: [response]
- Requirements RES-01–06 with RES-05-R2: [response]
- Out of scope: [response]
- Architecture constraints: [response]
- Acceptance criteria: [response]
- Definition of Done: [response]
- Issue / PG owner: [response]
- Human expected positive, negative and boundary tests: [response]
- Allowed files: [response]
- Forbidden/unnecessary files and changes: [response]
- Baseline/recovery link: [response]
- Evidence that human analysis preceded agent use: [response]

## D Agent plan and approval

Actual plan-only prompt/context and response or confirmed equivalent artefacts: [links]

| Plan step / action | Requirement link | Reason | Expected files | Accept / Modify / Reject | Conditions / evidence |
|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] |

Approved bounded scope / forbidden changes / verification plan: [response]
Human plan approver and approval before edits: [actual evidence]
Tool permissions and any expanded-scope requests / decision: [response]

## E Production diff review

Actual proposal / branch diff / version reviewed: [links]

| File | Change purpose and reason | Requirement / test link | Expected? | Architecture OK? | Decision | Notes / correction |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |

Every changed file inspected, including new/untracked files: [evidence]
Unexpected changes, scope creep, secrets/dependencies/configuration, unrelated cleanup: [response or none with evidence]

## F Separate test review

| Test | Criterion | Actual assertion | Assertion meaningful / adequate? | Agent changed expected behaviour? | Human or agent authorship | Decision and reason |
|---|---|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] | [response] | [response] |

Comparison with original common tests / any proposed weakening: [response]
Independent human checks and corrections: [response]

## G Actual verification

| Requirement / acceptance scenario | Test or demonstration | Meaningful expected result | Actual result | Evidence / version |
|---|---|---|---|---|
| RES-01 / AC-RES-01 successful move | [response] | [response] | [response] | [response] |
| RES-02 same object and participant identities | [response] | [response] | [response] | [response] |
| RES-03 / AC-RES-02 unknown and invalid IDs | [response] | [response] | [response] | [response] |
| RES-04 / AC-RES-03 conflicting practitioner | [response] | [response] | [response] | [response] |
| AC-RES-04 different practitioner allowed | [response] | [response] | [response] | [response] |
| RES-06 / AC-RES-05 cancelled and completed | [response] | [response] | [response] | [response] |
| RES-05-R2 / AC-RES-06-R2 lookup and listing order | [response] | [response] | [response] | [response] |
| Self-exclusion and same-time no-op | [response] | [response] | [response] | [response] |
| Invalid datetime and failed-state snapshots | [response] | [response] | [response] | [response] |
| Successful old-slot reuse | [response] | [response] | [response] | [response] |

| Suite | Command / working directory | Code SHA | Actual count and result | Evidence |
|---|---|---|---|---|
| Focused PG | [response] | [response] | [response] | [response] |
| Common independently | [response] | [response] | [response] | [response] |
| Full cumulative | [response] | [response] | [response] | [response] |
| Integrated retest | [response] | [response] | [response] | [response] |

Failures / diagnosis / corrections and reruns / unresolved concerns: [response]

## H Decisions corrections and independent review

| Significant agent action | Human review and evidence | Accept / Modify / Reject and reason | Manual correction or recovery | Recheck evidence |
|---|---|---|---|---|
| [response] | [response] | [response] | [response] | [response] |

Final proposal decision: [Accepted / Accepted after modification / Rejected]
Evidence supporting decision: [response]
If rejected, how the required feature was subsequently completed and verified: [response or not applicable]
Saved proposal and targeted recovery details if needed: [response or not applicable]
Human explanation of every changed method and limitations: [response]
Another PG / willing UG / tutor reviewer, actual PR/diff review and feedback: [links]
Corrections, recheck and actual approval before integration: [links]
Integrated PG SHA / common protected SHA: [response]
Each assessed PG member's implementation, supervision and test contribution: [response and links]
Optional UG help, acknowledged separately: [response or none]

## I Four reflections

1. Which agent change had the greatest blast radius? [response]
2. Did the plan predict it? [response]
3. What did you reject or manually correct? [response; report honestly if none]
4. What evidence justified final approval? [response]

## J Ten formative questions

1. What is the difference between an AI assistant and an engineering agent? [response]
2. What is the simplified agent loop used in Stage 10? [response]
3. Why should an agent plan be reviewed before repository edits begin? [response]
4. What is meant by the blast radius of a software change? [response]
5. Why is diff review essential for agentic changes? [response]
6. What is a human approval gate? [response]
7. What is test accommodation and why is it dangerous? [response]
8. What is rollback in the context of agentic software engineering? [response]
9. Who remains accountable for accepted agentic changes? [response]
10. What is the Stage 10 engineering rule? [response]

## K Completion and Stage 11 handover

- [ ] Common Stage 9 checkpoint protected; UG pathway unaffected.
- [ ] RES-01–06 and RES-05-R2 implemented in the same project.
- [ ] Domain/service boundaries, current exceptions and coding standard preserved.
- [ ] Positive/negative/boundary cases and failed-state checks verified.
- [ ] Common tests remain valid and independently passing; full suite passes.
- [ ] Plan reviewed before bounded actions; every file and test diff inspected.
- [ ] Actual agent route, decisions, corrections and rechecks recorded honestly.
- [ ] No unrelated features, persistence, dependencies or staff solutions introduced.
- [ ] Another-member or tutor review and integrated retest complete.
- [ ] Tutorial, four reflections, ten formative responses and PG contributions complete.
- [ ] Each PG member can explain their code and supervision.
- [ ] README PG note, actual integrated SHA and limitations recorded.

Unresolved issues / owner / action: [response]
Stage 11 handover references to extension, tests, dependencies and actual AI/review evidence: [response]
Submitted SHA / explanation if later than tested code: [response]
Stage 11 materials are supplied from the beginning. Begin Stage 11 only after Stage 10 has been integrated, verified and recorded. UG follows the protected common code from Stage 9 to Stage 12.
