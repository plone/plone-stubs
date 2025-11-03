from _typeshed import Incomplete
from Acquisition import Explicit
from Persistence import Persistent

class Guard(Persistent, Explicit):
    permissions: Incomplete
    roles: Incomplete
    groups: Incomplete
    expr: Incomplete
    security: Incomplete
    guardForm: Incomplete
    def check(self, sm, wf_def, ob, **kw):
        """Checks conditions in this guard."""
    def getSummary(self): ...
    def changeFromProperties(self, props):
        """
        Returns 1 if changes were specified.
        """
    def getPermissionsText(self): ...
    def getRolesText(self): ...
    def getGroupsText(self): ...
    def getExprText(self): ...

def formatNameUnion(names): ...
