from _typeshed import Incomplete
from zope.interface import Interface

class IRegisterMultiPlugin(Interface):
    """Register profiles with the global registry."""

    class_: Incomplete
    meta_type: Incomplete

def registerMultiPlugin(_context, class_=None, meta_type=None) -> None:
    """Add a new meta_type to the registry."""

def cleanUp() -> None: ...
