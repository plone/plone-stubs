from _typeshed import Incomplete
from plone.restapi.services import Service

class TypesPost(Service):
    """Creates a new field/fieldset"""

    params: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
