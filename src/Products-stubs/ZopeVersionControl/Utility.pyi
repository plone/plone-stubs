from _typeshed import Incomplete
from Persistence import Persistent

use_vc_permission: str

def isAVersionableResource(obj):
    """True if an object is versionable.

    To qualify, the object must be persistent (have its own db record), and
    must not have an true attribute named '__non_versionable__'."""

class VersionInfo(Persistent):
    """A VersionInfo object contains bookkeeping information for version
    controlled objects. The bookkeeping information can be read (but
    not changed) by restricted code."""

    __allow_access_to_unprotected_subobjects__: int
    timestamp: Incomplete
    history_id: Incomplete
    version_id: Incomplete
    status: Incomplete
    user_id: Incomplete
    def __init__(self, history_id, version_id, status) -> None: ...
    sticky: Incomplete
    CHECKED_OUT: int
    CHECKED_IN: int
    def branchName(self): ...
    def clone(self, clear_sticky: int = 0): ...

class ReadOnlyJar:
    """A read-only ZODB connection-like object that prevents changes."""

    __base__: Incomplete
    def __init__(self, base) -> None: ...
    def __getattr__(self, name): ...
    def commit(*args, **kw) -> None: ...
    def abort(*args, **kw) -> None: ...

class VersionControlError(Exception): ...
