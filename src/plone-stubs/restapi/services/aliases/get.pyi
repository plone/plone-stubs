from _typeshed import Incomplete
from plone.restapi.services import Service

class Aliases:
    """@aliases"""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def reply_item(self): ...
    def reply_root(self):
        """
        redirect-to - target
        path        - path
        redirect    - full path with root
        """
    def reply_root_csv(self): ...
    def __call__(self, expand: bool = False): ...

class AliasesGet(Service):
    """Get aliases"""
    def reply(self): ...
    def render(self): ...

def deroot_path(path):
    """Remove the portal root from alias"""
