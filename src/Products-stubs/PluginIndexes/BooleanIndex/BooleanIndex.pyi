from _typeshed import Incomplete
from collections.abc import Generator
from Products.PluginIndexes.unindex import UnIndex

LOG: Incomplete

class BooleanIndex(UnIndex):
    """Index for booleans

    self._index = set([documentId1, documentId2])
    self._unindex = {documentId:[True/False]}

    self._length is the length of the unindex
    self._index_length is the length of the index
    self._index_value is the indexed value

    The document ids in self._index have self._index_value as their value.

    Since there are only two possible values (True/False), the index
    only stores a forward index for the less common value.
    It starts off with the opposite of value of the first document
    and later checks and inverts itself, if more than 60% of all
    documents now have the indexed value. It does the inversion
    at 60% to avoid inverting itself constantly for an index that
    has a roughly equal 50/50 split.
    """

    meta_type: str
    manage_options: Incomplete
    query_options: Incomplete
    manage: Incomplete
    manage_main: Incomplete
    manage_browse: Incomplete
    def clear(self) -> None: ...
    def histogram(self):
        """Return a mapping which provides a histogram of the number of
        elements found at each point in the index.
        """
    def insertForwardIndexEntry(self, entry, documentId) -> None:
        """If the value matches the indexed one, insert into treeset"""
    def removeForwardIndexEntry(self, entry, documentId, check: bool = True) -> None:
        """Take the entry provided and remove any reference to documentId
        in its entry in the index.
        """
    def unindex_object(self, documentId) -> None:
        """Unindex the object with integer id 'documentId' and don't
        raise an exception if we fail
        """
    def query_index(self, record, resultset=None): ...
    def indexSize(self):
        """Return distinct values, as an optimization we always claim 2."""
    def items(self): ...
    def uniqueValues(self, name=None, withLengths: int = 0) -> Generator[Incomplete]:
        """returns the unique values for name

        if withLengths is true, returns a sequence of
        tuples of (value, length)
        """

manage_addBooleanIndexForm: Incomplete

def manage_addBooleanIndex(
    self, id, extra=None, REQUEST=None, RESPONSE=None, URL3=None
):
    """Add a boolean index"""
