from Products.PluggableAuthService.interfaces import plugins
from zope.interface import Interface

class IGroupManagement(Interface):
    def addGroup(id, **kw) -> None:
        """
        Create a group with the supplied id, roles, and groups.
        return True if the operation succeeded
        """
    def addPrincipalToGroup(principal_id, group_id) -> None:
        """
        Add a given principal to the group.
        return True on success
        """
    def updateGroup(id, **kw) -> None:
        """
        Edit the given group. plugin specific
        return True on success
        """
    def setRolesForGroup(group_id, roles=()) -> None:
        """
        set roles for group
        return True on success
        """
    def removeGroup(group_id) -> None:
        """
        Remove the given group
        return True on success
        """
    def removePrincipalFromGroup(principal_id, group_id) -> None:
        """
        remove the given principal from the group
        return True on success
        """

class IGroupIntrospection(Interface):
    def getGroupById(group_id) -> None:
        """
        Returns the portal_groupdata-ish object for a group
        corresponding to this id.
        """
    def getGroups() -> None:
        """
        Returns an iteration of the available groups
        """
    def getGroupIds() -> None:
        """
        Returns a list of the available groups
        """
    def getGroupMembers(group_id) -> None:
        """
        return the members of the given group
        """

class IGroupDataTool(Interface):
    def wrapGroup(group) -> None:
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
    def setProperties(properties=None, **kw) -> None:
        """Allows setting of group properties en masse.
        Properties can be given either as a dict or a keyword parameters
        list"""
    def getProperty(id) -> None:
        """Return the value of the property specified by 'id'"""
    def getProperties() -> None:
        """Return the properties of this group. Properties are as usual in
        Zope."""
    def getGroupId() -> None:
        """Return the string id of this group, WITHOUT group prefix."""
    def getMemberId() -> None:
        """This exists only for a basic user/group API compatibility"""
    def getGroupName() -> None:
        """Return the name of the group."""
    def getGroupMembers() -> None:
        """Return a list of the portal_memberdata-ish members of the group."""
    def getAllGroupMembers() -> None:
        """Return a list of the portal_memberdata-ish members of the group
        including transitive ones (ie. users or groups of a group in that
        group)."""
    def getGroupMemberIds() -> None:
        """Return a list of the user ids of the group."""
    def getAllGroupMemberIds() -> None:
        """Return a list of the user ids of the group.
        including transitive ones (ie. users or groups of a group in that
        group)."""
    def addMember(id) -> None:
        """Add the existing member with the given id to the group"""
    def removeMember(id) -> None:
        """Remove the member with the provided id from the group"""
    def getGroup() -> None:
        """Returns the actual group implementation. Varies by group
        implementation (GRUF/Nux/et al)."""
