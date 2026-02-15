from plone.dexterity.content import DexterityContent
from Products.PlonePAS.tools.groupdata import GroupData
from Products.PlonePAS.tools.memberdata import MemberData
from Products.PluggableAuthService.interfaces.authservice import IBasicUser
from typing import Any

def create(
    email: str | None = None,
    username: str | None = None,
    password: str | None = None,
    roles: tuple[str, ...] = ("Member",),
    properties: dict[str, Any] | None = None,
) -> MemberData:
    """Create a user.

    :param email: [required] Email for the new user.
    :type email: string
    :param username: Username for the new user. Required if email is not used as login.
    :type username: string
    :param password: Password for the new user. If not set, generate a random 8-char one.
    :type password: string
    :param roles: Roles for the new user. Defaults to ('Member',).
    :type roles: tuple of strings
    :param properties: User properties to assign to the new user.
    :type properties: dict
    :returns: Newly created user.
    :rtype: MemberData object
    """
def get(
    userid: str | None = None,
    username: str | None = None,
) -> MemberData | None:
    """Get a user.

    :param userid: Userid of the user we want to get.
    :type userid: string
    :param username: Username of the user we want to get.
    :type username: string
    :returns: User or None if not found.
    :rtype: MemberData object
    """
def get_current() -> MemberData:
    """Get the currently logged-in user.

    :returns: Currently logged-in user.
    :rtype: MemberData object
    """
def get_users(
    groupname: str | None = None,
    group: GroupData | None = None,
) -> list[MemberData]:
    """Get all users or users filtered by group.

    :param groupname: Groupname of the group of which to return users.
    :type groupname: string
    :param group: Group of which to return users.
    :type group: GroupData object
    :returns: All users (optionally filtered by group).
    :rtype: list of MemberData objects
    """
def delete(
    username: str | None = None,
    user: MemberData | IBasicUser | None = None,
) -> None:
    """Delete a user.

    :param username: Username of the user to be deleted.
    :type username: string
    :param user: User object to be deleted.
    :type user: MemberData object
    """
def is_anonymous() -> bool:
    """Check if the currently logged-in user is anonymous.

    :returns: True if the current user is anonymous, False otherwise.
    :rtype: bool
    """
def get_roles(
    username: str | None = None,
    user: MemberData | IBasicUser | None = None,
    obj: DexterityContent | None = None,
    inherit: bool = True,
) -> list[str]:
    """Get user's site-wide or local roles.

    :param username: Username of the user for which to get roles.
    :type username: string
    :param user: User object for which to get roles.
    :type user: MemberData object
    :param obj: If obj is set then return local roles on this context.
    :type obj: Content object
    :param inherit: If obj is set and inherit is False, only return local roles.
    :type inherit: boolean
    :returns: List of roles.
    :rtype: list of strings
    """
def get_permissions(
    username: str | None = None,
    user: MemberData | IBasicUser | None = None,
    obj: DexterityContent | None = None,
) -> dict[str, bool]:
    """Get user's site-wide or local permissions.

    :param username: Username of the user for which you want to check the permissions.
    :type username: string
    :param user: User object for which you want to check the permissions.
    :type user: MemberData object
    :param obj: If obj is set then check the permissions on this context.
    :type obj: Content object
    :returns: Dictionary mapping permission names to boolean values.
    :rtype: dict
    """
def has_permission(
    permission: str,
    username: str | None = None,
    user: MemberData | IBasicUser | None = None,
    obj: DexterityContent | None = None,
) -> bool:
    """Check whether a user has the given permission.

    :param permission: [required] The permission you wish to check.
    :type permission: string
    :param username: Username of the user for which you want to check the permission.
    :type username: string
    :param user: User object for which you want to check the permission.
    :type user: MemberData object
    :param obj: If obj is set then check the permission on this context.
    :type obj: Content object
    :returns: True if the user has the permission, False otherwise.
    :rtype: bool
    """
def grant_roles(
    username: str | None = None,
    user: MemberData | IBasicUser | None = None,
    obj: DexterityContent | None = None,
    roles: list[str] | None = None,
) -> None:
    """Grant roles to a user.

    :param username: Username of the user that will receive the granted roles.
    :type username: string
    :param user: User object that will receive the granted roles.
    :type user: MemberData object
    :param obj: If obj is set then grant roles on this context.
    :type obj: Content object
    :param roles: [required] List of roles to grant.
    :type roles: list of strings
    """
def revoke_roles(
    username: str | None = None,
    user: MemberData | IBasicUser | None = None,
    obj: DexterityContent | None = None,
    roles: list[str] | None = None,
) -> None:
    """Revoke roles from a user.

    :param username: Username of the user that will have roles revoked.
    :type username: string
    :param user: User object that will have roles revoked.
    :type user: MemberData object
    :param obj: If obj is set then revoke roles on this context.
    :type obj: Content object
    :param roles: [required] List of roles to revoke.
    :type roles: list of strings
    """
