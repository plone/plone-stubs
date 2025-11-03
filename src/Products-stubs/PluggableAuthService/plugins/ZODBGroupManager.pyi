from ..plugins.BasePlugin import BasePlugin
from ..utils import csrf_only
from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from zope.interface import Interface

class IZODBGroupManager(Interface):
    """Marker interface."""

manage_addZODBGroupManagerForm: Incomplete

def addZODBGroupManager(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add a ZODBGroupManager to a Pluggable Auth Service."""

class ZODBGroupManager(BasePlugin):
    """PAS plugin for managing groups, and groups of groups in the ZODB"""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    @security.private
    def enumerateGroups(
        self,
        id=None,
        title=None,
        exact_match: bool = False,
        sort_by=None,
        max_results=None,
        **kw,
    ):
        """See IGroupEnumerationPlugin."""
    @security.private
    def getGroupsForPrincipal(self, principal, request=None):
        """See IGroupsPlugin."""
    def listGroupIds(self):
        """-> (group_id_1, ... group_id_n)"""
    def listGroupInfo(self):
        """-> (dict, ...dict)

        o Return one mapping per group, with the following keys:

          - 'id'
        """
    def getGroupInfo(self, group_id):
        """group_id -> dict"""
    @security.private
    def addGroup(self, group_id, title=None, description=None) -> None:
        """Add 'group_id' to the list of groups managed by this object.

        o Raise KeyError on duplicate.
        """
    @security.private
    def updateGroup(self, group_id, title=None, description=None) -> None:
        """Update properties for 'group_id'

        o Raise KeyError if group_id doesn't already exist.
        """
    @security.private
    def removeGroup(self, group_id) -> None:
        """Remove 'role_id' from the list of roles managed by this
            object, removing assigned members from it before doing so.

        o Raise KeyError if 'group_id' doesn't already exist.
        """
    def listAvailablePrincipals(self, group_id, search_id):
        """Return a list of principal IDs to that can belong to the group.

        o If supplied, 'search_id' constrains the principal IDs;  if not,
          return empty list.

        o Omit principals with existing assignments.
        """
    def listAssignedPrincipals(self, group_id):
        """Return a list of principal IDs belonging to a group."""
    @security.private
    def addPrincipalToGroup(self, principal_id, group_id):
        """Add a principal to a group.

        o Return a boolean indicating whether a new assignment was created.

        o Raise KeyError if 'group_id' is unknown.
        """
    @security.private
    def removePrincipalFromGroup(self, principal_id, group_id):
        """Remove a prinicpal from from a group.

        o Return a boolean indicating whether the principal was already
          a member of the group.

        o Raise KeyError if 'group_id' is unknown.

        o Ignore requests to remove a principal if not already a member
          of the group.
        """
    manage_options: Incomplete
    manage_widgets: Incomplete
    manage_groups: Incomplete
    manage_twoLists: Incomplete
    def manage_addGroup(
        self, group_id, title=None, description=None, RESPONSE=None
    ) -> None:
        """Add a group via the ZMI."""
    def manage_updateGroup(self, group_id, title, description, RESPONSE=None) -> None:
        """Update a group via the ZMI."""
    @csrf_only
    @postonly
    def manage_removeGroups(self, group_ids, RESPONSE=None, REQUEST=None) -> None:
        """Remove one or more groups via the ZMI."""
    @csrf_only
    @postonly
    def manage_addPrincipalsToGroup(
        self, group_id, principal_ids, RESPONSE=None, REQUEST=None
    ) -> None:
        """Add one or more principals to a group via the ZMI."""
    @csrf_only
    @postonly
    def manage_removePrincipalsFromGroup(
        self, group_id, principal_ids, RESPONSE=None, REQUEST=None
    ) -> None:
        """Remove one or more principals from a group via the ZMI."""

class _ZODBGroupFilter:
    def __init__(self, id=None, title=None, **kw) -> None: ...
    def __call__(self, group_info): ...
