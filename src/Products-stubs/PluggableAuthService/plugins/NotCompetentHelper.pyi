from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete

class HigherLevelUserFolderAccessMixin:
    """mixin class for access to higher level user folders

    requires to be mixed with a `BasePlugin`.
    """

class NotCompetentBase(BasePlugin, HigherLevelUserFolderAccessMixin):
    """abstract `INotCompententPlugin` base class.

    with access to higher level user folders.
    """

    security: Incomplete
    id: Incomplete
    title: Incomplete
    def __init__(self, id, title: str = "") -> None: ...
    @security.private
    def isNotCompetentToAuthenticate(self, request) -> None: ...

class NotCompetent_byRoles(NotCompetentBase):
    """`INotCompetentPlugin` to prevent authentication shadowing by roles."""

    meta_type: str
    roles: Incomplete
    manage_options: Incomplete
    def isNotCompetentToAuthenticate(self, request): ...

manage_addNotCompetent_byRolesForm: Incomplete

def manage_addNotCompetent_byRoles(self, id, title: str = "", REQUEST=None) -> None:
    """Factory method to instantiate a NotCompetent_byRoles"""
