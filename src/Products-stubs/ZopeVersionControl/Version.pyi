from _typeshed import Incomplete
from Acquisition import Implicit
from Persistence import Persistent

def cloneByPickle(obj, ignore_list=()):
    """Makes a copy of a ZODB object, loading ghosts as needed.

    Ignores specified objects along the way, replacing them with None
    in the copy.
    """

class Version(Implicit, Persistent):
    """A Version is a resource that contains a copy of a particular state
    (content and dead properties) of a version-controlled resource.  A
    version is created by checking in a checked-out resource. The state
    of a version of a version-controlled resource never changes."""

    id: Incomplete
    date_created: Incomplete
    def __init__(self, version_id, obj) -> None: ...
    branch: str
    prev: Incomplete
    next: Incomplete
    security: Incomplete
    @security.public
    def getId(self): ...
    @security.private
    def saveState(self, obj) -> None:
        """Save the state of object as the state for this version of
        a version-controlled resource."""
    @security.private
    def copyState(self):
        """Return an independent deep copy of the state of the version."""
    @security.private
    def stateCopy(self, obj, container):
        """Get a deep copy of the state of an object.

        Breaks any database identity references.
        """
