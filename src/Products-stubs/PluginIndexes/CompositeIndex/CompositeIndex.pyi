from _typeshed import Incomplete
from Persistence import PersistentMapping
from Products.PluginIndexes.KeywordIndex.KeywordIndex import KeywordIndex

LOG: Incomplete
QUERY_OPTIONS: Incomplete
QUERY_OPERATORS: Incomplete
MIN_COMPONENTS: int

def tuple_cast(kw): ...
def collect(recs, not_cid=None): ...

class ComponentMapping(PersistentMapping):
    """A persistent wrapper for mapping objects
    recording the order in which items are added."""
    def __init__(self, *args, **kwargs) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __setitem__(self, key, item) -> None: ...
    def clear(self) -> None: ...
    def copy(self): ...
    def items(self): ...
    def keys(self): ...
    def popitem(self): ...
    def setdefault(self, key, failobj=None): ...
    def update(self, d) -> None: ...
    def values(self): ...

class Component:
    def __init__(self, id, meta_type, attributes) -> None: ...
    @property
    def id(self): ...
    @property
    def meta_type(self): ...
    @property
    def attributes(self): ...
    @property
    def rawAttributes(self): ...

class CompositeIndex(KeywordIndex):
    """Index for composition of simple fields.
    or sequences of items
    """

    meta_type: str
    manage_options: Incomplete
    query_options: Incomplete
    id: Incomplete
    ignore_ex: Incomplete
    call_methods: Incomplete
    def __init__(
        self, id, ignore_ex=None, call_methods=None, extra=None, caller=None
    ) -> None:
        """Create an composite index"""
    def getIndexComponents(self):
        """return sequence of indexed attributes"""
    def getComponentIndexNames(self):
        """returns component index names to composite"""
    def getComponentIndexAttributes(self):
        """returns list of attributes of each component index to composite"""
    def getIndexNames(self):
        """returns index names that are caught by query substitution"""
    def make_query(self, query):
        """optimize the query for supported index names"""
    def addComponent(self, c_id, c_meta_type, c_attributes) -> None: ...
    def delComponent(self, c_id) -> None: ...
    def saveComponents(self, components) -> None: ...
    def manage_addComponent(
        self, c_id, c_meta_type, c_attributes, URL1, REQUEST=None, RESPONSE=None
    ) -> None:
        """add a new component"""
    def manage_delComponents(
        self, del_ids=(), URL1=None, REQUEST=None, RESPONSE=None
    ) -> None:
        """delete one or more components"""
    def manage_saveComponents(
        self, components, URL1=None, REQUEST=None, RESPONSE=None
    ) -> None:
        """save values of components"""
    def fastBuild(self, threshold=None) -> None: ...
    def manage_fastBuild(
        self, threshold=None, URL1=None, REQUEST=None, RESPONSE=None
    ) -> None:
        """fast build index directly via catalog brains and attribute values
        of matching field and keyword indexes"""
    manage: Incomplete
    manage_main: Incomplete
    manage_browse: Incomplete

manage_addCompositeIndexForm: Incomplete

def manage_addCompositeIndex(
    self, id, extra=None, REQUEST=None, RESPONSE=None, URL3=None
):
    """Add a composite index"""
