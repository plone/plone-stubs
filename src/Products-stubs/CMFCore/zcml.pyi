from _typeshed import Incomplete
from zope.interface import Interface

class IRegisterDirectoryDirective(Interface):
    """Register directories with the global registry."""

    name: Incomplete
    directory: Incomplete
    recursive: Incomplete
    ignore: Incomplete

def registerDirectory(
    _context, name, directory=None, recursive: bool = False, ignore=...
) -> None:
    """Add a new directory to the registry."""

def cleanUp() -> None: ...
