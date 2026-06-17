from zope.interface import Interface

class IMigrationTool(Interface):
    """Handles migrations between Plone releases."""
    def getInstanceVersion(self) -> None:
        """The version this instance of Plone is on."""
    def setInstanceVersion(self, version) -> None:
        """The version this instance of Plone is on."""
    def getFileSystemVersion(self) -> None:
        """The version the filesystem code of Plone is on."""
    def needUpgrading(self) -> None:
        """Need upgrading?"""
    def coreVersions(self) -> None:
        """Useful core version information."""
    def coreVersionsList(self) -> None:
        """Useful core version information."""
    def needUpdateRole(self) -> None:
        """Do roles need to be updated?"""
    def needRecatalog(self) -> None:
        """Does this thing now need recataloging?"""
    def upgrade(self, REQUEST=None, dry_run=None, swallow_errors: int = 1) -> None:
        """Perform the upgrade."""
