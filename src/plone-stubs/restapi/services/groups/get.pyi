from _typeshed import Incomplete
from plone.restapi.services import Service

DEFAULT_SEARCH_RESULTS_LIMIT: int

class GroupsGet(Service):
    params: Incomplete
    query: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
