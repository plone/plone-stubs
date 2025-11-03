from _typeshed import Incomplete
from collections.abc import Generator

MAXCOUNT: int

def recurrence_sequence_ical(
    start, recrule=None, from_=None, until=None, count=None, duration=None
) -> Generator[Incomplete, None, Incomplete]:
    """Calculates a sequence of datetime objects from a recurrence rule
    following the RFC2445 specification, using python-dateutil recurrence
    rules.  The resolution of the resulting datetime objects is one second,
    since python-dateutil rrulestr doesn't support microseconds.

    :param start:   datetime or DateTime instance of the date from which the
                    recurrence sequence is calculated.
    :type start: datetime.datetime

    :param recrule: Optional string with RFC2445 compatible recurrence
                    definition, dateutil.rrule or dateutil.rruleset instances.
    :type recrule: string

    :param from_:   Optional datetime or DateTime instance of the date, to
                    limit the result within a timespan.
    :type from_: datetime.datetime

    :param until:   Optional datetime or DateTime instance of the date, until
                    the recurrence is calculated. If not given, count or
                    MAXDATE limit the recurrence calculation.
    :type until: datetime.datetime

    :param count:   Optional integer which defines the number of occurrences.
                    If not given, until or MAXDATE limits the recurrence
                    calculation.
    :type count: integer

    :param duration: Optional timedelta instance, which is used to calculate
                     if a occurrence datetime plus duration is within the
                     queried timerange.
    :type duration:  datetime.timedelta

    :returns: A generator which generates a sequence of datetime instances.
    :rtype: generator

    """

def recurrence_sequence_timedelta(
    start, delta=None, until=None, count=None, dst=...
) -> Generator[Incomplete]:
    """Calculates a sequence of datetime objects from a timedelta integer,
    which defines the minutes between each occurrence.

    :param start: datetime or DateTime instance of the date from which the
                  recurrence sequence is calculated.
    :type start: datetime

    :param delta: Integer which defines the minutes
                  between each date occurrence.
    :type delta: integer

    :param until: datetime or DateTime instance of the date, until the
                  recurrence is calculated. If not given,
                  count or MAXDATE limit the recurrence calculation.
    :type until: datetime

    :param count: Integer which defines the number of occurrences. If not given,
                  until or MAXDATE limits the recurrence calculation.
    :param count: integer

    :param dst:   Daylight Saving Time crossing behavior. DSTAUTO, DSTADJUST or
                  DSTKEEP. For more information, see
                  plone.event.utils.utcoffset_normalize.
    :param dst: string

    :return: A generator which generates a sequence of datetime instances.
    :rtype: generator

    """

def recurrence_int_sequence(sequence) -> Generator[Incomplete]:
    """Generates a sequence of integer representations from a sequence of
    dateime instances.

    :param sequence: An iterable sequence of datetime instances.
    :type sequence: iterable
    :returns: Generator of integer representations of datetime instances.
    :rtype: generator

    """
