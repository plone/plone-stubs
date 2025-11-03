from _typeshed import Incomplete
from collections.abc import Generator
from OFS.SimpleItem import SimpleItem
from Products.Five.browser import BrowserView
from ZPublisher.BaseRequest import DefaultPublishTraverse

class RecurrenceSupport:
    """IRecurrenceSupport Adapter."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def occurrences(
        self, range_start=None, range_end=None
    ) -> Generator[Incomplete, None, Incomplete]:
        """Return all occurrences of an event, possibly within a start and end
        limit.

        :param range_start: Optional start datetime, from which you want
                            occurrences be returned.
        :type range_start: Python datetime
        :param range_end: Optional start datetime, from which you want
                          occurrences be returned.
        :type range_end: Python datetime
        :returns: List of occurrences, including the start event.
        :rtype: IEvent or IOccurrence based objects

        Please note: Events beginning before range_start but ending afterwards
                     won't be found.

        TODO: really?

        TODO: test with event start = 21st feb, event end = start+36h,
        recurring for 10 days, range_start = 1st mar, range_end = last Mark
        """

class OccurrenceTraverser(DefaultPublishTraverse):
    """Generic Occurrence traverser.

    Please note: the .at and .dx subpackages implement their own Occurrence
    traversers.
    """
    def publishTraverse(self, request, name): ...
    def fallbackTraverse(self, request, name): ...

class Occurrence(SimpleItem):
    """Transient Occurrence object, representing an individual event in a
    recurrecne set.
    """

    id: Incomplete
    start: Incomplete
    end: Incomplete
    portal_type: str
    def __init__(self, id, start, end) -> None: ...

class EventOccurrenceAccessor:
    """Generic event accessor adapter implementation for Occurrence objects."""
    def __init__(self, context) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...
    def __delattr__(self, name) -> None: ...
    @property
    def url(self): ...

class ImageScalingViewFactory(BrowserView):
    """Factory for ImageScaling view for Occurrences.
    Delegates to parent @@images view.
    """
    def __new__(cls, context, request): ...
