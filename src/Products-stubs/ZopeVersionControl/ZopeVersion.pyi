from . import Version
from _typeshed import Incomplete
from OFS.role import RoleManager

import OFS

class ZopeVersion(Version.Version, RoleManager, OFS.SimpleItem.Item):
    """The ZopeVersion class builds on the core Version class to provide
    the Zope management interface and other product trappings."""

    security: Incomplete
    meta_type: str
    manage_options: Incomplete
    icon: str
    manage_main: Incomplete
    manage = manage_main
    manage_properties_form: Incomplete
    def manage_edit(self, REQUEST=None):
        """Change object properties."""
