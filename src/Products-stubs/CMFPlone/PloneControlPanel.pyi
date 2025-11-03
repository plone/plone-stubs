from _typeshed import Incomplete
from OFS.Folder import Folder
from OFS.PropertyManager import PropertyManager
from Products.CMFCore.ActionInformation import ActionInformation
from Products.CMFCore.ActionProviderBase import ActionProviderBase
from Products.CMFCore.utils import UniqueObject
from Products.CMFPlone.PloneBaseTool import PloneBaseTool

class PloneConfiglet(ActionInformation):
    appId: Incomplete
    def __init__(self, appId, **kwargs) -> None: ...
    def getAppId(self): ...
    def getDescription(self): ...
    def clone(self): ...
    def getAction(self, ec): ...

class PloneControlPanel(
    PloneBaseTool, UniqueObject, Folder, ActionProviderBase, PropertyManager
):
    """Weave together the various sources of "actions" which
    are apropos to the current user and context.
    """

    security: Incomplete
    id: str
    title: str
    toolicon: str
    meta_type: str
    manage_options: Incomplete
    group: Incomplete
    def __init__(self, **kw) -> None: ...
    def registerConfiglets(self, configlets) -> None: ...
    def getGroupIds(self, category: str = "site"): ...
    def getGroups(self, category: str = "site"): ...
    def listActions(self, info=None, object=None): ...
    def maySeeSomeConfiglets(self): ...
    def enumConfiglets(self, group=None): ...
    def unregisterConfiglet(self, id) -> None: ...
    def unregisterApplication(self, appId) -> None: ...
    def addAction(
        self,
        id,
        name,
        action,
        condition: str = "",
        permission: str = "",
        category: str = "Plone",
        visible: int = 1,
        appId=None,
        icon_expr: str = "",
        description: str = "",
        REQUEST=None,
    ):
        """Add an action to our list."""
    registerConfiglet = addAction
    def manage_editActionsForm(self, REQUEST, manage_tabs_message=None):
        """Show the 'Actions' management tab."""
    @property
    def site_url(self):
        """Return the absolute URL to the current site, which is likely not
        necessarily the portal root.
        Used by ``portlet_prefs`` to construct the URL to
        ``@@overview-controlpanel``.
        """
