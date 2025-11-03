from zope.interface import Interface

class IMigrationTool(Interface):
    """Handles migrations between Plone releases."""
    def getInstanceVersion() -> None:
        """The version this instance of Plone is on."""
    def setInstanceVersion(version) -> None:
        """The version this instance of Plone is on."""
    def getFileSystemVersion() -> None:
        """The version the filesystem code of Plone is on."""
    def needUpgrading() -> None:
        """Need upgrading?"""
    def coreVersions() -> None:
        """Useful core version information."""
    def coreVersionsList() -> None:
        """Useful core version information."""
    def needUpdateRole() -> None:
        """Do roles need to be updated?"""
    def needRecatalog() -> None:
        """Does this thing now need recataloging?"""
    def upgrade(REQUEST=None, dry_run=None, swallow_errors: int = 1) -> None:
        """Perform the upgrade."""
