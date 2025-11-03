from _typeshed import Incomplete
from plone.restapi.services import Service

class AddonsGet(Service):
    params: Incomplete
    addons: Incomplete
    query: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
