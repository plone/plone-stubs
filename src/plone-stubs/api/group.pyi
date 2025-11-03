from Products.PlonePAS.tools.groupdata import GroupData
from Products.PluggableAuthService.interfaces.authservice import IBasicUser
from typing import Any

def create(
    groupname: str,
    title: str | None = None,
    description: str | None = None,
    roles: list[str] = [],
    groups: list[str] = [],
) -> GroupData:
    """Create a group.

    :param groupname: [required] Name of the new group.
    :param title: Title of the new group
    :param description: Description of the new group
    :param roles: Roles to assign to this group
    :param groups: Groups that belong to this group
    :returns: Newly created group
    :raises: ValueError
    """

def get(groupname: str) -> GroupData | None:
    """Get a group.

    :param groupname: [required] Name of the group we want to get.
    :returns: Group or None if not found
    """

def get_groups(
    username: str | None = None, user: IBasicUser | None = None
) -> list[GroupData]:
    """Get all groups or all groups filtered by user.

    :param username: Username of the user for which to return groups.
    :param user: User for which to return groups.
    :returns: All groups (optionally filtered by user)
    :raises: UserNotFoundError
    """

def delete(groupname: str | None = None, group: GroupData | None = None) -> Any:
    """Delete a group.

    :param groupname: Name of the group to be deleted.
    :param group: Group object to be deleted.
    :raises: ValueError
    """

def add_user(
    groupname: str | None = None,
    group: GroupData | None = None,
    username: str | None = None,
    user: IBasicUser | None = None,
) -> None:
    """Add the user to a group.

    :param groupname: Name of the group to which to add the user.
    :param group: Group to which to add the user.
    :param username: Username of the user to add to the group.
    :param user: User to add to the group.
    :raises: ValueError, UserNotFoundError
    """

def remove_user(
    groupname: str | None = None,
    group: GroupData | None = None,
    username: str | None = None,
    user: IBasicUser | None = None,
) -> None:
    """Remove the user from a group.

    :param groupname: Name of the group to remove the user from.
    :param group: Group to remove the user from.
    :param username: Username of the user to delete from the group.
    :param user: User to delete from the group.
    :raises: ValueError, UserNotFoundError
    """

def get_roles(
    groupname: str | None = None,
    group: GroupData | None = None,
    obj: Any = None,
    inherit: bool = True,
) -> list[str]:
    """Get group's site-wide or local roles.

    :param groupname: Name of the group to get roles from.
    :param group: Group to get roles from.
    :param obj: If obj is set then return local roles on this context.
    :param inherit: Show only local roles if False
    :raises: ValueError
    """

def grant_roles(
    groupname: str | None = None,
    group: GroupData | None = None,
    roles: list[str] | None = None,
    obj: Any = None,
) -> None:
    """Grant roles to a group.

    :param groupname: Name of the group to grant roles to.
    :param group: Group to grant roles to.
    :param roles: [required] List of roles to grant
    :param obj: If obj is set then grant local roles on this context.
    :raises: ValueError
    """

def revoke_roles(
    groupname: str | None = None,
    group: GroupData | None = None,
    roles: list[str] | None = None,
    obj: Any = None,
) -> None:
    """Revoke roles from a group.

    :param groupname: Name of the group to revoke roles to.
    :param group: Group to revoke roles to.
    :param roles: [required] List of roles to revoke
    :param obj: If obj is set then revoke local roles on this context.
    :raises: ValueError
    """
