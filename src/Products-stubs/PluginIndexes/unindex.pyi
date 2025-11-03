from _typeshed import Incomplete
from collections.abc import Generator
from OFS.SimpleItem import SimpleItem

LOG: Incomplete

class UnIndex(SimpleItem):
    """Simple forward and reverse index."""

    zmi_icon: str
    operators: Incomplete
    useOperator: str
    query_options: Incomplete
    id: Incomplete
    ignore_ex: Incomplete
    call_methods: Incomplete
    indexed_attrs: Incomplete
    def __init__(
        self, id, ignore_ex=None, call_methods=None, extra=None, caller=None
    ) -> None:
        """Create an unindex

        UnIndexes are indexes that contain two index components, the
        forward index (like plain index objects) and an inverted
        index.  The inverted index is so that objects can be unindexed
        even when the old value of the object is not known.

        e.g.

        self._index = {datum:[documentId1, documentId2]}
        self._unindex = {documentId:datum}

        The arguments are:

          'id' -- the name of the item attribute to index.  This is
          either an attribute name or a record key.

          'ignore_ex' -- should be set to true if you want the index
          to ignore exceptions raised while indexing instead of
          propagating them.

          'call_methods' -- should be set to true if you want the index
          to call the attribute 'id' (note: 'id' should be callable!)
          You will also need to pass in an object in the index and
          unindex methods for this to work.

          'extra' -- a mapping object that keeps additional
          index-related parameters - subitem 'indexed_attrs'
          can be string with comma separated attribute names or
          a list

          'caller' -- reference to the calling object (usually
          a (Z)Catalog instance
        """
    def __len__(self) -> int: ...
    def getId(self): ...
    def clear(self) -> None: ...
    def __nonzero__(self): ...
    def histogram(self):
        """Return a mapping which provides a histogram of the number of
        elements found at each point in the index.
        """
    def referencedObjects(self):
        """Generate a list of IDs for which we have referenced objects."""
    def getEntryForObject(self, documentId, default=...):
        """Takes a document ID and returns all the information we have
        on that specific object.
        """
    def removeForwardIndexEntry(self, entry, documentId) -> None:
        """Take the entry provided and remove any reference to documentId
        in its entry in the index.
        """
    def insertForwardIndexEntry(self, entry, documentId) -> None:
        """Take the entry provided and put it in the correct place
        in the forward index.

        This will also deal with creating the entire row if necessary.
        """
    def index_object(self, documentId, obj, threshold=None):
        """wrapper to handle indexing of multiple attributes"""
    def getCounter(self):
        """Return a counter which is increased on index changes"""
    def numObjects(self):
        """Return the number of indexed objects."""
    def indexSize(self):
        """Return the size of the index in terms of distinct values."""
    def unindex_object(self, documentId) -> None:
        """Unindex the object with integer id 'documentId' and don't
        raise an exception if we fail
        """
    def getRequestCache(self):
        """returns dict for caching per request for interim results
        of an index search. Returns 'None' if no REQUEST attribute
        is available"""
    def getRequestCacheKey(self, record, resultset=None):
        """returns an unique key of a search record"""
    def query_index(self, record, resultset=None):
        """Search the index with the given IndexQuery object.

        If not `None`, the resultset argument
        indicates that the search result is relevant only on this set,
        i.e. everything outside resultset is of no importance.
        The index can use this information for optimizations.
        """
    def hasUniqueValuesFor(self, name):
        """has unique values for column name"""
    def getIndexSourceNames(self):
        """Return sequence of indexed attributes."""
    def getIndexQueryNames(self):
        """Indicate that this index applies to queries for the index's name."""
    def uniqueValues(self, name=None, withLengths: int = 0) -> Generator[Incomplete]:
        """returns the unique values for name

        if withLengths is true, returns a sequence of
        tuples of (value, length)
        """
    def keyForDocument(self, id): ...
    def documentToKeyMap(self): ...
    def items(self): ...
