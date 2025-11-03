from _typeshed import Incomplete
from plone.restapi.services import Service

class TypesDelete(Service):
    """Deletes a field/fieldset from content type"""

    params: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
