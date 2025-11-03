from _typeshed import Incomplete
from AccessControl.requestmethod import postonly

class WorkflowUIMixin:
    """ """

    security: Incomplete
    manage_properties: Incomplete
    manage_groups: Incomplete
    title: Incomplete
    description: Incomplete
    manager_bypass: Incomplete
    creation_guard: Incomplete
    @postonly
    def setProperties(
        self,
        title,
        manager_bypass: int = 0,
        props=None,
        REQUEST=None,
        description: str = "",
    ):
        """Sets basic properties."""
    def manage_permissions(self, REQUEST, manage_tabs_message=None):
        """Displays the form for choosing which permissions to manage."""
    permissions: Incomplete
    @postonly
    def addManagedPermission(self, p, REQUEST=None):
        """Adds to the list of permissions to manage."""
    @postonly
    def delManagedPermissions(self, ps, REQUEST=None):
        """Removes from the list of permissions to manage."""
    def getPossiblePermissions(self):
        """Returns the list of all permissions that can be managed."""
    def getGroups(self):
        """Returns the names of groups managed by this workflow."""
    def getAvailableGroups(self):
        """Returns a list of available group names."""
    groups: Incomplete
    @postonly
    def addGroup(self, group, RESPONSE=None, REQUEST=None) -> None:
        """Adds a group by name."""
    @postonly
    def delGroups(self, groups, RESPONSE=None, REQUEST=None) -> None:
        """Removes groups by name."""
    def getAvailableRoles(self):
        """Returns the acquired roles mixed with base_cms roles."""
    def getRoles(self):
        """Returns the list of roles managed by this workflow."""
    roles: Incomplete
    @postonly
    def setRoles(self, roles, RESPONSE=None, REQUEST=None) -> None:
        """Changes the list of roles mapped to groups by this workflow."""
    def getGuard(self):
        """Returns the initiation guard.

        If no init guard has been created, returns a temporary object.
        """
    @security.public
    def guardExprDocs(self):
        """Returns documentation on guard expressions."""
