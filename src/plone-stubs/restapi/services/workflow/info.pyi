from _typeshed import Incomplete
from plone.restapi.services import Service

class WorkflowInfo:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, expand: bool = False): ...

class WorkflowInfoService(Service):
    """Get workflow information"""
    def reply(self): ...
