from _typeshed import Incomplete
from plone.restapi.services import Service

log: Incomplete

class PostRelations(Service):
    """Create new relations or rebuild relations."""

    params: Incomplete
    sm: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
