from contextlib import AbstractContextManager
from typing import Any

IS_TEST: bool | None

def adopt_user(
    username: str | None = None, user: Any = None
) -> AbstractContextManager[None]:
    """Context manager for temporarily switching user inside a block.

    :param user: User object to switch to inside block.
    :param username: username of user to switch to inside block.
    """

def adopt_roles(roles: list[str] | None = None) -> AbstractContextManager[None]:
    """Context manager for temporarily switching roles.

    :param roles: [required] New roles to gain inside block. Existing roles will be lost.
    :type roles: list of strings
    """

class _GlobalRoleOverridingContext:
    """Context object for temporarily overriding roles."""

    _proxy_roles: list[str]
    def __init__(self, roles: list[str]) -> None: ...
    def getOwner(self) -> None: ...
    def getWrappedOwner(self) -> None: ...

def debug_mode() -> bool:
    """Return True if your zope instance is running in debug mode."""

def test_mode() -> bool:
    """Returns True if you are running the zope test runner."""

def read_only_mode() -> bool:
    """Check if the Zope instance is running on a read-only ZODB.

    :returns: bool isReadOnly True if ZODB is read-only
    """

def plone_version() -> str:
    """Return Plone version number.

    :returns: string denoting what release of Plone this distribution contains
    """

def zope_version() -> str:
    """Return Zope 2 version number.

    :returns: string denoting what release of Zope2 this distribution contains
    """
