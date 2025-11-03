from _typeshed import Incomplete
from zope.interface import Interface

class IResourceDirectoryDirective(Interface):
    """Register resource directories with the global registry."""

    directory: Incomplete
    name: Incomplete
    type: Incomplete

def registerResourceDirectory(_context, directory, name=None, type=None) -> None:
    """
    Register a new resource directory.

    The actual ZCA registrations are deferred so that conflicts can be resolved
    via zope.configuration's discriminator machinery.
    """
