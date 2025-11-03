from _typeshed import Incomplete
from Acquisition import Explicit

class FormattedDateProvider(Explicit):
    template: Incomplete
    __parent__: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request, view) -> None: ...
    date_dict: Incomplete
    def __call__(self, occ):
        """Return a formatted date string.

        :param occ: An event or occurrence.
        :type occ: IEvent, IOccurrence or IEventAccessor based object
        :returns: Formatted date string for display.
        :rtype: string

        """

class FormattedStartDateProvider(FormattedDateProvider):
    template: Incomplete
