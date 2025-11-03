from _typeshed import Incomplete
from collections.abc import Generator
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent

LOG: Incomplete

class PathIndex(Persistent, SimpleItem):
    """Index for paths returned by getPhysicalPath.

    A path index stores all path components of the physical path of an object.

    Internal datastructure:

    - a physical path of an object is split into its components

    - every component is kept as a  key of a OOBTree in self._indexes

    - the value is a mapping 'level of the path component' to
      'all docids with this path component on this level'
    """

    meta_type: str
    zmi_icon: str
    operators: Incomplete
    useOperator: str
    query_options: Incomplete
    manage_options: Incomplete
    id: Incomplete
    def __init__(self, id, caller=None) -> None: ...
    def __len__(self) -> int: ...
    def getEntryForObject(self, docid, default=None):
        """See IPluggableIndex."""
    def getIndexSourceNames(self):
        """See IPluggableIndex."""
    def getIndexQueryNames(self): ...
    def index_object(self, docid, obj, threshold: int = 100):
        """See IPluggableIndex."""
    def unindex_object(self, docid) -> None:
        """See IPluggableIndex."""
    def query_index(self, record, resultset=None):
        """See IPluggableIndex.

        o Unpacks record from catalog and map onto '_search'.
        """
    def numObjects(self):
        """See IPluggableIndex."""
    def indexSize(self):
        """See IPluggableIndex."""
    def clear(self) -> None:
        """See IPluggableIndex."""
    def hasUniqueValuesFor(self, name):
        """See IUniqueValueIndex."""
    def uniqueValues(self, name=None, withLengths: int = 0) -> Generator[Incomplete]:
        """See IUniqueValueIndex."""
    def keyForDocument(self, documentId):
        """See ISortIndex."""
    def documentToKeyMap(self):
        """See ISortIndex."""
    def insertEntry(self, comp, id, level) -> None:
        """See IPathIndex"""
    manage: Incomplete
    manage_main: Incomplete

manage_addPathIndexForm: Incomplete

def manage_addPathIndex(self, id, REQUEST=None, RESPONSE=None, URL3=None):
    """Add a path index"""
