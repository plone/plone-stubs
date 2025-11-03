from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

logger: Incomplete

def traverse(base, path):
    """simplified fast unrestricted traverse.
    base: the app-root to start from
    path: absolute path from app root as string
    returns: content at the end or None
    """

class StubIndex(SimpleItem):
    """stub catalog index doing nothing"""

    id: Incomplete
    def __init__(self, id, *args, **kw) -> None: ...
    def getId(self): ...
    def getEntryForObject(self, *args, **kw): ...
    def getIndexSourceNames(self): ...
    def index_object(self, *args, **kw): ...
    def unindex_object(self, *args, **kw) -> None: ...
    def numObjects(self): ...
    def clear(self) -> None: ...

class GopipIndex(StubIndex):
    """fake index for sorting against `getObjPositionInParent`"""

    meta_type: str
    manage_options: Incomplete
    keyForDocument: int
    catalog: Incomplete
    def __init__(self, id, extra=None, caller=None) -> None: ...
    def __len__(self) -> int: ...
    def documentToKeyMap(self): ...

manage_addGopipForm: Incomplete

def manage_addGopipIndex(self, identifier, REQUEST=None, RESPONSE=None, URL3=None):
    """add a fake gopip index"""
