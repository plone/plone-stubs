from Products.PluggableAuthService.interfaces import plugins
from zope.interface import Interface

class IGroupManagement(Interface):
    def addGroup(self, id, **kw) -> None:
        """
        Create a group with the supplied id, roles, and groups.
        return True if the operation succeeded
        """
    def addPrincipalToGroup(self, principal_id, group_id) -> None:
        """
        Add a given principal to the group.
        return True on success
        """
    def updateGroup(self, id, **kw) -> None:
        """
        Edit the given group. plugin specific
        return True on success
        """
    def setRolesForGroup(self, group_id, roles=()) -> None:
        """
        set roles for group
        return True on success
        """
    def removeGroup(self, group_id) -> None:
        """
        Remove the given group
        return True on success
        """
    def removePrincipalFromGroup(self, principal_id, group_id) -> None:
        """
        remove the given principal from the group
        return True on success
        """

class IGroupIntrospection(Interface):
    def getGroupById(self, group_id) -> None:
        """
        Returns the portal_groupdata-ish object for a group
        corresponding to this id.
        """
    def getGroups(self) -> None:
        """
        Returns an iteration of the available groups
        """
    def getGroupIds(self) -> None:
        """
        Returns a list of the available groups
        """
    def getGroupMembers(self, group_id) -> None:
        """
        return the members of the given group
        """

class IGroupDataTool(Interface):
    def wrapGroup(self, group) -> None:
        """
        decorate a group with property management capabilities if needed
        """

class IGroupTool(IGroupIntrospection, IGroupManagement, plugins.IGroupsPlugin):
    """
    Defines an interface for managing and introspecting and
    groups and group membership.
    """

class IGroupData(Interface):
    """An abstract interface for accessing properties on a group object"""
    def setProperties(self, properties=None, **kw) -> None:
        """Allows setting of group properties en masse.
        Properties can be given either as a dict or a keyword parameters
        list"""
    def getProperty(self, id) -> None:
        """Return the value of the property specified by 'id'"""
    def getProperties(self) -> None:
        """Return the properties of this group. Properties are as usual in
        Zope."""
    def getGroupId(self) -> None:
        """Return the string id of this group, WITHOUT group prefix."""
    def getMemberId(self) -> None:
        """This exists only for a basic user/group API compatibility"""
    def getGroupName(self) -> None:
        """Return the name of the group."""
    def getGroupMembers(self) -> None:
        """Return a list of the portal_memberdata-ish members of the group."""
    def getAllGroupMembers(self) -> None:
        """Return a list of the portal_memberdata-ish members of the group
        including transitive ones (ie. users or groups of a group in that
        group)."""
    def getGroupMemberIds(self) -> None:
        """Return a list of the user ids of the group."""
    def getAllGroupMemberIds(self) -> None:
        """Return a list of the user ids of the group.
        including transitive ones (ie. users or groups of a group in that
        group)."""
    def addMember(self, id) -> None:
        """Add the existing member with the given id to the group"""
    def removeMember(self, id) -> None:
        """Remove the member with the provided id from the group"""
    def getGroup(self) -> None:
        """Returns the actual group implementation. Varies by group
        implementation (GRUF/Nux/et al)."""
