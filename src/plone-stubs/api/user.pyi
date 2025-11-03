from Products.PlonePAS.tools.groupdata import GroupData
from Products.PlonePAS.tools.memberdata import MemberData
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
    :param username: Username for the new user.
    :param password: Password for the new user. If not set, generate a random 8-char one.
    :param roles: Roles for the new user. Defaults to ('Member',)
    :param properties: User properties to assign to the new user.
    :returns: Newly created user
    :raises: MissingParameterError, InvalidParameterError
    """

def get(userid: str | None = None, username: str | None = None) -> MemberData | None:
    """Get a user.

    :param userid: Userid of the user we want to get.
    :param username: Username of the user we want to get.
    :returns: User or None if not found
    :raises: MissingParameterError
    """

def get_current() -> MemberData:
    """Get the currently logged-in user.

    :returns: Currently logged-in user
    """

def get_users(
    groupname: str | None = None,
    group: GroupData | None = None,
) -> list[MemberData]:
    """Get all users or all users filtered by group.

    :param groupname: Groupname of the group of which to return users.
    :param group: Group of which to return users.
    :returns: All users (optionally filtered by group)
    """

def delete(username: str | None = None, user: MemberData | None = None) -> None:
    """Delete a user.

    :param username: Username of the user to be deleted.
    :param user: User object to be deleted.
    :raises: MissingParameterError, InvalidParameterError
    """

def is_anonymous() -> bool:
    """Check if the currently logged-in user is anonymous.

    :returns: True if the current user is anonymous, False otherwise.
    """

def get_roles(
    username: str | None = None,
    user: MemberData | None = None,
    obj: Any = None,
    inherit: bool = True,
) -> list[str]:
    """Get user's site-wide or local roles.

    :param username: Username of the user for which to get roles.
    :param user: User object for which to get roles.
    :param obj: If obj is set then return local roles on this context.
    :param inherit: if obj is set and inherit is False, only return local roles
    :raises: MissingParameterError
    """

def get_permissions(
    username: str | None = None,
    user: MemberData | None = None,
    obj: Any = None,
) -> dict[str, bool]:
    """Get user's site-wide or local permissions.

    :param username: Username of the user for which you want to check the permissions.
    :param user: User object for which you want to check the permissions.
    :param obj: If obj is set then check the permissions on this context.
    :returns: Dictionary mapping permission names to boolean values
    :raises: InvalidParameterError
    """

def has_permission(
    permission: str,
    username: str | None = None,
    user: MemberData | None = None,
    obj: Any = None,
) -> bool:
    """Check whether this user has the given permission.

    :param permission: [required] The permission you wish to check
    :param username: Username of the user for which you want to check the permission.
    :param user: User object for which you want to check the permission.
    :param obj: If obj is set then check the permission on this context.
    :returns: True if the user has the permission, False otherwise.
    :raises: InvalidParameterError
    """

def grant_roles(
    username: str | None = None,
    user: MemberData | None = None,
    obj: Any = None,
    roles: list[str] | None = None,
) -> None:
    """Grant roles to a user.

    :param username: Username of the user that will receive the granted roles.
    :param user: User object that will receive the granted roles.
    :param obj: If obj is set then grant roles on this context.
    :param roles: [required] List of roles to grant
    :raises: InvalidParameterError, MissingParameterError
    """

def revoke_roles(
    username: str | None = None,
    user: MemberData | None = None,
    obj: Any = None,
    roles: list[str] | None = None,
) -> None:
    """Revoke roles from a user.

    :param username: Username of the user that will receive the revoked roles.
    :param user: User object that will receive the revoked roles.
    :param obj: If obj is set then revoke roles on this context.
    :param roles: [required] List of roles to revoke
    :raises: InvalidParameterError
    """
