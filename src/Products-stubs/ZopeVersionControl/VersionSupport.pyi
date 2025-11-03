from _typeshed import Incomplete

import ExtensionClass

class VersionSupport(ExtensionClass.Base):
    """Mixin class to support version-controllable resources."""

    manage_options: Incomplete
    security: Incomplete
    versionControlMain: Incomplete
    versionControlLog: Incomplete
    @security.private
    def haveRepository(self): ...
    @security.private
    def getRepository(self): ...
    @security.public
    def isAVersionableResource(self, object): ...
    @security.public
    def isUnderVersionControl(self): ...
    @security.public
    def isResourceUpToDate(self): ...
    @security.public
    def isResourceChanged(self): ...
    @security.public
    def getVersionInfo(self): ...
    def applyVersionControl(self, REQUEST=None):
        """Place a resource under version control."""
    def checkoutResource(self, REQUEST=None):
        """Checkout a version-controlled resource."""
    def checkinResource(self, message: str = "", REQUEST=None):
        """Checkout a version-controlled resource."""
    def uncheckoutResource(self, REQUEST=None):
        """Uncheckout a version-controlled resource."""
    def updateResource(self, selector, REQUEST=None):
        """Update a version-controlled resource."""
    def labelResource(self, label, force: int = 0, REQUEST=None):
        """Label a version-controlled resource."""
    def getVersionIds(self): ...
    def getLabelsForHistory(self): ...
    def getLabelsForVersion(self): ...
    def getLogEntries(self): ...
