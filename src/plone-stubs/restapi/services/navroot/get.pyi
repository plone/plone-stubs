from _typeshed import Incomplete
from plone.restapi.services import Service

class Navroot:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, expand: bool = False): ...

class NavrootGet(Service):
    def reply(self): ...
