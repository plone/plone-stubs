from _typeshed import Incomplete
from DateTime import DateTime

DEFAULT_END_DELTA: int
FALLBACK_TIMEZONE: str
SYNC_NONE: int
SYNC_KEEP_NEWER: int
SYNC_KEEP_MINE: int
SYNC_KEEP_THEIRS: int
RET_MODE_BRAINS: int
RET_MODE_OBJECTS: int
RET_MODE_ACCESSORS: int
replacement_zones: Incomplete

def get_events(
    context,
    start=None,
    end=None,
    limit=None,
    ret_mode=...,
    expand: bool = False,
    sort: str = "start",
    sort_reverse: bool = False,
    **kw,
):
    """Return all events as catalog brains, possibly within a given
    timeframe.

    :param context: [required] A context object.
    :type context: Content object

    :param start: Date, from which on events should be searched.
    :type start: Python datetime.

    :param end: Date, until which events should be searched.
    :type end: Python datetime

    :param limit: Number of items to be returned.
    :type limit: integer

    :param ret_mode: Return type of search results. These options are
                     available:

                         * 1 (brains): Return results as catalog brains.
                         * 2 (objects): Return results as IEvent and/or
                                        IOccurrence objects.
                         * 3 (accessors): Return results as IEventAccessor
                                          wrapper objects.
    :type ret_mode: integer [1|2|3]

    :param expand: Expand the results to all occurrences (within a timeframe,
                   if given). With this option set to True, the resultset also
                   includes the event's recurrence occurrences and is sorted by
                   the start date.
                   Only available in ret_mode 2 (objects) and 3 (accessors).
    :type expand: boolean

    :param sort: Catalog index id to sort on.
    :type sort: string

    :param sort_reverse: Change the order of the sorting.
    :type sort_reverse: boolean

    :returns: Portal events, matching the search criteria.
    :rtype: catalog brains, event objects or IEventAccessor object wrapper,
            depending on ret_mode.
    """

def filter_and_resort(context, brains, start, end, sort, sort_reverse):
    """#114 sorting bug is fallout from a Products.DateRecurringIndex
    limitation. The index contains a set of start and end dates
    represented as integer: that allows valid slicing of searches.
    However the returned brains have a .start attribute which is
    the start DateTime of the *first* occurrence of an event.

    This results in mis-sorting of search results if the next occurrence
    of event B is after the next occurrence of event A, but the first
    occurrence of event B is *before* the first occurrence of event A.
    The catalog results sort that as B<A instead of A<B.

    This method works around that issue by extracting all occurrence
    start/end from the index, and then sorting on the actual next start/end.

    For ongoing events which have an occurrence starting in the past
    but ending in the future, the past start of that ongoing occurrence
    is selected, so this will show up right at the start of the result.

    :param context: [required] A context object.
    :type context: Content object

    :param brains: [required] catalog brains
    :type brains: catalog brains

    :param start: [required] min end datetime (sic!)
    :type start: Python datetime.

    :param end: [required] max start datetime (sic!)
    :type start: Python datetime.

    :param sort_reverse: Change the order of the sorting.
    :type sort_reverse: boolean

    :param sort: Which field to sort on
    :type sort: 'start' or 'end'

    :returns: catalog brains
    :rtype: catalog brains

    """

def expand_events(events, ret_mode, start=None, end=None, sort=None, sort_reverse=None):
    """Expand to the recurrence occurrences of a given set of events.

    :param events: IEvent based objects or IEventAccessor object wrapper.

    :param ret_mode: Return type of search results. These options are
                     available:

                         * 2 (objects): Return results as IEvent and/or
                                        IOccurrence objects.
                         * 3 (accessors): Return results as IEventAccessor
                                          wrapper objects.
                     Option "1" (brains) is not supported.

    :type ret_mode: integer [2|3]

    :param start: Date, from which on events should be expanded.
    :type start: Python datetime.

    :param end: Date, until which events should be expanded.
    :type end: Python datetime

    :param sort: Object or IEventAccessor Attribute to sort on.
    :type sort: string

    :param sort_reverse: Change the order of the sorting.
    :type sort_reverse: boolean
    """

