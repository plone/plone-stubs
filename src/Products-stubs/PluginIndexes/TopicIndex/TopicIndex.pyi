from _typeshed import Incomplete
from collections.abc import Generator
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent

LOG: Incomplete

class TopicIndex(Persistent, SimpleItem):
    """A TopicIndex maintains a set of FilteredSet objects.

    Every FilteredSet object consists of an expression and and IISet with all
    Ids of indexed objects that eval with this expression to 1.
    """

    meta_type: str
    zmi_icon: str
    operators: Incomplete
    useOperator: str
    query_options: Incomplete
    manage_options: Incomplete
    id: Incomplete
    filteredSets: Incomplete
    def __init__(self, id, caller=None) -> None: ...
    def getId(self): ...
    def clear(self) -> None: ...
    def index_object(self, docid, obj, threshold: int = 100):
        """hook for (Z)Catalog"""
    def unindex_object(self, docid):
        """hook for (Z)Catalog"""
    def numObjects(self):
        """Return the number of indexed objects."""
    def indexSize(self):
        """Return the size of the index in terms of distinct values."""
    def search(self, filter_id): ...
    def query_index(self, record, resultset=None):
        """Hook for (Z)Catalog
        \'record\' --  mapping type (usually {"topic": "..." }
        """
    def hasUniqueValuesFor(self, name):
        """has unique values for column name"""
    def uniqueValues(self, name=None, withLength: int = 0) -> Generator[Incomplete]:
        """Return an iterable/sequence of unique values for name.

        If 'withLengths' is true, returns a iterable/sequence of tuples of
        (value, length).
        """
    def getEntryForObject(self, docid, default=None):
        """Takes a document ID and returns all the information we have
        on that specific object.
        """
    def addFilteredSet(self, filter_id, typeFilteredSet, expr) -> None: ...
    def delFilteredSet(self, filter_id) -> None: ...
    def clearFilteredSet(self, filter_id) -> None: ...
    def manage_addFilteredSet(
        self, filter_id, typeFilteredSet, expr, URL1, REQUEST=None, RESPONSE=None
    ) -> None:
        """add a new filtered set"""
    def manage_delFilteredSet(
        self, filter_ids=[], URL1=None, REQUEST=None, RESPONSE=None
    ) -> None:
        """delete a list of FilteredSets"""
    def manage_saveFilteredSet(
        self, filter_id, expr, URL1=None, REQUEST=None, RESPONSE=None
    ) -> None:
        """save expression for a FilteredSet"""
    def getIndexSourceNames(self):
        """return names of indexed attributes"""
    def getIndexQueryNames(self): ...
    def manage_clearFilteredSet(
        self, filter_ids=[], URL1=None, REQUEST=None, RESPONSE=None
    ) -> None:
        """clear a list of FilteredSets"""
    manage: Incomplete
    manage_main: Incomplete
    editFilteredSet: Incomplete

manage_addTopicIndexForm: Incomplete

def manage_addTopicIndex(self, id, REQUEST=None, RESPONSE=None, URL3=None):
    """Add a TopicIndex"""
