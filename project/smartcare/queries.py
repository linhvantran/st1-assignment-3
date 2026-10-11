"""Stage 9 contracts for pure collection processing."""


from datetime import datetime

from smartcare.domain import Appointment, AppointmentStatus


def appointment_sort_key(appointment: Appointment) -> tuple[datetime, str]:
    """Return the date/time and appointment ID ordering key without side
    effects.
    """
    raise NotImplementedError('Stage 9: named sorting key')


def select_appointments(
    appointments: list[Appointment],
    practitioner_id: str,
    status: AppointmentStatus | None = None,
) -> list[Appointment]:
    """Return a new list for this practitioner, optionally filtered by
    status.

    Order by date/time then appointment ID using appointment_sort_key.
    Do not mutate the source list/objects or perform input/output.
    """
    raise NotImplementedError('Stage 9: pure query')
