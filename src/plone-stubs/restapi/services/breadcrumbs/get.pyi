from _typeshed import Incomplete
from plone.restapi.services import Service

class Breadcrumbs:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, expand: bool = False): ...

class BreadcrumbsGet(Service):
    def reply(self): ...
