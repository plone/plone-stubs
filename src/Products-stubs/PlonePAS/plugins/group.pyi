from .ufactory import PloneUser
from _typeshed import Incomplete
from Products.PluggableAuthService.plugins.ZODBGroupManager import ZODBGroupManager

manage_addGroupManagerForm: Incomplete
logger: Incomplete

def manage_addGroupManager(self, id, title: str = "", RESPONSE=None):
    """
    Add a zodb group manager with management and introspection
    capabilities to pas.
    """

class GroupManager(ZODBGroupManager):
    meta_type: str
    security: Incomplete
    def __init__(self, *args, **kw) -> None: ...
    def addGroup(self, group_id, *args, **kw): ...
    def removeGroup(self, group_id): ...
    def addPrincipalToGroup(self, principal_id, group_id): ...
    def removePrincipalFromGroup(self, principal_id, group_id): ...
    def updateGroup(self, group_id, title=None, description=None): ...
    def getGroupById(self, group_id, default=None): ...
    def getGroups(self): ...
    def getGroupIds(self): ...
    def getGroupMembers(self, group_id): ...
    @security.public
    def allowDeletePrincipal(self, principal_id):
        """True iff this plugin can delete a certain group.
        This is true if this plugin manages the group.
        """
    def getGroupInfo(self, group_id):
        """Over-ride parent to not explode when getting group info dict by
        group id."""
    def allowGroupAdd(self, user_id, group_id):
        """True iff this plugin will allow adding a certain user to a
        certain group."""
    def allowGroupRemove(self, user_id, group_id):
        """True iff this plugin will allow removing a certain user from a
        certain group."""

class PloneGroup(PloneUser):
    """Plone expects a user to come, with approximately the same
    behavior as a user.
    """

    security: Incomplete
    def getId(self, unprefixed=None):
        """-> user ID
        Modified to accept silly GRUF param.
        """
    @security.private
    def getMemberIds(self, transitive: int = 1):
        """Return member ids of this group, including or not
        transitive groups.
        """
    @security.public
    def addMember(self, id) -> None:
        """Add the existing member with the given id to the group"""
    @security.public
    def removeMember(self, id) -> None:
        """Remove the member with the provided id from the group."""
    @security.public
    def getRolesInContext(self, object):
        """Since groups can't actually log in, do nothing."""
    @security.public
    def allowed(self, object, object_roles=None):
        """Since groups can't actually log in, do nothing."""
