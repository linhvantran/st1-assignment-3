# Stage 6 activities and evidence

Complete this one group record. Link actual issues, diffs, tests and reviews; avoid copying entire histories. Blank fields are intentional. Duplicate rows as needed. Use synthetic data only. Every member records their own meaningful contribution. Do not invent results, reviews or Copilot use.

- Group/tutorial: [Mon 9:30-11:30 Group 1]
- Members, GitHub usernames and cohorts: [Van Tran (@linhvantran), Xi Chen (@cz1295768-ui), Chars (@charatwukki), Thomas Pollock (@CrowdedGolf)]
- Repository URL: [(https://github.com/linhvantran/st1-assignment-3)]
- Starting SHA: [response]

## A Requirement to issue activities

### FR-02 Patient Search

- Title: [Patient lookup by ID in PatientService]
- Context: [Booking and later stages need to retrieve a registered patient reliably. The service layer currently has no working lookup, so callers can’t tell “patient not found” from “bad ID”.]
- Requirement: [FR-02 Patient Search, implemented in PatientService.find_patient. Supporting criterion, only if agreed with your tutor: PractitionerService.find_practitioner follows the same contract.]
- Acceptance criteria: 
  - Given a registered patient ID, find_patient returns the same stored Patient object, not a copy or a new one.]
  - Given a valid but unregistered ID, it raises LookupError.]
  - Given a blank, whitespace-only or non-string ID, it raises ValueError.]
  - A lookup, successful or failed, doesn’t add, change or remove any stored patient.]
- Scope: [In scope are PatientService.find_patient and its tests in test_services.py. Out of scope are searching by name, changes to domain.py or data_store.py, and any new features.]
- Definition of Done: [The new tests pass alongside the supplied tests. Another member reviews the actual diff and any feedback is resolved. The PR links to this issue and the docstring still matches the behaviour.]
- Owner: [Van Tran (@linhvantran)]
- Actual issue link: [https://github.com/linhvantran/st1-assignment-3/issues/1]

### FR-06 Appointment Cancellation with FR-07 retained history

- Title: [Cancel a scheduled appointment and keep it in the record]
- Context: [Patients and practitioners sometimes need to cancel appointments. The service has no working cancellation, so a SCHEDULED appointment can’t be cancelled and there’s no guarantee that a cancelled appointment stays on record afterwards.]
- Requirement: [FR-06 Appointment Cancellation (only SCHEDULED appointments may be cancelled) and FR-07 retained history (a cancelled appointment stays retrievable with status CANCELLED). Implemented in AppointmentService.cancel_appointment.]
- Acceptance criteria:
  - Given a SCHEDULED appointment, cancel_appointment changes its status to CANCELLED and returns the same stored Appointment object.
  - After cancellation, the appointment is still in the store: find_appointment returns it and list_appointments includes it (FR-07).]
  - Given a valid but unknown appointment ID, it raises LookupError.
  - Given a blank or invalid ID, it raises ValueError.
  - Cancelling an already CANCELLED appointment raises ValueError, and the status stays CANCELLED.
  - Cancelling a COMPLETED appointment raises ValueError, and the status stays COMPLETED.
