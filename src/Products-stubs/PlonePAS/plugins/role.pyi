from _typeshed import Incomplete
from Products.PluggableAuthService.plugins.ZODBRoleManager import ZODBRoleManager

def manage_addGroupAwareRoleManager(self, id, title: str = "", RESPONSE=None) -> None:
    """
    this is a doc string
    """

manage_addGroupAwareRoleManagerForm: Incomplete

class GroupAwareRoleManager(ZODBRoleManager):
    meta_type: str
    security: Incomplete
    def updateRolesList(self) -> None: ...
    def manage_afterAdd(self, item, container) -> None: ...
    def assignRoleToPrincipal(self, role_id, principal_id, REQUEST=None): ...
    def assignRolesToPrincipal(self, roles, principal_id, REQUEST=None) -> None:
        """Assign a specific set of roles, and only those roles, to a
        principal.

        o no return value

        o Raise KeyError if a role_id is unknown.
        """
    assignRolesToPrincipal: Incomplete
    @security.private
    def getRolesForPrincipal(self, principal, request=None):
        """See IRolesPlugin."""
    def allowRoleAssign(self, user_id, role_id):
        """True iff this plugin will allow assigning a certain user a
        certain role.

        Note that at least currently this only checks if the role_id
        exists.  If it exists, this method returns True.  Nothing is
        done with the user_id parameter.  This might be wrong.  See
        http://dev.plone.org/plone/ticket/7762
        """
    def listRoleIds(self): ...
    def listRoleInfo(self): ...
    def getRoleInfo(self, role_id): ...
