# SmartCare Stage 6 starter

Requirements baseline: SmartCare A3 2026 revision 2. Python 3.13 and pytest 8.3.5 verified. Runtime uses only the standard library.

From this directory, using a Python environment with the development dependency installed:

```sh
python main.py
python -m pytest
```

If needed in your approved environment: `python -m pip install -r requirements-dev.txt`.

The demo registers synthetic records and books/finds an appointment. All supplied tests pass. Data exists only in this session and is lost on exit; FR-10 restart persistence is retired. Use synthetic information only.

`domain.py` contains the entities, status and guarded cancellation. `data_store.py` holds three dictionaries through add/find/list methods. The three services share that object. Supplied registration, booking, appointment lookup and conflict checking work. IDs are trimmed, non-blank and case-sensitive. Properties provide read-only identity/appointment state; changes go through domain methods. No special architecture terminology is required.

Stage 6 TODOs: service patient/practitioner lookup and cancellation. Stage 9 TODOs: pure query, named sort key, service listing and interactive menu. The starter TODO contracts are in docstrings. All three Stage 6 TODO calls deliberately raise NotImplementedError; future TODOs remain stubs. No PG rescheduling or assurance solution is supplied.

Service booking accepts IDs and a `datetime` (local, minute precision). Console parser accepts exactly `YYYY-MM-DD HH:MM`. Store lookups return None when absent; service lookups raise LookupError. Invalid values, duplicates, conflicts and illegal transitions raise ValueError. Lists are new containers holding the stored objects. No age, duration, patient-conflict or past-date rules apply.
