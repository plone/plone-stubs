from _typeshed import Incomplete
from plone.restapi.services import Service

class ContentRulesAdd(Service):
    """Adds content rules"""

    params: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
