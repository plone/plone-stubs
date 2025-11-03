from _typeshed import Incomplete
from plone.restapi.services import Service

logger: Incomplete

class AliasesPost(Service):
    """Creates new aliases"""
    def reply(self): ...
    def edit_for_navigation_root(self, alias): ...

class AliasesRootPost(Service):
    """Creates new aliases via controlpanel"""
    def reply(self): ...
