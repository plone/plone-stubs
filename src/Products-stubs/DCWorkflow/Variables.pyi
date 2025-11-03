from .ContainerTab import ContainerTab
from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

class VariableDefinition(SimpleItem):
    """Variable definition"""

    meta_type: str
    security: Incomplete
    description: str
    for_catalog: int
    for_status: int
    default_value: str
    default_expr: Incomplete
    info_guard: Incomplete
    update_always: int
    manage_options: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    def getDefaultExprText(self): ...
    def getInfoGuard(self): ...
    def getInfoGuardSummary(self): ...
    def manage_properties(self, REQUEST, manage_tabs_message=None):
        """ """
    def setProperties(
        self,
        description,
        default_value: str = "",
        default_expr: str = "",
        for_catalog: int = 0,
        for_status: int = 0,
        update_always: int = 0,
        props=None,
        REQUEST=None,
    ):
        """ """

class Variables(ContainerTab):
    """A container for variable definitions"""

    meta_type: str
    all_meta_types: Incomplete
    def manage_main(self, REQUEST, manage_tabs_message=None):
        """ """
    def addVariable(self, id, REQUEST=None):
        """ """
    def deleteVariables(self, ids, REQUEST=None):
        """ """
    def getStateVar(self): ...
    def setStateVar(self, id, REQUEST=None):
        """ """
