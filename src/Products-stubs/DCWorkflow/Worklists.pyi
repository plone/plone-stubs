from .ContainerTab import ContainerTab
from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

tales_re: Incomplete

class WorklistDefinition(SimpleItem):
    """Worklist definiton"""

    meta_type: str
    security: Incomplete
    description: str
    var_matches: Incomplete
    actbox_name: str
    actbox_url: str
    actbox_icon: str
    actbox_category: str
    guard: Incomplete
    manage_options: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    def getGuard(self): ...
    def getGuardSummary(self): ...
    def getWorkflow(self): ...
    def getAvailableCatalogVars(self): ...
    def getVarMatchKeys(self): ...
    def getVarMatch(self, id): ...
    def getVarMatchText(self, id): ...
    def manage_properties(self, REQUEST, manage_tabs_message=None):
        """ """
    def setProperties(
        self,
        description,
        actbox_name: str = "",
        actbox_url: str = "",
        actbox_category: str = "global",
        actbox_icon: str = "",
        props=None,
        REQUEST=None,
    ):
        """ """
    def search(self, info=None, **kw):
        """Perform the search corresponding to this worklist

        Returns sequence of ZCatalog brains
        - info is a mapping for resolving formatted string variable references
        - additional keyword/value pairs may be used to restrict the query
        """

class Worklists(ContainerTab):
    """A container for worklist definitions"""

    meta_type: str
    security: Incomplete
    all_meta_types: Incomplete
    def manage_main(self, REQUEST, manage_tabs_message=None):
        """ """
    def addWorklist(self, id, REQUEST=None):
        """ """
    def deleteWorklists(self, ids, REQUEST=None):
        """ """