- Scope: [In scope are AppointmentService.cancel_appointment and its tests in test_services.py, with the existing Appointment.cancel() doing the state change. Out of scope are deleting appointments, rescheduling, changes to domain.py or data_store.py, and the Stage 9 practitioner appointment listing.]
- Definition of Done: [The new tests pass alongside the eight supplied tests. Another member reviews the actual diff and any feedback is resolved. The PR links to this issue, and the docstring and criteria agree.]
- Owner: [Van Tran (@linhvantran)]
- Actual issue link: [(https://github.com/linhvantran/st1-assignment-3/issues/2)]

## B Commit quality

| Original example | Strong or Weak | Reason |
|---|----------------|---|
| changes | Weak           | It says nothing about what changed or why. A reviewer or future maintainer can’t tell from the history whether it was a fix, a feature or a cleanup, so the commit is hard to find, review or revert. |
| final version | Weak           | It describes a moment in the project rather than a change, and “final” is rarely true. It gives no clue about the content, so it fails as a record of the work. |
| Add patient search by ID | Strong         | It starts with a verb and names one specific behaviour, so it reads as one coherent change that maps to FR-02. A reviewer knows what to expect in the diff. |
| fix stuff | Weak           | “Stuff” doesn’t identify what was wrong or which part of the code was touched, and a fix with no description can’t be checked against a requirement or a bug. |
| Prevent cancellation of completed appointments | Strong       | It states the rule the change enforces in terms of behaviour, and it matches the FR-06 criterion that COMPLETED appointments can’t be cancelled. It’s clearly one focused change, so it’s easy to review. |

## C Over scoped PR review

A cancellation PR also renames unrelated patient fields, restructures unrelated code and adds a new dependency.

- Scope concerns:
  - [The PR was meant to deliver one behaviour, cancellation (FR-06/FR-07), but it also contains three unrelated changes. The patient field rename, the restructuring and the new dependency aren’t needed for cancellation and aren’t in the linked issue’s scope. A PR should do what its issue says and nothing else, so a reviewer can tell whether the stated requirement is met.]
- Responsibility and architecture concerns:
  - [Renaming any of the patient fields will impact Patient. This is from the domain layer and has nothing to do with cancelling appointments. Any code using the old field names will break. This also causes unrelated code to be restructured and causes unnecessary shifting of responsibility. We have introduced a new dependency which means everyone on the project must adapt and introduces more maintenance and security risks. This breaks the Stage 6 constraint of no new frameworks/ features. Cancellations should not be a large change to the service. We should still use the existing rule Appointment.cancel()]
- Testing and review concerns:
  - [A green test does not prove that the changes are safe. The tests may not have even been run on the renamed variables or refactored code. There are more lines to look at and these are not focused so it is more likely that there will be an actual issue with the cancel functionality missed by the reviewer. If any of the changes are incorrect then the whole PR will need to be rejected or rolled back. There is also no way to map each line changed to an acceptance criteria. The reviewer should ask for proof rather than ‘the tests passed’.]
- Changes to remove or separate, with reasons: 
  - Removing the rename of the patients field. This isn’t related to FR-06 and could cause issues with other code. If this is required it should be a separate issue, with tests and review.
  - Removing re-structuring of unrelated code. There is no requirement for doing this and can cause confusion as to what is actually changing. If this is justified then raise it as a separate issue.
  - Removing the addition of a new dependency. As there is nothing related to cancelling that requires this addition it needs to be agreed upon by the team and with guidance from the tutor.
  - Leaving the actual cancelling change and tests. Keeping the PR small and easily traceable back to the issue.


## D Challenge a weak Copilot review

GitHub Copilot says: "Looks good; tests pass."

- Missing evidence:
  - The comment doesn’t say which requirement or acceptance criteria were checked. It doesn’t name the tests that ran, the command, the directory or the code SHA, and “tests pass” doesn’t show that the tests assert the right behaviour. It doesn’t mention failure cases, scope, responsibility boundaries or the diff lines it looked at, and nothing shows it actually ran anything. Copilot’s statement is a claim, not evidence.
- Follow-up review question 1: 
  - Which issue and acceptance criteria did you check this diff against, and which changed lines satisfy each one?
- Follow-up review question 2: 
  - Which tests cover cancelling a COMPLETED appointment and cancelling twice, and what do they assert about the status afterwards? Please point to the assertions.
- Follow-up review question 3: 
  - Do the tests check that the returned object is the same stored object (identity) and that the appointment is still retrievable after cancellation, or only that no exception was raised?
- Follow-up review question 4: 
  - Does the diff contain any change outside the linked issue’s scope, such as renamed fields, restructured code or new dependencies? Please list each changed file and say why it’s needed.
- Follow-up review question 5: 
  - What exact command, in which directory and at which code SHA, produced “tests pass”, and were the original supplied tests included and passing?
- Additional questions if useful:
  - Does the service call Appointment.cancel() rather than setting the status directly, and which lines show that?
  - Which error cases (unknown ID, blank ID) are tested, and what exception does each raise?
  - Are there any behaviours you could not verify from the diff alone, and what would have to be checked by running the code?

## E Team workflow agreement

| Practice | Team agreement |
|---|--|
| Branch naming | One focused branch per issue, named by type, issue number and topic, for example feature/2-patient-lookup and feature/3-cancel-appointment. Nobody commits routine work directly to main. |
| Commit message convention | A short imperative message that says what changed, such as “Add patient lookup by ID”. One coherent step per commit, with no “changes” or “fix stuff”. |
| PR size | One issue per PR, containing only what the linked issue’s scope covers. No unrelated renames, restructuring or new dependencies. If the diff grows beyond the issue, split it. |
| Another-member review requirement | Every PR is reviewed by at least one member who didn’t write it. The reviewer reads the actual diff against the issue’s acceptance criteria and records their own observations before consulting Copilot. Self-review is only preparation. |
| Merge rule | Merge only after another member has approved, all feedback is resolved and rechecked, and the tests pass, including the supplied ones. The author doesn’t merge their own PR until the approval is on record. After merging, everyone pulls the updated main. |
| Significant Copilot disclosure rule | Any significant Copilot use (generating or changing code or tests, or reviewing a PR) is recorded in the evidence file’s Copilot section: what was asked, what it produced, how the human checked it, and the Accept, Modify or Reject decision. Trivial autocompletions don’t need recording. |

## F Issue and backlog index

Create at least two focused issues. Add a linked practitioner-lookup issue or an explicit supporting criterion with the tutor if needed to cover all three service targets.

| Issue link                                                 | Requirement | Owner                   | Acceptance criteria or precise link                                 | Status |
|------------------------------------------------------------|-|-------------------------|---------------------------------------------------------------------|--------|
| (https://github.com/linhvantran/st1-assignment-3/issues/1) | FR-02 Patient Search (PatientService.find_patient), plus practitioner lookup if you cover it here | Van Tran (@linhvantran) | Returns the same stored patient for a registered ID; raises LookupError for an unknown ID and ValueError for a blank or invalid ID; a lookup changes no stored data. | Open   |
| (https://github.com/linhvantran/st1-assignment-3/issues/2)                                                  | FR-06 Appointment Cancellation with FR-07 retained history (AppointmentService.cancel_appointment)| Van Tran (@linhvantran) | A SCHEDULED appointment becomes CANCELLED and the same stored object is returned and retained; unknown ID raises LookupError, blank or invalid ID raises ValueError, and repeated or COMPLETED cancellation raises ValueError with the status unchanged.                                                      | Open   |

## G Pull request evidence

Repeat this block per PR. Record actual events, not planned approvals.

- PR link and title: [response]
- Linked issue and requirement: [response]
- Feature branch: [response]
- Changed behaviour: [response]
- Meaningful commits: [links]
- Test command, directory and observed result: [response]
- Another-member reviewer: [response]
- Human observations recorded before Copilot: [link and time]
- Requirement, responsibilities, test assertions and unrelated-scope checks: [response]
- Key feedback: [response]
- Author response/change and verification: [response]
- Reviewer recheck and approval: [link]
- Merge outcome and SHA: [response]
- Significant Copilot assistance: [summary or none]
- Linked issue closure: [response]
- Each member updated main: [member and confirmation]
- Integrated verification after merge: [command, directory, result and code SHA]

## H Copilot collaboration record

Record meaningful required use, not every trivial completion. Repeat per significant interaction.

- Member and task: [response]
- Prompt/purpose and relevant issue/diff: [response]
- Summary of output: [response]
- Human check against actual code, requirements and tests: [response]
- Decision — Accept / Modify / Reject: [select]
- Reason: [response]
- Verification/evidence: [link and result]

## I Human versus Copilot review comparison

- Human reviewer noticed before consulting Copilot: [response]
- Copilot noticed: [response]
- Overlap: [response]
- What did the human reviewer notice that Copilot did not: [response]
- What did Copilot identify that the human reviewer initially missed: [response]
- Unsupported or incorrect Copilot suggestion: [response or none identified with explanation]
- Human judgement accepted, modified or rejected, and why: [response]
- Which evidence justified merge approval: [response]

## J Contributions

Repeat per member. Include only categories that describe actual work; write not applicable where appropriate. Pairing or mentoring can be supported by a short corroborated note.

- Member: [response]
- Implementation: [work and evidence]
- Testing: [work and evidence]
- Review: [work and evidence]
- Issue refinement: [work and evidence]
- Design and responsibility discussion: [work and evidence]
- Debugging or integration: [work and evidence]
- Documentation or team support: [work and evidence]

## K Exit question

Why is a high commit count not necessarily evidence of strong contribution?

The number of commits does not necessarily show how much progress has been made when contributing. Commits are very variable in terms of their size and contribution. One team member may have many small commits, for example fixing whitespace or a personal error, whilst another may have fewer but higher quality commits with good scope, and provide working and tested functionality. There can be significant contributions with few commits, for instance creating good issues and acceptance criteria, peer reviewing another team members PR with respect to the requirements, debugging, discussing design and responsibilities, and helping teammates understand the code. Within our team [insert real example here (e.g. I created FR-02 and FR-06/FR-07 issues and criteria, or helped review a team members PR and identified a missing test)]. The number of commits can be increased by someone developing a habit of committing or breaking up tasks into unnecessary sections. It should be taken into account what was actually in the commits, quality of testing and reviews, and evidence to demonstrate knowledge. Contribution can be better assessed by looking at what someone actually contributed.

## L Stage 6 formative questions

1. What is version control?

A record of changes made within a project. This can show who made the change, the reason for the change and allows comparisons between different versions. It also allows multiple people to work on the same piece of code.

2. Why is a feature branch useful?

Helps create a single focused change. This means that any incomplete or incorrect changes will not affect the stable version. Allows parallel working and can be reviewed and tested before being merged.

3. What makes a commit a good engineering commit?

A single focused change with a clear message stating what has been changed and why (e.g "Prevent completed appointments from being cancelled"). No unrelated changes have been made and can be traced back to an issue/requirement. This makes it easy to review and roll back.

4. What is a pull request?

A plan to merge the commits on one branch into another (typically the main branch). Shows diff, links to issue and tests, discussion and review occur here before merging.

5. What is the purpose of code review?

Makes sure that the change satisfies the requirements from an independent point of view. Ensures accountability by making sure that mistakes are handled properly. Also ensures that the test cases are making proper assertions and do not have any irrelevant scope. This helps to find defects early and also ensures that everyone on the team understands the code.

6. What does a Git diff show?

Precisely those lines that have been added, removed or altered between two branches (such as your working copy vs last commit, or a branch vs trunk). This tells you exactly what has changed.

7. What is a Definition of Done?

A common checklist for when a task is done. This could be: Acceptance criteria met, Meaningful tests passed, Checked by another member of the team, Feedback addressed and Documentation updated.

8. What is the appropriate role of GitHub Copilot in pull-request review?

Second opinion. This involves examining the observations made and documented by humans. The result of this is the assertion which must be verified against the requirements, the actual code and an observed test run. It is not evidence from the human, but it does provide an opinion.

9. Why should individual contribution not be judged only by commit count?

Commit size and value varies. Sometimes it's better to make a few great commits rather than lots of small, insignificant ones. Work such as reviews, tests, debugging, issue improvement, design discussions and mentoring won't result in many commits. It is the quality of your commits and showing that you understand what you are doing that matters most.

10. What is the Stage 6 engineering rule?

A requirement is then worked on via a single focused change, this includes: issues with acceptance criteria, creating a feature branch, implementing and testing, reviewed by another team member and merging into main. Services are used to control store and domain objects, without circumventing any domain rules. No code is merged based solely on passing tests.

## M Completion and handover

- Starting SHA: [response]
- Final Stage 6 code SHA: [response]
- Test command: [response]
- Working directory: [response]
- Observed result: [response]
- PR and another-member reviewer: [links]
- Unresolved issue or none: [response]
- Stage 7 handover status: [ready for tutor checkpoint / unresolved work]
- Final submitted SHA if later than tested SHA: [response and evidence-only difference]

- [ ] Three Stage 6 service targets completed and checked.
- [ ] Original supplied tests retained and passing.
- [ ] At least two focused issues link requirements and acceptance criteria.
- [ ] Feature work reviewed by another member using the actual diff.
- [ ] Human-first review and required Copilot comparison recorded.
- [ ] Feedback resolved and approval recorded before merge.
- [ ] Everyone pulled main and integrated checks passed.
- [ ] Required activities, quiz responses and contribution notes completed.
- [ ] Only synthetic data included; confidential peer material kept out.
- [ ] Tutor can trace a requirement through issue, code, tests, PR and checkpoint.

Do not write a file's own future commit SHA into that file. Record the tested code SHA first, then commit the evidence; explain the difference when submitting.
