from _typeshed import Incomplete
from zope.interface import Interface

class IPluggableIndex(Interface):
    def getId() -> None:
        """Return Id of index."""
    def getEntryForObject(documentId, default=None) -> None:
        """Get all information contained for 'documentId'."""
    def getIndexSourceNames() -> None:
        """Get a sequence of attribute names that are indexed by the index."""
    def getIndexQueryNames() -> None:
        """Get a sequence of query parameter names to which this index applies."""
    def index_object(documentId, obj, threshold=None) -> None:
        """Index an object.

        - ``documentId`` is the integer ID of the document.

        - ``obj`` is the object to be indexed.

        - ``threshold`` is the number of words to process between committing
          subtransactions.  If None, subtransactions are disabled.

        For each name in ``getIndexSourceNames``, try to get the named
        attribute from ``obj``.

        - If the object does not have the attribute, do not add it to the
          index for that name.

        - If the attribute is a callable, call it to get the value.  If
          calling it raises an AttributeError, do not add it to the index.
          for that name.
        """
    def unindex_object(documentId) -> None:
        """Remove the documentId from the index."""
    def numObjects() -> None:
        """Return the number of indexed objects."""
    def indexSize() -> None:
        """Return the size of the index in terms of distinct values."""
    def clear() -> None:
        """Empty the index"""

class ILimitedResultIndex(IPluggableIndex): ...

class IQueryIndex(IPluggableIndex):
    id: Incomplete
    operators: Incomplete
    useOperator: Incomplete
    query_options: Incomplete
    def query_index(record, resultset=None) -> None:
        """Same as _apply_index, but the query is already a pre-parsed
        IndexQuery object.
        """

class IUniqueValueIndex(IPluggableIndex):
    """An index which can return lists of unique values contained in it"""
    def hasUniqueValuesFor(name) -> None:
        """Return true if the index can return the unique values for name"""
    def uniqueValues(name=None, withLengths: int = 0) -> None:
        """Return an iterable/sequence of unique values for name.

        If 'withLengths' is true, returns a iterable/sequence of tuples of
        (value, length).
        """

class ISortIndex(IPluggableIndex):
    """An index which may be used to sort a set of document ids"""
    def keyForDocument(documentId) -> None:
        """Return the sort key that cooresponds to the specified document id

        This method is no longer used by ZCatalog, but is left for backwards
        compatibility."""
    def documentToKeyMap() -> None:
        """Return an object that supports __getitem__ and may be used to
        quickly lookup the sort key given a document id"""

class IDateIndex(Interface):
    """Index for dates."""

    index_naive_time_as_local: Incomplete

class IDateRangeIndex(Interface):
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
    def getSinceField() -> None:
        """Get the name of the attribute indexed as start date."""
    def getUntilField() -> None:
        """Get the name of the attribute indexed as end date."""

class IPathIndex(Interface):
    """Index for paths returned by getPhysicalPath.

    A path index stores all path components of the physical path of an object.

    Internal datastructure:

    - a physical path of an object is split into its components

    - every component is kept as a  key of a OOBTree in self._indexes

    - the value is a mapping 'level of the path component' to
      'all docids with this path component on this level'
    """
    def insertEntry(comp, id, level) -> None:
        """Insert an entry.

        This method is intended for use by subclasses:  it is not
        a normal API for the index.

        'comp' is an individual path component

        'id' is the docid

        .level'is the level of the component inside the path
        """

class IFilteredSet(Interface):
    """A pre-calculated result list based on an expression."""
    def getExpression() -> None:
        """Get the expression."""
    def getIds() -> None:
        """Get the IDs of all objects for which the expression is True."""
    def setExpression(expr) -> None:
        """Set the expression."""

class ITopicIndex(Interface):
    """A TopicIndex maintains a set of FilteredSet objects.

    Every FilteredSet object consists of an expression and and IISet with all
    Ids of indexed objects that eval with this expression to 1.
    """
    def addFilteredSet(filter_id, typeFilteredSet, expr) -> None:
        """Add a FilteredSet object."""
    def delFilteredSet(filter_id) -> None:
        """Delete the FilteredSet object specified by 'filter_id'."""
    def clearFilteredSet(filter_id) -> None:
        """Clear the FilteredSet object specified by 'filter_id'."""

class IIndexConfiguration(Interface):
    """Introspection API for pluggable indexes"""
    def getSettings(self) -> None:
        """Returns an mapping with index specific settings.
        E.g. {'indexed_attrs' : ('SearchableText', )}.
        The interface does not define any specifc mapping keys.
        """

class IRequestCacheIndex(Interface):
    """Request cache API for pluggable indexes"""
    def getRequestCache() -> None:
        """Returns dict for caching per request for interim results
        of an index search. Returns 'None' if no REQUEST attribute
        is available
        """
    def getRequestCacheKey(record, resultset=None) -> None:
        """Returns an unique key of a search record"""

class ITransposeQuery(Interface):
    """Optimization API for queries and indexing"""
    def make_query(query) -> None:
        """returns an optimized query for given index"""
    def getIndexNames() -> None:
        """returns index names that are optimized by index"""
