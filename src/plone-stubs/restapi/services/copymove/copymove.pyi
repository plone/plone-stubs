from _typeshed import Incomplete
from plone.restapi.services import Service

class BaseCopyMove(Service):
    """Base service for copy/move operations."""

    portal: Incomplete
    portal_url: Incomplete
    catalog: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_object(self, key):
        """Get an object by url, path or UID."""
    def reply(self): ...
    def clipboard(self, parent, ids) -> None:
        """Get clipboard data"""

class Copy(BaseCopyMove):
    """Copies existing content objects."""

    is_moving: bool
    def clipboard(self, parent, ids): ...

class Move(BaseCopyMove):
    """Moves existing content objects."""

    is_moving: bool
    def clipboard(self, parent, ids): ...
