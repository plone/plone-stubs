from _typeshed import Incomplete
from plone.app.event.dx.interfaces import IDXEvent
from plone.app.event.dx.interfaces import IDXEventRecurrence
from plone.supermodel import model
from zope.interface import Invalid
from zope.interface import invariant

def first_weekday_sun0(): ...

class StartBeforeEnd(Invalid):
    __doc__: Incomplete

def default_start(context):
    """Provide default start for the form."""

def default_end(context):
    """Provide default end for the form."""

class IEventBasic(model.Schema, IDXEvent):
    """Basic event schema."""

    start: Incomplete
    end: Incomplete
    whole_day: Incomplete
    open_end: Incomplete
    sync_uid: Incomplete
    @invariant
    def validate_start_end(data) -> None: ...

class IEventRecurrence(model.Schema, IDXEventRecurrence):
    """Recurring Event Schema."""

    recurrence: Incomplete

class IEventLocation(model.Schema):
    """Event Location Schema."""

    location: Incomplete

class IEventAttendees(model.Schema):
    """Event Attendees Schema."""

    attendees: Incomplete

class IEventContact(model.Schema):
    """Event Contact Schema."""

    contact_name: Incomplete
    contact_email: Incomplete
    contact_phone: Incomplete
    event_url: Incomplete

def start_indexer(obj): ...
def end_indexer(obj): ...
def location_indexer(obj): ...
def sync_uid_indexer(obj): ...

class EventAccessor:
    """Generic event accessor adapter implementation for Dexterity content
    objects.
    """
    def __init__(self, context) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def __delattr__(self, name) -> None: ...
    @property
    def uid(self): ...
    @property
    def url(self):
        """need to lookup globalrequest in order to calculate
        correct URL during cached lookup (eg. in event portlet renderer)
        """
    @property
    def created(self): ...
    @property
    def duration(self): ...
    @property
    def start(self): ...
    @start.setter
    def start(self, value) -> None: ...
    @property
    def end(self): ...
    @end.setter
    def end(self, value) -> None: ...
    @property
    def timezone(self):
        """Returns the timezone name for the event. If the start timezone
        differs from the end timezone, it returns a tuple with
        (START_TIMEZONENAME, END_TIMEZONENAME).
        """
    @property
    def sync_uid(self): ...
    @property
    def title(self): ...
    @title.setter
    def title(self, value) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, value) -> None: ...
    @property
    def last_modified(self): ...
    @last_modified.setter
    def last_modified(self, value) -> None: ...
    @property
    def text(self): ...
    @text.setter
    def text(self, value) -> None: ...
