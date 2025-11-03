from _typeshed import Incomplete
from plone.restapi.services import Service

logger: Incomplete

class AddonsPost(Service):
    """Performs install/upgrade/uninstall functions on an addon."""

    params: Incomplete
    errors: Incomplete
    addons: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
