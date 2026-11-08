# Stage08 Artefact 

This document is for B of the stage08 MD file. 

PS C:\Users\JohnDoe\st1-assignment-3> python C:\Users\JohnDoe\prepare_debugging.py project --check 
Stage 8 tool 1.1; preflight PASS; baseline SHA256 986c5445532ffd1d85e88639b6b6f34b84e15b2bbfc1882511a96938c3b641f6
Baseline Git SHA fb8f1c4b030ab05a838b74df4eddbd2d58f82364
CHECK ONLY: project unchanged; both proposed fault signatures verified in a temporary copy
PS C:\Users\JohnDoe\st1-assignment-3> python C:\Users\JohnDoe\prepare_debugging.py project --apply       
Stage 8 tool 1.1; preflight PASS; baseline SHA256 986c5445532ffd1d85e88639b6b6f34b84e15b2bbfc1882511a96938c3b641f6
Baseline Git SHA fb8f1c4b030ab05a838b74df4eddbd2d58f82364
PREPARED: F8-01 practitioner conflict; F8-02 retained-history lookup
Verified expected failures: test_f8_01_conflict; test_f8_02_history (2 failed)
Backup/hash recorded in .stage8_faults; use --restore for setup recoveryonly
PS C:\Users\JohnDoe\st1-assignment-3> python C:\Users\JohnDoe\prepare_debugging.py project --verify
VERIFIED: exactly 2 expected failures; both approved symptom signatures present
PS C:\Users\JohnDoe\st1-assignment-3> 

- I want you to know that this is not my directory btw. 