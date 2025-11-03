from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject
from Products.CMFPlone.PloneBaseTool import PloneBaseTool

logger: Incomplete

class Addon:
    """A profile or product.

    This is meant for core Plone packages, especially packages that
    are marked as not installable.  These are packages that an admin should
    not activate, deactivate or upgrade manually, but that should be
    handled by Plone.

    Most of this is already handled in plone.app.upgrade.  But when
    you have added an upgrade step to such a package, it can be hard
    to remember that you should also arrange that plone.app.upgrade
    applies this upgrade step.  This leads to an upgraded Plone Site
    where some core packages are not updated.  Or the upgrade handlers
    are run, but the version of the profile is not upgraded in the
    GenericSetup tool.
    """

    profile_id: Incomplete
    check_module: Incomplete
    def __init__(self, profile_id=None, check_module=None) -> None: ...
    def safe(self): ...

class AddonList(list):
    def upgrade_all(self, context) -> None: ...

ADDON_LIST: Incomplete

class MigrationTool(PloneBaseTool, UniqueObject, SimpleItem):
    """Handles migrations between Plone releases"""

    id: str
    meta_type: str
    toolicon: str
    manage_options: Incomplete
    security: Incomplete
    def getInstanceVersion(self): ...
    def setInstanceVersion(self, version) -> None: ...
    def getFileSystemVersion(self): ...
    def getSoftwareVersion(self): ...
    def needUpgrading(self): ...
    def coreVersions(self): ...
    def coreVersionsList(self): ...
    def needUpdateRole(self): ...
    def needRecatalog(self): ...
    def listUpgrades(self): ...
    def upgrade(self, REQUEST=None, dry_run=None, swallow_errors: bool = True): ...
    upgrade: Incomplete

def registerUpgradePath(oldversion, newversion, function) -> None:
    """Basic register func"""
