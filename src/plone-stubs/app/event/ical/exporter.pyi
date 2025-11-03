from _typeshed import Incomplete
from zope.publisher.browser import BrowserView

PRODID: str
VERSION: str

def construct_icalendar(context, events):
    """Returns an icalendar.Calendar object.

    :param context: A content object, which is used for calendar details like
                    Title and Description. Usually a container, collection or
                    the event itself.

    :param events: The list of event objects, which are included in this
                   calendar.
    """

def add_to_zones_map(tzmap, tzid, dt):
    """Build a dictionary of timezone information from a timezone identifier
    and a date/time object for which the timezone information should be
    calculated.

    :param tzmap: An existing dictionary of timezone information to be extended
                  or an empty dictionary.
    :type tzmap: dictionary
    :param tzid: A timezone identifier.
    :type tzid: string
    :param dt: A datetime object.
    :type dt: datetime

    :returns: A dictionary with timezone information needed to build VTIMEZONE
              entries.
    :rtype: dictionary
    """

def calendar_from_event(context):
    """Event adapter. Returns an icalendar.Calendar object from an Event
    context.
    """

def calendar_from_container(context):
    """Container adapter. Returns an icalendar.Calendar object from a
    Containerish context like a Folder.
    """

def calendar_from_collection(context):
    """Container/Event adapter. Returns an icalendar.Calendar object from a
    Collection.
    """

class ICalendarEventComponent:
    """Returns an icalendar object of the event."""

    context: Incomplete
    event: Incomplete
    ical: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def dtstamp(self): ...
    @property
    def created(self): ...
    @property
    def last_modified(self): ...
    @property
    def uid(self): ...
    @property
    def url(self): ...
    @property
    def summary(self): ...
    @property
    def description(self): ...
    @property
    def dtstart(self): ...
    @property
    def dtend(self): ...
    @property
    def recurrence(self): ...
    @property
    def location(self): ...
    @property
    def attendee(self): ...
    @property
    def contact(self): ...
    @property
    def categories(self): ...
    @property
    def geo(self) -> None:
        """Not implemented."""
    def ical_add(self, prop, val) -> None: ...
    def to_ical(self): ...

class EventsICal(BrowserView):
    """Returns events in iCal format."""
    def get_ical_string(self): ...
    def __call__(self) -> None: ...
