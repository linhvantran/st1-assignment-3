from datetime import datetime

from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)
from smartcare.queries import appointment_sort_key, select_appointments

EIGHT_AM = datetime(2026, 11, 10, 8, 0)
NINE_AM = datetime(2026, 11, 10, 9, 0)
TEN_AM = datetime(2026, 11, 10, 10, 0)


def make_appointment(
    appointment_id,
    date_time=NINE_AM,
    practitioner_id='D1',
    status=AppointmentStatus.SCHEDULED,
):
    """Build a synthetic appointment for the query tests."""
    patient = Patient('P1', 'Alice Example')
    practitioner = Practitioner(practitioner_id, 'Dr Sample', 'GP')
    return Appointment(
        appointment_id, patient, practitioner, date_time, status
    )


def test_sort_key_returns_date_time_and_appointment_id():
    appointment = make_appointment('A1')

    key = appointment_sort_key(appointment)

    assert key == (NINE_AM, 'A1')


def test_equal_time_appointments_sort_by_appointment_id():
    a2 = make_appointment('A2')
    a1 = make_appointment('A1')

    result = sorted([a2, a1], key=appointment_sort_key)

    assert result == [a1, a2]


def test_sort_key_orders_by_time_before_id():
    later = make_appointment('A1', NINE_AM)
    earlier = make_appointment('A2', EIGHT_AM)

    result = sorted([later, earlier], key=appointment_sort_key)

    assert result == [earlier, later]


def test_sort_key_does_not_change_the_appointment():
    appointment = make_appointment('A1')
    appointment_id = appointment.appointment_id
    date_time = appointment.date_time
    status = appointment.status
    patient = appointment.patient
    practitioner = appointment.practitioner

    appointment_sort_key(appointment)

    assert appointment.appointment_id == appointment_id
    assert appointment.date_time == date_time
    assert appointment.status is status
    assert appointment.patient is patient
    assert appointment.practitioner is practitioner


def test_select_returns_only_requested_practitioner():
    mine = make_appointment('A1', NINE_AM, 'D1')
    other = make_appointment('A2', NINE_AM, 'D2')

    result = select_appointments([mine, other], 'D1')

    assert result == [mine]


def test_select_without_status_returns_every_status():
    scheduled = make_appointment('A1', EIGHT_AM)
    cancelled = make_appointment(
        'A2', NINE_AM, status=AppointmentStatus.CANCELLED
    )
    completed = make_appointment(
        'A3', TEN_AM, status=AppointmentStatus.COMPLETED
    )

    result = select_appointments([completed, cancelled, scheduled], 'D1')

    assert result == [scheduled, cancelled, completed]


def test_select_with_status_returns_only_that_status():
    scheduled = make_appointment('A1', EIGHT_AM)
    cancelled = make_appointment(
        'A2', NINE_AM, status=AppointmentStatus.CANCELLED
    )
    appointments = [scheduled, cancelled]

    only_cancelled = select_appointments(
        appointments, 'D1', AppointmentStatus.CANCELLED
    )
    only_scheduled = select_appointments(
        appointments, 'D1', AppointmentStatus.SCHEDULED
    )

    assert only_cancelled == [cancelled]
    assert only_scheduled == [scheduled]


def test_select_returns_empty_list_when_nothing_matches():
    scheduled = make_appointment('A1')

    unknown_practitioner = select_appointments([scheduled], 'D9')
    no_matching_status = select_appointments(
        [scheduled], 'D1', AppointmentStatus.COMPLETED
    )

    assert unknown_practitioner == []
    assert no_matching_status == []


def test_select_orders_equal_time_appointments_by_id():
    a2 = make_appointment('A2')
    a1 = make_appointment('A1')

    result = select_appointments([a2, a1], 'D1')

    assert result == [a1, a2]


def test_select_returns_new_list_and_leaves_source_unchanged():
    a2 = make_appointment('A2', NINE_AM)
    a1 = make_appointment('A1', EIGHT_AM)
    source = [a2, a1]

    result = select_appointments(source, 'D1')

    assert result is not source
    assert source[0] is a2 and source[1] is a1
    assert result[0] is a1 and result[1] is a2
    assert a1.status is AppointmentStatus.SCHEDULED
    assert a2.date_time == NINE_AM


def test_select_repeated_calls_give_same_result():
    a2 = make_appointment('A2', NINE_AM)
    a1 = make_appointment('A1', EIGHT_AM)
    appointments = [a2, a1]

    first = select_appointments(appointments, 'D1')
    second = select_appointments(appointments, 'D1')

    assert first == second
    assert first is not second


def test_select_returns_fresh_list_for_empty_sorted_and_unsorted_input():
    a1 = make_appointment('A1', EIGHT_AM)
    a2 = make_appointment('A2', NINE_AM)
    inputs = [[], [a1, a2], [a2, a1]]

    for source in inputs:
        result = select_appointments(source, 'D1')

        assert result is not source
        assert result == sorted(source, key=appointment_sort_key)