def construct_calendar(events, start=None, end=None):
    """Return a dictionary with dates in a given timeframe as keys and the
    actual occurrences for that date for building calendars.
    Long lasting events will occur on every day until their end.

    :param events: List of IEvent and/or IOccurrence objects, to construct a
                   calendar data structure from.
    :type events: list

    :param start: An optional start range date.
    :type start: Python datetime or date

    :param end: An optional start range date.
    :type end: Python datetime or date

    :returns: Dictionary with isoformat date strings as keys and event
              occurrences as values.
    :rtype: dict

    """

def start_end_query(start, end):
    """Make a catalog query out of start and end dates."""

def default_timezone(context=None, as_tzinfo: bool = False):
    """Return the timezone from the portal or user.

    :param context: Optional context. If not given, the current Site is used.
    :type context: Content object

    :param as_tzinfo: Return the default timezone as tzinfo object.
    :type as_tzinfo: boolean

    :returns: Timezone identifier or tzinfo object.
    :rtype: string or tzinfo object

    """

def localized_now(context=None):
    """Return the current datetime localized to the default timezone.

    :param context: Context object.
    :type context: Content object
    :returns: Localized current datetime.
    :rtype: Python datetime

    """

def localized_today(context=None):
    """Return the current date localized to the default timezone.

    :param context: Context object.
    :type context: Content object
    :returns: Localized current date.
    :rtype: Python date

    """

def first_weekday():
    """Returns the number of the first Weekday in a Week, as defined in
    the registry. 0 is Monday, 6 is Sunday, as expected by Python's datetime.

    PLEASE NOTE: strftime %w interprets 0 as Sunday unlike the calendar module!

    :returns: Index of first weekday [0(Monday)..6(Sunday)]
    :rtype: integer

    """

def wkday_to_mon0(day):
    """Converts an integer weekday number to a representation where Monday is 0
    and Sunday is 6 (the datetime default), from a representation where Sunday
    is 0, Monday is 1 and Saturday is 6 (the strftime behavior).

    :param day: The weekday number [0(Sunday)..6]
    :type day: integer

    :returns: The weekday number [0(Monday)..6]
    :rtype: integer

    """

def wkday_to_mon1(day):
    """Converts an integer weekday number to a representation where Monday is
    1, Saturday is 6 and Sunday is 0 (the strftime behavior), from a
    representation where Monday is 0 and Sunday is 6 (the datetime default).

    :param day: The weekday number [0(Monday)..6]
    :type day: integer

    :returns: The weekday number [0(Sunday)..6]
    :rtype: integer

    """

def DT(dt, exact: bool = False):
    """Return a Zope DateTime instance from a Python datetime instance.

    :param dt: Python datetime, Python date, Zope DateTime instance or string.
    :param exact: If True, the resolution goes down to microseconds. If False,
                  the resolution are seconds. Default is False.
    :type exact: Boolean
    :returns: Zope DateTime
    :rtype: Zope DateTime

    """

def guess_date_from(datestr, context=None):
    """Returns a timezone aware date object if an arbitrary ASCII string is
    formatted in an ISO date format, otherwise None is returned.

    Used for traversing and Occurrence ids.

    :param datestr: Date string in an ISO format.
    :type datestr: string
    :param context: Context object (for retrieving the timezone).
    :type context: Content object
    :returns: Localized date object.
    :rtype: Python date

    """

def dt_start_of_day(dt):
    """Returns a Python datetime instance set to the start time of the given
    day (00:00:00).

    :param dt: datetime to set to the start time of the day.
    :type dt: Python datetime
    :returns: datetime set to the start time of the day (00:00:00).
    :rtype: Python datetime

    """

def dt_end_of_day(dt):
    """Returns a Python datetime instance set to the end time of the given day
    (23:59:59).

    :param dt: datetime to set to the end time of the day.
    :type dt: Python datetime
    :returns: datetime set to the end time of the day (23:59:59).
    :rtype: Python datetime

    """

