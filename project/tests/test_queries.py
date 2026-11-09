from datetime import datetime

from smartcare.domain import Appointment, Patient, Practitioner
from smartcare.queries import appointment_sort_key

NINE_AM = datetime(2026, 11, 10, 9, 0)
EIGHT_AM = datetime(2026, 11, 10, 8, 0)


def make_appointment(appointment_id, date_time=NINE_AM):
    """Build a synthetic appointment for the sort key tests."""
    patient = Patient('P1', 'Alice Example')
    practitioner = Practitioner('D1', 'Dr Sample', 'GP')
    return Appointment(appointment_id, patient, practitioner, date_time)


def test_sort_key_returns_date_time_and_appointment_id():
    appointment = make_appointment('A1')

    key = appointment_sort_key(appointment)

    assert key == (NINE_AM, 'A1')


def test_equal_time_appointments_sort_by_appointment_id():
    # Same time for both. A2 is created first, so a correct result
    # cannot come from the original order.
    a2 = make_appointment('A2')
    a1 = make_appointment('A1')

    result = sorted([a2, a1], key=appointment_sort_key)

    assert result == [a1, a2]


def test_sort_key_orders_by_time_before_id():
    # The later appointment has the smaller ID (A1). If the key sorted
    # by ID first, this test would fail.
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