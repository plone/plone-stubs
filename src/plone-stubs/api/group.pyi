from plone.dexterity.content import DexterityContent
from Products.PlonePAS.tools.groupdata import GroupData
from Products.PlonePAS.tools.memberdata import MemberData
from Products.PluggableAuthService.interfaces.authservice import IBasicUser

def create(
    groupname: str,
    title: str | None = None,
    description: str | None = None,
    roles: list[str] | None = None,
    groups: list[str] | None = None,
) -> GroupData:
    """Create a group.

    :param groupname: [required] Name of the new group.
    :type groupname: string
    :param title: Title of the new group.
    :type title: string
    :param description: Description of the new group.
    :type description: string
    :param roles: Roles to assign to this group.
    :type roles: list of strings
    :param groups: Groups that belong to this group.
    :type groups: list of strings
    :returns: Newly created group.
    :rtype: GroupData object
    """
def get(groupname: str) -> GroupData | None:
    """Get a group.

    :param groupname: [required] Name of the group we want to get.
    :type groupname: string
    :returns: Group or None if not found.
    :rtype: GroupData object
    """
def get_groups(
    username: str | None = None,
    user: MemberData | IBasicUser | None = None,
) -> list[GroupData]:
    """Get all groups or all groups filtered by user.

    :param username: Username of the user for which to return groups.
    :type username: string
    :param user: User for which to return groups.
    :type user: MemberData or IBasicUser object
    :returns: All groups (optionally filtered by user).
    :rtype: list of GroupData objects
    """
def delete(
    groupname: str | None = None,
    group: GroupData | None = None,
) -> bool:
    """Delete a group.

    :param groupname: Name of the group to be deleted.
    :type groupname: string
    :param group: Group object to be deleted.
    :type group: GroupData object
    :returns: True if the group was deleted.
    :rtype: bool
    """
def add_user(
    groupname: str | None = None,
    group: GroupData | None = None,
    username: str | None = None,
    user: MemberData | IBasicUser | None = None,
) -> None:
    """Add the user to a group.

    :param groupname: Name of the group to which to add the user.
    :type groupname: string
    :param group: Group to which to add the user.
    :type group: GroupData object
    :param username: Username of the user to add to the group.
    :type username: string
    :param user: User to add to the group.
    :type user: MemberData or IBasicUser object
    """
def remove_user(
    groupname: str | None = None,
    group: GroupData | None = None,
    username: str | None = None,
    user: MemberData | IBasicUser | None = None,
) -> None:
    """Remove the user from a group.

    :param groupname: Name of the group to remove the user from.
    :type groupname: string
    :param group: Group to remove the user from.
    :type group: GroupData object
    :param username: Username of the user to remove from the group.
    :type username: string
    :param user: User to remove from the group.
    :type user: MemberData or IBasicUser object
    """
def get_roles(
    groupname: str | None = None,
    group: GroupData | None = None,
    obj: DexterityContent | None = None,
    inherit: bool = True,
) -> list[str]:
    """Get group's site-wide or local roles.

    :param groupname: Name of the group to get roles from.
    :type groupname: string
    :param group: Group to get roles from.
    :type group: GroupData object
    :param obj: If obj is set then return local roles on this context.
    :type obj: Content object
    :param inherit: Show only local roles if False.
    :type inherit: boolean
    :returns: List of roles.
    :rtype: list of strings
    """
def grant_roles(
    groupname: str | None = None,
    group: GroupData | None = None,
    roles: list[str] | None = None,
    obj: DexterityContent | None = None,
) -> None:
    """Grant roles to a group.

    :param groupname: Name of the group to grant roles to.
    :type groupname: string
    :param group: Group to grant roles to.
    :type group: GroupData object
    :param roles: [required] List of roles to grant.
    :type roles: list of strings
    :param obj: If obj is set then grant local roles on this context.
    :type obj: Content object
    """
def revoke_roles(
    groupname: str | None = None,
    group: GroupData | None = None,
    roles: list[str] | None = None,
    obj: DexterityContent | None = None,
) -> None:
    """Revoke roles from a group.

    :param groupname: Name of the group to revoke roles from.
    :type groupname: string
    :param group: Group to revoke roles from.
    :type group: GroupData object
    :param roles: [required] List of roles to revoke.
    :type roles: list of strings
    :param obj: If obj is set then revoke local roles on this context.
    :type obj: Content object
    """
