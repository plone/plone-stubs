from .ContainerTab import ContainerTab
from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from OFS.SimpleItem import SimpleItem

class StateDefinition(SimpleItem):
    """State definition"""

    meta_type: str
    manage_options: Incomplete
    title: str
    description: str
    transitions: Incomplete
    permission_roles: Incomplete
    group_roles: Incomplete
    var_values: Incomplete
    security: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    def getId(self): ...
    def getWorkflow(self): ...
    def getTransitions(self): ...
    def getTransitionTitle(self, tid): ...
    def getAvailableTransitionIds(self): ...
    def getAvailableVarIds(self): ...
    def getManagedPermissions(self): ...
    def getAvailableRoles(self): ...
    def getPermissionInfo(self, p):
        """Returns the list of roles to be assigned to a permission."""
    def getGroupInfo(self, group):
        """Returns the list of roles to be assigned to a group."""
    def manage_properties(self, REQUEST, manage_tabs_message=None):
        """Show state properties ZMI form."""
    def setProperties(
        self, title: str = "", transitions=(), REQUEST=None, description: str = ""
    ):
        """Set the properties for this State."""
    def manage_variables(self, REQUEST, manage_tabs_message=None):
        """Show State variables ZMI form."""
    def getVariableValues(self):
        """Get VariableValues for management UI."""
    def getWorkflowVariables(self):
        """Get all variables that are available from the workflow and
        not handled yet.
        """
    def addVariable(self, id, value, REQUEST=None):
        """Add a WorkflowVariable to State."""
    def deleteVariables(self, ids=[], REQUEST=None):
        """Delete a WorkflowVariable from State."""
    def setVariables(self, ids=[], REQUEST=None):
        """Set values for Variables set by this State."""
    def manage_permissions(self, REQUEST, manage_tabs_message=None):
        """Present TTW UI for managing this State's permissions."""
    @postonly
    def setPermissions(self, REQUEST):
        """Set the permissions in REQUEST for this State."""
    @postonly
    def setPermission(self, permission, acquired, roles, REQUEST=None) -> None:
        """Set a permission for this State."""
    manage_groups: Incomplete
    @postonly
    def setGroups(self, REQUEST, RESPONSE=None) -> None:
        """Set the group to role mappings in REQUEST for this State."""

class States(ContainerTab):
    """A container for state definitions"""

    meta_type: str
    security: Incomplete
    all_meta_types: Incomplete
    def manage_main(self, REQUEST, manage_tabs_message=None):
        """ """
    def addState(self, id, REQUEST=None):
        """ """
    def deleteStates(self, ids, REQUEST=None):
        """ """
    def setInitialState(self, id=None, ids=None, REQUEST=None):
        """ """
