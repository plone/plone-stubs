from _typeshed import Incomplete
from plone.restapi.services import Service

class ContentRulesGet(Service):
    """Publishes the content rules assigned or acquired by given context"""

    params: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
