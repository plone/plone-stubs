from _typeshed import Incomplete
from zope.interface import Interface

class IEvent(Interface):
    """Event type marker interface."""

class IEventRecurrence(Interface):
    """Event type marker interface for events with an RFC5545 compatible
    recurrence definition.

    """

class IOccurrence(Interface):
    """Marker interface for an occurrence item, which represents a single
    occurrence.

    """

    start: Incomplete
    end: Incomplete

class ICalendarAccessor(Interface):
    """Generic calendar accessor adapter interface.

    A calendar is a collection of calendar components, like events.

    """

    uid: Incomplete
    title: Incomplete
    description: Incomplete
    timezone: Incomplete
    def items(self) -> None:
        """Return a list of calendar component items, like events."""

class IEventAccessor(Interface):
    """Event type generic accessor adapter interface.

    A specific adapter implementation should be provided by the individual
    content type packages.

    """

    uid: Incomplete
    created: Incomplete
    duration: Incomplete
    url: Incomplete
    last_modified: Incomplete
    title: Incomplete
    description: Incomplete
    start: Incomplete
    end: Incomplete
    whole_day: Incomplete
    open_end: Incomplete
    timezone: Incomplete
    recurrence: Incomplete
    location: Incomplete
    attendees: Incomplete
    contact_name: Incomplete
    contact_email: Incomplete
    contact_phone: Incomplete
    event_url: Incomplete
    subjects: Incomplete
    text: Incomplete

class IRecurrenceSupport(Interface):
    """Event type recurrence adapter."""
    def occurrences(self, range_start, range_end) -> None:
        """Return a list of IOccurrence objects with custom attributes of the
        specific occurrence set.

        :param range_start: Search for occurrences after this date.
        :type range_start: Python datetime.

        :param range_end: Search for occurrences before this date.
        :type range_end: Python datetime.

        """

class IICalendar(Interface):
    """Adapter, which is used to construct an icalendar object."""

class IICalendarEventComponent(Interface):
    """Adapter, which is used to construct an event component object for
    icalendar.

    """

class IVEvent(Interface):
    """RFC5545 Event schema

    ; The following are REQUIRED,
    ; but MUST NOT occur more than once.
    ;
    dtstamp / uid /
    ;
    ; The following is REQUIRED if the component
    ; appears in an iCalendar object that doesn\'t
    ; specify the "METHOD" property; otherwise, it
    ; is OPTIONAL; in any case, it MUST NOT occur
    ; more than once.
    ;
    dtstart /
    ;
    ; The following are OPTIONAL,
    ; but MUST NOT occur more than once.
    ;
    class / created / description / geo /
    last-mod / location / organizer / priority /
    seq / status / summary / transp /
    url / recurid /
    ;
    ; The following is OPTIONAL,
    ; but SHOULD NOT occur more than once.
    ;
    rrule /
    ;
    ; Either \'dtend\' or \'duration\' MAY appear in
    ; a \'eventprop\', but \'dtend\' and \'duration\'
    ; MUST NOT occur in the same \'eventprop\'.
    ;
    dtend / duration /
    ;
    ; The following are OPTIONAL,
    ; and MAY occur more than once.
    ;
    attach / attendee / categories / comment /
    contact / exdate / rstatus / related /
    resources / rdate / x-prop / iana-prop

    """

    dtstart: Incomplete
    dtend: Incomplete
    duration: Incomplete
    rrule: Incomplete
    description: Incomplete
    location: Incomplete
    summary: Incomplete
    url: Incomplete
    attendee: Incomplete
    categories: Incomplete
    contact: Incomplete
    exdate: Incomplete
    rdate: Incomplete
    dtstamp: Incomplete
    uid: Incomplete
    klass: Incomplete
    created: Incomplete
    geo: Incomplete
    last_mod: Incomplete
    organizer: Incomplete
    priority: Incomplete
    seq: Incomplete
    status: Incomplete
    transp: Incomplete
    recurid: Incomplete
    attach: Incomplete
    comment: Incomplete
    rstatus: Incomplete
    related: Incomplete
    resources: Incomplete
    x_prop: Incomplete
    iana_prop: Incomplete
