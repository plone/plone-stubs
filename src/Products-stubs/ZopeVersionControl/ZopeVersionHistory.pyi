from . import VersionHistory
from _typeshed import Incomplete
from OFS.role import RoleManager

import OFS

class ZopeVersionHistory(
    VersionHistory.VersionHistory, RoleManager, OFS.SimpleItem.Item
):
    """The ZopeVersionHistory build on the core VersionHistory class to
    provide the Zope management interface and other product trappings."""

    security: Incomplete
    meta_type: str
    manage_options: Incomplete
    icon: str
    manage_main: Incomplete
    manage = manage_main
    manage_properties_form: Incomplete
    def manage_edit(self, REQUEST=None):
        """Change object properties."""
    def __getitem__(self, name): ...
    @security.private
    def objectIds(self, spec=None): ...
    @security.private
    def objectValues(self, spec=None): ...
    @security.private
    def objectItems(self, spec=None): ...
