from _typeshed import Incomplete
from OFS.Folder import Folder
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin

logger: Incomplete
CC_ID: str

def manage_addCookieCrumblingPlugin(
    self, id, title: str = "", RESPONSE=None, **kw
) -> None:
    """
    Create an instance of a cookie crumbling plugin.
    """

manage_addCookieCrumblingPluginForm: Incomplete

class CookieCrumblingPlugin(Folder, BasePlugin):
    """Multi-plugin for injecting HTTP Basic Authentication
    credentials from form credentials.
    """

    meta_type: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    @security.private
    def extractCredentials(self, request):
        """Extract basic auth credentials from 'request'."""
