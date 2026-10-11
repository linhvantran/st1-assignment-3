# Software Technology 1 Assignment 3

One group repository and one evolving SmartCare application.
Baseline: Stage 6 foundation, 2026 revision 2. This starter deliberately leaves the three Stage 6 service tasks incomplete.

## Group index

- Group and tutorial: [complete]
- Member names, GitHub usernames and UG/PG cohorts: [complete]
- Shared repository URL: [complete]
- Latest completed stage: [complete]
- Verified code SHA: [complete]
- Test command, working directory and observed result: [complete]
- Final submitted SHA, if different from tested code SHA: [complete; explain evidence-only changes]

Do not put student IDs, private peer ratings, credentials or personal contact details here.

## Complete package and stage sequence

All Assignment 3 ordinary materials are supplied at the beginning: the Overview, Git/GitHub Group Guide, Stage 6–12 handouts, this incomplete SmartCare starter, all seven blank activity/evidence records, and assessment instructions/forms. Stage numbers control the engineering sequence, not document availability.

Start with Stage 6. Complete each stage only after the previous applicable stage has been integrated, verified and recorded.

UG: 6 → 7 → 8 → 9 → 12

PG: 6 → 7 → 8 → 9 → 10 → 11 → 12

Use ONE group repository and ONE evolving project/ throughout. The stage folders contain your response/evidence records; all templates are already present. Preserve previous code, tests, records and Git history. Never replace project/ with another starter or copy completed staff reference implementations: those are private staff material.

Stages 10 and 11 are PG-only. UG skipping these stages is correct and complete. In an UG-only submission, retain the supplied PG-only templates unchanged as intentionally not applicable; do not fill them with fabricated N/A responses. Optional UG collaboration is voluntary and unassessed. Mixed groups protect the verified common Stage 9 SHA while PG extends the same project. Use only the teaching team's confirmed Copilot agent capability or approved equivalent route.

The Stage 8 preparation utility version 1.1 is a controlled teaching asset supplied or run by teaching staff when Stage 8 begins. Follow the instructions provided by your tutor. It is not included in the normal student package. If temporarily supplied for the handout commands, keep it in a sibling Stage_8_Assets/ folder outside the repository. Never include it in Git or the final submission. The Stage 7 checkpoint and Stage 8 technical activity are unchanged.

Complete the supplied Stage 12 record when you reach Stage 12. UG releases the common scope; PG releases the extended scope, protecting the common SHA where needed. Record exact tested/submitted SHAs and create one source ZIP as the handout directs, without duplicate application copies per stage.

## Application and evidence

- [Application setup and commands](project/README.md)
- [Stage 6 activities and evidence](stage06/stage06_activities_and_evidence.md)
- [Stage 7 activities and evidence](stage07/stage07_activities_and_evidence.md)
- [Stage 8 activities and evidence](stage08/stage08_activities_and_evidence.md)
- [Stage 9 activities and evidence](stage09/stage09_activities_and_evidence.md)
- [Stage 10 PG activities and evidence](stage10_pg/stage10_activities_and_evidence.md)
- [Stage 11 PG activities and evidence](stage11_pg/stage11_activities_and_evidence.md)
- [Stage 12 activities and evidence](stage12/stage12_activities_and_evidence.md)

Git commands in the practical guide run from this root. Application commands run from project/:

```sh
cd project
python main.py
python -m pytest
cd ..
```

Use the approved environment described in the Git/GitHub group guide. The verified baseline is Python 3.13 with pytest 8.3.5. GitHub Copilot is the nominated assistant; verify significant output and record required decisions. Use synthetic data only. Use each supplied record only when you reach that stage in the applicable sequence.