def start_end_from_mode(mode, dt=None, context=None):
    """Return a start and end date from a given mode string, like
    "today", "past" or "future". This can be used in event retrieval
    functions.

    :param mode: One of the following modes:

                    \'all\' Show all events.
                    \'past\': Show only past events with descending sorting.
                    \'future\': Show only future events (default).
                    \'today\': Show todays events.
                    \'now\': Show todays upcoming events.
                    \'7days\': Show events until 7 days in future.
                    \'day\': Return all events on the given day (dt parameter
                           required)
                    \'week\': Show a weeks events, optionally from a given date.

                 These settings override the start and end parameters.

                 Not implemented yet:

                    \'month\': Show this month\'s events.

    :type mode: string

    :param dt: Optional datetime for day mode.
    :type dt: Python datetime

    """

def dates_for_display(occurrence):
    """Return a dictionary containing pre-calculated information for building
    <start>-<end> date strings.

    Keys are:
        'start_date' - date string of the start date
        'start_time' - time string of the start date
        'end_date'   - date string of the end date
        'end_time'   - time string of the end date
        'start_iso'  - start date in iso format
        'end_iso'    - end date in iso format
        'same_day'   - event ends on the same day
        'same_time'  - event ends at same time
        'whole_day'  - whole day events
        'open_end'   - events without end time

    :param occurrence: Event or occurrence object.
    :type occurrence: IEvent, IOccurrence or IEventAccessor based object.
    :returns: Dictionary with date strings.
    :rtype: dict


    The behavior os ulocalized_time() with time_only is odd.
    Setting time_only=False should return the date part only and *not*
    the time

    NOTE: these tests are not run, but serve as documentation.
    TODO: remove.
    >>> from DateTime import DateTime
    >>> start = DateTime(2010,3,16,14,40)
    >>> from zope.component.hooks import getSite
    >>> site = getSite()
    >>> ulocalized_time(start, False,  time_only=True, context=site)
    u'14:40'
    >>> ulocalized_time(start, False,  time_only=False, context=site)
    u'14:40'
    >>> ulocalized_time(start, False,  time_only=None, context=site)
    u'16.03.2010'

    """

def date_speller(context, dt): ...
def spell_date(dt, translation_context=None):
    """Return a dictionary with localized and readable formatted date parts."""

def default_start(context=None):
    """Return the default start as python datetime for prefilling forms.

    :returns: Default start datetime.
    :rtype: Python datetime

    """

def default_end(context=None):
    """Return the default end as python datetime for prefilling forms.

    :returns: Default end datetime.
    :rtype: Python datetime

    """

class AnnotationAdapter:
    """Abstract Base Class for an annotation storage.

    If the annotation wasn't set, it won't be created until the first attempt
    to set a property on this adapter.
    So, the context doesn't get polluted with annotations by accident.

    """

    ANNOTATION_KEY: Incomplete
    context: Incomplete
    def __init__(self, context) -> None: ...
    def __setattr__(self, name, value) -> None: ...
    def __getattr__(self, name): ...

def find_context(
    context, viewname=None, iface=None, as_url: bool = False, append_view: bool = True
):
    """Find the next context with a given view name or interface, up in the
    content tree, starting from the given context. This might not be the
    IPloneSiteRoot, but another subsite.

    :param context: The context to start the search from.
    :param viewname: (optional) The name of a view which a context should have
                     configured as defaultView.
    :param iface: (optional) The interface, the context to search for should
                  implement.
    :param as_url: (optional) Return the URL of the context found.
    :param append_view: (optional) In case of a given viewname and called with
                        as_url, append the viewname to the url, if the context
                        hasn't configured it as defaultView. Otherwise ignore
                        this parameter.
    :returns: A context with the given view name, interface or ISite root.
    """

def find_site(context, as_url: bool = False): ...
def find_ploneroot(context, as_url: bool = False): ...
def find_navroot(context, as_url: bool = False): ...
def find_event_listing(context, as_url: bool = False): ...

class PatchedDateTime(DateTime):
    def strftime(self, fmt): ...

def ulocalized_time(time, *args, **kwargs):
    """Corrects for DateTime bugs doing wrong thing with timezones"""
