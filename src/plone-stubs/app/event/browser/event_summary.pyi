from _typeshed import Incomplete
from plone.memoize import view
from Products.Five.browser import BrowserView

class EventSummaryView(BrowserView):
    context: Incomplete
    request: Incomplete
    data: Incomplete
    max_occurrences: int
    excludes: Incomplete
    def __init__(self, context, request) -> None: ...
    @property
    def is_occurrence(self): ...
    @property
    def event_context(self): ...
    def formatted_date(self, occ): ...
    @property
    @view.memoize
    def next_occurrences(self):
        """Returns occurrences for this context, except the start
        occurrence, limited to self.max_occurrence occurrences.

        :returns: List with next occurrences.
        :rtype: list
        """
    @property
    @view.memoize
    def num_more_occurrences(self):
        """Return the number of extra occurrences, which are not listed by
        next_occurrences.
        """
    @property
    def more_occurrences_text(self): ...
    @property
    @view.memoize
    def has_occurrences(self): ...
