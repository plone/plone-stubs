from _typeshed import Incomplete
from collections.abc import Generator
from Products.PluginIndexes.unindex import UnIndex

logger: Incomplete

class UUIDIndex(UnIndex):
    """Index for uuid fields with an unique value per key.

    The internal structure is:

    self._index = {datum:documentId]}
    self._unindex = {documentId:datum}

    For each datum only one documentId can exist.
    """

    meta_type: str
    manage_options: Incomplete
    query_options: Incomplete
    manage: Incomplete
    manage_main: Incomplete
    manage_browse: Incomplete
    def clear(self) -> None: ...
    def numObjects(self):
        """Return the number of indexed objects. Since we have a 1:1 mapping
        from documents to values, we can reuse the stored length.
        """
    def uniqueValues(self, name=None, withLengths: int = 0) -> Generator[Incomplete]:
        """returns the unique values for name

        if withLengths is true, returns a sequence of
        tuples of (value, length)
        """
    def insertForwardIndexEntry(self, entry, documentId) -> None:
        """Take the entry provided and put it in the correct place
        in the forward index.
        """
    def removeForwardIndexEntry(self, entry, documentId) -> None:
        """Take the entry provided and remove any reference to documentId
        in its entry in the index.
        """

manage_addUUIDIndexForm: Incomplete

def manage_addUUIDIndex(self, id, extra=None, REQUEST=None, RESPONSE=None, URL3=None):
    """Add an uuid index"""
