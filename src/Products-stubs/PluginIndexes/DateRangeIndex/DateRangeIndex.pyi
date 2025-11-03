from _typeshed import Incomplete
from collections.abc import Generator
from Products.PluginIndexes.unindex import UnIndex

MAX32: Incomplete

class DateRangeIndex(UnIndex):
    """Index for date ranges, such as the "effective-expiration" range in CMF.

    Any object may return None for either the start or the end date: for the
    start date, this should be the logical equivalent of "since the beginning
    of time"; for the end date, "until the end of time".

    Therefore, divide the space of indexed objects into four containers:

    - Objects which always match (i.e., they returned None for both);

    - Objects which match after a given time (i.e., they returned None for the
      end date);

    - Objects which match until a given time (i.e., they returned None for the
      start date);

    - Objects which match only during a specific interval.
    """

    security: Incomplete
    meta_type: str
    query_options: Incomplete
    manage_options: Incomplete
    since_field: Incomplete
    until_field: Incomplete
    floor_value: int
    ceiling_value: int
    precision_value: int
    def __init__(
        self,
        id,
        since_field=None,
        until_field=None,
        caller=None,
        extra=None,
        floor_value=None,
        ceiling_value=None,
        precision_value=None,
    ) -> None: ...
    def getSinceField(self):
        """Get the name of the attribute indexed as start date."""
    def getUntilField(self):
        """Get the name of the attribute indexed as end date."""
    def getFloorValue(self):
        """ """
    def getCeilingValue(self):
        """ """
    def getPrecisionValue(self):
        """ """
    manage_indexProperties: Incomplete
    def manage_edit(
        self,
        since_field,
        until_field,
        floor_value,
        ceiling_value,
        precision_value,
        REQUEST,
    ) -> None:
        """ """
    def clear(self) -> None:
        """Start over fresh."""
    def getEntryForObject(self, documentId, default=None):
        """Get all information contained for the specific object
        identified by 'documentId'.  Return 'default' if not found.
        """
    def index_object(self, documentId, obj, threshold=None):
        """Index an object:
        - 'documentId' is the integer ID of the document
        - 'obj' is the object to be indexed
        - ignore threshold
        """
    def unindex_object(self, documentId) -> None:
        """Remove the object corresponding to 'documentId' from the index."""
    def uniqueValues(self, name=None, withLengths: int = 0) -> Generator[Incomplete]:
        """Return a sequence of unique values for 'name'.

        If 'withLengths' is true, return a sequence of tuples, in
        the form '(value, length)'.
        """
    def getRequestCacheKey(self, record, resultset=None): ...
    def query_index(self, record, resultset=None): ...

manage_addDateRangeIndexForm: Incomplete

def manage_addDateRangeIndex(
    self, id, extra=None, REQUEST=None, RESPONSE=None, URL3=None
):
    """Add a date range index to the catalog, using the incredibly icky
    double-indirection-which-hides-NOTHING.
    """
