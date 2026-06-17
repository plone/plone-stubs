from _typeshed import Incomplete
from zope.container.interfaces import IContainer
from zope.interface.common.sequence import IFiniteSequence
from zope.location.interfaces import IContained

class IKeyManager(IContainer):
    def clear(self, ring: str = "_system") -> None:
        """Clear all keys on a given ring. By default the system ring
        is cleader.  If None is used as ring id all rings are cleared.
        """
    def rotate(self, ring: str = "_system") -> None:
        """Rotate a given ring. By default rotates the system ring.
        If None is used as ring id all rings are rotated.
        """
    def secret(self, ring: str = "_system") -> None:
        """Return the current secret for a given ring. If no ring
        is given the secret for the system ring is returned"""

class IKeyring(IContained, IFiniteSequence):
    current: Incomplete
    def __init__(self, size: int = 5) -> None:
        """Construct a new keyring for a specified number of keys."""
    def clear(self) -> None:
        """Remove all keys from the ring."""
    def rotate(self) -> None:
        """Add a new secret to the ring, pushing out the oldest secret."""
