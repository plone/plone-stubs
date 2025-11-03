from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

logger: Incomplete

class NotSupported(Exception): ...

class GroupsTool(UniqueObject, SimpleItem):
    """This tool accesses group data through a acl_users object.

    It can be replaced with something that groups member data in a
    different way.
    """

    id: str
    meta_type: str
    security: Incomplete
    toolicon: str
    @postonly
    def addGroup(
        self, id, roles=[], groups=[], properties=None, REQUEST=None, *args, **kw
    ):
        """Create a group, with the supplied id, roles, and domains.

        Underlying user folder must support adding users via the usual
        Zope API.
        """
    @postonly
    def editGroup(self, id, roles=None, groups=None, REQUEST=None, *args, **kw) -> None:
        """Edit the given group with the supplied roles.

        Passwords for groups seem to be irrelevant.
        PlonePAS doesn't deal with domains either.

        If group is not present, returns without exception.
        """
    @postonly
    def removeGroup(self, group_id, REQUEST=None):
        """Remove a single group."""
    @postonly
    def removeGroups(self, ids, REQUEST=None) -> None:
        """Remove the group in the provided list (if possible)."""
    @postonly
    def setRolesForGroup(self, group_id, roles=(), REQUEST=None) -> None: ...
    @postonly
    def addPrincipalToGroup(self, principal_id, group_id, REQUEST=None): ...
    @postonly
    def removePrincipalFromGroup(self, principal_id, group_id, REQUEST=None): ...
    def getGroupById(self, group_id): ...
    def searchGroups(self, *args, **kw): ...
    def searchForGroups(self, REQUEST={}, **kw):
        """Search for groups by keyword.
        The following properties can be searched:
        - name
        #- email
        #- title

        Only id/title search is implemented for groups. Is the rest of
        this junk used anywhere?

        This is an \'AND\' request.

        When it takes \'name\' as keyword (or in REQUEST) and searches on
        Full name and id.

        Simple name searches are "fast".
        """
    def listGroups(self): ...
    def getGroupIds(self): ...
    listGroupIds = getGroupIds
    def getGroupMembers(self, group_id): ...
    def getGroupsForPrincipal(self, principal): ...
    @security.public
    def getGroupInfo(self, groupId):
        """
        Return default group info of any group
        """
    def getGroupsByUserId(self, userid):
        """Return a list of the groups the user corresponding to 'userid'
        belongs to."""
    def listGroupNames(self):
        """Return a list of the available groups' ids as entered
        (without group prefixes)."""
    @security.public
    def isGroup(self, u):
        """Test if a user/group object is a group or not.
        You must pass an object you get earlier with wrapUser() or wrapGroup()
        """
    @postonly
    def setGroupOwnership(self, group, object, REQUEST=None) -> None:
        """Make the object  'object' owned by group 'group'
        (a portal_groupdata-ish object).

        For GRUF this is easy. Others may have to re-implement."""
    @security.private
    def wrapGroup(self, g, wrap_anon: int = 0):
        """Sets up the correct acquisition wrappers for a group
        object and provides an opportunity for a portal_memberdata
        tool to retrieve and store member data independently of
        the user object.
        """
