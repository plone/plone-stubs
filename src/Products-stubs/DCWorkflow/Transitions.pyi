from .ContainerTab import ContainerTab
from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

TRIGGER_AUTOMATIC: int
TRIGGER_USER_ACTION: int

class TransitionDefinition(SimpleItem):
    """Transition definition"""

    meta_type: str
    security: Incomplete
    title: str
    description: str
    new_state_id: str
    trigger_type = TRIGGER_USER_ACTION
    guard: Incomplete
    actbox_name: str
    actbox_url: str
    actbox_icon: str
    actbox_category: str
    var_exprs: Incomplete
    script_name: Incomplete
    after_script_name: Incomplete
    manage_options: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    def getId(self): ...
    def getGuardSummary(self): ...
    def getGuard(self): ...
    def getVarExprText(self, id): ...
    def getWorkflow(self): ...
    def getAvailableStateIds(self): ...
    def getAvailableScriptIds(self): ...
    def getAvailableVarIds(self): ...
    def manage_properties(self, REQUEST, manage_tabs_message=None):
        """ """
    def setProperties(
        self,
        title,
        new_state_id,
        trigger_type=...,
        script_name: str = "",
        after_script_name: str = "",
        actbox_name: str = "",
        actbox_url: str = "",
        actbox_category: str = "workflow",
        actbox_icon: str = "",
        props=None,
        REQUEST=None,
        description: str = "",
    ):
        """ """
    def manage_variables(self, REQUEST, manage_tabs_message=None):
        """ """
    def getVariableExprs(self):
        """get variable exprs for management UI"""
    def getWorkflowVariables(self):
        """get all variables that are available form
        workflow and not handled yet.
        """
    def addVariable(self, id, text, REQUEST=None):
        """
        Add a variable expression.
        """
    def deleteVariables(self, ids=[], REQUEST=None):
        """delete a WorkflowVariable from State"""
    def setVariables(self, ids=[], REQUEST=None):
        """set values for Variables set by this state"""

class Transitions(ContainerTab):
    """A container for transition definitions"""

    meta_type: str
    security: Incomplete
    all_meta_types: Incomplete
    def manage_main(self, REQUEST, manage_tabs_message=None):
        """ """
    def addTransition(self, id, REQUEST=None):
        """ """
    def deleteTransitions(self, ids, REQUEST=None):
        """ """
