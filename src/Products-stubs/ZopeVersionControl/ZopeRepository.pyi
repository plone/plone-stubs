from . import Repository
from _typeshed import Incomplete
from OFS.role import RoleManager

import OFS

class ZopeRepository(Repository.Repository, RoleManager, OFS.SimpleItem.Item):
    """The ZopeRepository class builds on the core Repository implementation
    to provide the Zope management interface and other product trappings."""

    security: Incomplete
    meta_type: str
    manage_options: Incomplete
    manage_main: Incomplete
    manage = manage_main
    title: Incomplete
    def __init__(self, id=None, title: str = "") -> None: ...
    manage_properties_form: Incomplete
    def manage_edit(self, title: str = "", REQUEST=None):
        """Change object properties."""
    def __getitem__(self, name): ...
    @security.private
    def objectIds(self, spec=None): ...
    @security.private
    def objectValues(self, spec=None): ...
    @security.private
    def objectItems(self, spec=None): ...

def addRepository(self, id, title: str = "", REQUEST=None) -> None:
    """Zope object constructor function."""

addRepositoryForm: Incomplete
constructors: Incomplete
