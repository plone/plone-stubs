from _typeshed import Incomplete
from Products.PluginIndexes.PathIndex.PathIndex import PathIndex

logger: Incomplete

class ExtendedPathIndex(PathIndex):
    """A path index stores all path components of the physical path of an
    object.

    Internal datastructure (regular pathindex):

    - a physical path of an object is split into its components

    - every component is kept as a key of a OOBTree in self._indexes

    - the value is a mapping 'level of the path component' to
      'all docids with this path component on this level'

    In addition

    - there is a terminator (None) signifying the last component in the path

    - 2 additional indexes map absolute path to either the doc id or doc ids of
      contained objects. This allows for rapid answering of common queries.
    """

    meta_type: str
    manage_options: Incomplete
    indexed_attrs: Incomplete
    multi_valued: bool
    query_options: Incomplete
    def __init__(self, id, extra=None, caller=None) -> None:
        """ExtendedPathIndex supports indexed_attrs"""
    def clear(self) -> None: ...
    def index_object(self, docid, obj, threshold: int = 100):
        """hook for (Z)Catalog"""
    def unindex_object(self, docid, _old=...) -> None:
        """hook for (Z)Catalog"""
    def search(
        self,
        path,
        default_level: int = 0,
        depth: int = -1,
        navtree: int = 0,
        navtree_start: int = 0,
        resultset=None,
    ):
        """
        path is either a string representing a relative URL or a part of a
        relative URL or a tuple (path, level).

        default_level specifies the level to use when no more specific level
        has been passed in with the path.

        level >= 0  starts searching at the given level
        level <  0  finds matches at *any* level

        depth let's you limit the results to items at most depth levels deeper
        than the matched path. depth == 0 means no subitems are included at
        all, with depth == 1 only direct children are included, etc.
        depth == -1, the default, returns all children at any depth.

        navtree is treated as a boolean; if it evaluates to True, not only the
        query match is returned, but also each container in the path. If depth
        is greater than 0, also all siblings of those containers, as well as
        the siblings of the match are included as well, plus *all* documents at
        the starting level.

        navtree_start limits what containers are included in a navtree search.
        If greater than 0, only containers (and possibly their siblings) at
        that level and up will be included in the resultset.

        """
    def query_index(self, record, resultset=None): ...
    def getIndexSourceNames(self):
        """return names of indexed attributes"""

manage_addExtendedPathIndexForm: Incomplete

def manage_addExtendedPathIndex(
    self, id, extra=None, REQUEST=None, RESPONSE=None, URL3=None
):
    """Add an extended path index"""
