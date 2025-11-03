from .ActionProviderBase import ActionProviderBase
from .utils import UniqueObject
from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

class URLTool(UniqueObject, SimpleItem, ActionProviderBase):
    """CMF URL Tool."""

    id: str
    meta_type: str
    zmi_icon: str
    security: Incomplete
    manage_options: Incomplete
    manage_overview: Incomplete
    @security.public
    def __call__(self, relative: int = 0, *args, **kw):
        """Get by default the absolute URL of the portal."""
    @security.public
    def getPortalObject(self):
        """Get the portal object itself."""
    @security.public
    def getRelativeContentPath(self, content):
        """Get the path for an object, relative to the portal root."""
    @security.public
    def getRelativeContentURL(self, content):
        """Get the URL for an object, relative to the portal root."""
    getRelativeUrl = getRelativeContentURL
    @security.public
    def getPortalPath(self):
        """Get the portal object's URL without the server URL component."""
