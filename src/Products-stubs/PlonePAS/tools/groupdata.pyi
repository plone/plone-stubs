from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

logger: Incomplete

class GroupDataError(Exception): ...

class GroupDataTool(UniqueObject, SimpleItem, PropertyManager):
    """This tool wraps group objects, allowing transparent access to
    properties.
    """

    id: str
    meta_type: str
    toolicon: str
    security: Incomplete
    def __init__(self) -> None: ...
    def wrapGroup(self, g):
        """Returns an object implementing the GroupData interface."""
    @security.private
    def registerGroupData(self, g, id) -> None:
        """
        Adds the given member data to the _members dict.
        This is done as late as possible to avoid side effect
        transactions and to reduce the necessary number of
        entries.
        """

class GroupData(SimpleItem):
    security: Incomplete
    id: Incomplete
    def __init__(self, tool, id) -> None: ...
    @security.private
    def notifyModified(self) -> None: ...
    @security.public
    def getGroup(self):
        """Returns the actual group implementation. Varies by group
        implementation (GRUF/Nux/et al). In GRUF this is a user object."""
    def getTool(self): ...
    @security.public
    def getGroupMemberIds(self):
        """
        Return a list of group member ids
        """
    @security.public
    def getAllGroupMemberIds(self):
        """
        Return a list of group member ids
        """
    @security.public
    def getGroupMembers(self):
        """
        Returns a list of the portal_memberdata-ish members of the group.
        This doesn't include TRANSITIVE groups/users.
        """
    @security.public
    def getAllGroupMembers(self):
        """
        Returns a list of the portal_memberdata-ish members of the group.
        This will include transitive groups / users
        """
    @security.private
    def canAdministrateGroup(self):
        """
        Return true if the #current# user can administrate this group
        """
    @security.public
    @postonly
    def addMember(self, id, REQUEST=None) -> None:
        """Add the existing member with the given id to the group"""
    @security.public
    @postonly
    def removeMember(self, id, REQUEST=None) -> None:
        """Remove the member with the provided id from the group."""
    def setProperties(self, properties=None, **kw):
        """Allows the manager group to set his/her own properties.
        Accepts either keyword arguments or a mapping for the "properties"
        argument.
        """
    def setGroupProperties(self, mapping):
        """PAS-specific method to set the properties of a group."""
    @security.public
    def getProperties(self):
        """Return the properties of this group. Properties are as usual
        in Zope.
        """
    @security.public
    def getProperty(self, id, default=None):
        """PAS-specific method to fetch a group's properties. Looks
        through the ordered property sheets.
        """
    @security.public
    def isGroup(self):
        """
        isGroup(self,) => Return true if this is a group.
        Will always return true for groups.
        As MemberData objects do not support this method, it is quite useless
        by now.
        So one can use groupstool.isGroup(g) instead to get this information.
        """
    @security.public
    def getGroupName(self): ...
    @security.public
    def getGroupId(self):
        """Get the ID of the group. The ID can be used, at least from
        Python, to get the user from the user's UserDatabase.
        Within Plone, all group ids are UNPREFIXED."""
    def getGroupTitleOrName(self):
        """Get the Title property of the group. If there is none
        then return the name"""
    @security.public
    def getMemberId(self):
        """This exists only for a basic user/group API compatibility"""
    @security.public
    def getRoles(self):
        """Return the list of roles assigned to a user."""
    @security.public
    def getRolesInContext(self, object):
        """Return the list of roles assigned to the user,  including local
        roles assigned in context of the passed in object."""
    @security.public
    def getDomains(self):
        """Return the list of domain restrictions for a user"""
    @security.public
    def has_role(self, roles, object=None):
        """Check to see if a user has a given role or roles."""
    def getUserName(self): ...
    getUserNameWithoutGroupPrefix = getUserName
    def canDelete(self):
        """True iff user can be removed from the Plone UI."""
    def canPasswordSet(self):
        """Always false for groups, which have no password."""
    def passwordInClear(self):
        """True iff password can be retrieved in the clear (not hashed.)

        False for PAS. It provides no API for getting passwords,
        though it would be possible to add one in the future.
        """
    def canWriteProperty(self, prop_name):
        """True iff the group property named in 'prop_name'
        can be changed.
        """
    canAddToGroup: Incomplete
    canRemoveFromGroup: Incomplete
    canAssignRole: Incomplete
