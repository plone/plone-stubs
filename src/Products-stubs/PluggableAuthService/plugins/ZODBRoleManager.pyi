from ..plugins.BasePlugin import BasePlugin
from ..utils import csrf_only
from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from zope.interface import Interface

LOG: Incomplete

class MultiplePrincipalError(Exception): ...

class IZODBRoleManager(Interface):
    """Marker interface."""

manage_addZODBRoleManagerForm: Incomplete

def addZODBRoleManager(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add a ZODBRoleManager to a Pluggable Auth Service."""

class ZODBRoleManager(BasePlugin):
    """PAS plugin for managing roles in the ZODB."""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    def manage_afterAdd(self, item, container) -> None: ...
    @security.private
    def getRolesForPrincipal(self, principal, request=None):
        """See IRolesPlugin."""
    @security.private
    def enumerateRoles(
        self, id=None, exact_match: bool = False, sort_by=None, max_results=None, **kw
    ):
        """See IRoleEnumerationPlugin."""
    @security.private
    def doAssignRoleToPrincipal(self, principal_id, role): ...
    @security.private
    def doRemoveRoleFromPrincipal(self, principal_id, role): ...
    def listRoleIds(self):
        """Return a list of the role IDs managed by this object."""
    def listRoleInfo(self):
        """Return a list of the role mappings."""
    def getRoleInfo(self, role_id):
        """Return a role mapping."""
    @security.private
    def addRole(self, role_id, title: str = "", description: str = "") -> None:
        """Add 'role_id' to the list of roles managed by this object.

        o Raise KeyError on duplicate.
        """
    @security.private
    def updateRole(self, role_id, title, description) -> None:
        """Update title and description for the role.

        o Raise KeyError if not found.
        """
    @security.private
    def removeRole(self, role_id, REQUEST=None) -> None:
        """Remove 'role_id' from the list of roles managed by this object.

        o Raise KeyError if not found.

        Note that if you really want to remove a role you should first
        remove it from the roles in the root of the site (at the
        bottom of the Security tab at manage_access).
        """
    def listAvailablePrincipals(self, role_id, search_id):
        """Return a list of principal IDs to whom a role can be assigned.

        o If supplied, 'search_id' constrains the principal IDs;  if not,
          return empty list.

        o Omit principals with existing assignments.
        """
    def listAssignedPrincipals(self, role_id):
        """Return a list of principal IDs to whom a role is assigned."""
    @security.private
    def assignRoleToPrincipal(self, role_id, principal_id):
        """Assign a role to a principal (user or group).

        o Return a boolean indicating whether a new assignment was created.

        o Raise KeyError if 'role_id' is unknown.
        """
    @security.private
    def removeRoleFromPrincipal(self, role_id, principal_id):
        """Remove a role from a principal (user or group).

        o Return a boolean indicating whether the role was already present.

        o Raise KeyError if 'role_id' is unknown.

        o Ignore requests to remove a role not already assigned to the
          principal.
        """
    manage_options: Incomplete
    manage_roles: Incomplete
    manage_twoLists: Incomplete
    @csrf_only
    @postonly
    def manage_addRole(
        self, role_id, title, description, RESPONSE=None, REQUEST=None
    ) -> None:
        """Add a role via the ZMI."""
    @csrf_only
    @postonly
    def manage_updateRole(
        self, role_id, title, description, RESPONSE=None, REQUEST=None
    ) -> None:
        """Update a role via the ZMI."""
    @csrf_only
    @postonly
    def manage_removeRoles(self, role_ids, RESPONSE=None, REQUEST=None) -> None:
        """Remove one or more role assignments via the ZMI.

        Note that if you really want to remove a role you should first
        remove it from the roles in the root of the site (at the
        bottom of the Security tab at manage_access).
        """
    @csrf_only
    @postonly
    def manage_assignRoleToPrincipals(
        self, role_id, principal_ids, RESPONSE, REQUEST=None
    ) -> None:
        """Assign a role to one or more principals via the ZMI."""
    @csrf_only
    @postonly
    def manage_removeRoleFromPrincipals(
        self, role_id, principal_ids, RESPONSE=None, REQUEST=None
    ) -> None:
        """Remove a role from one or more principals via the ZMI."""

class _ZODBRoleFilter:
    def __init__(self, id=None, **kw) -> None: ...
    def __call__(self, role_info): ...
