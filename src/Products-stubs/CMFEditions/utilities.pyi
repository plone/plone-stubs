from _typeshed import Incomplete
from Persistence import Persistent

STUB_OBJECT_PREFIX: str

class KwAsAttributes(Persistent):
    """Class attaching to itself passed keyword attributes."""

    __roles__: Incomplete
    def __init__(self, **kw) -> None: ...

def dereference(obj=None, history_id=None, zodb_hook=None):
    """Dereference an object.

    Works with either an obj or a history_id or both.

    If only a history_id is used, then a 'zodb_hook' is required to obtain
    the uid tool.

    Returns a tuple consisting of the derefrenced object and
    the unique id of the object: ``(obj, uid)``

    If an object or history_id cannot be found None will be returned for
    one or both values.
    """

def generateId(parent, prefix: str = "", volatile: bool = False):
    """Generate an unused id (optionally a volatile one)."""

def isObjectVersioned(obj):
    """Return true iff object has a version_id."""

def isObjectChanged(obj): ...
def maybeSaveVersion(
    obj, policy: str = "at_edit_autoversion", comment: str = "", force: bool = False
) -> None: ...
def wrap(obj, parent):
    """Copy the context and containment from one object to another.

    This is needed to allow acquiring attributes. Containment and context
    is setup only in direction to the parents but not from the parent
    to itself. So doing the following raises an ``AttributeError``::

        getattr(wrapped.aq_parent, tempAttribute)
    """
