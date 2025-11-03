from _typeshed import Incomplete
from Acquisition import Implicit
from App.Management import Tabs
from OFS.owner import Owned
from OFS.role import RoleManager
from OFS.SimpleItem import Item
from Persistence import Persistent

bad_path_chars_in: Incomplete
LOG: Incomplete
default_sdc_settings: Incomplete
constructSessionDataManagerForm: Incomplete

def constructSessionDataManager(
    self, id, title: str = "", path=None, requestName=None, REQUEST=None
):
    """ """

class SessionIdManagerErr(Exception): ...

class SessionDataManager(Item, Implicit, Persistent, RoleManager, Owned, Tabs):
    """The Zope default session data manager implementation."""

    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    security: Incomplete
    ok: Incomplete
    manage_sessiondatamgr: Incomplete
    def getSessionData(self, create: int = 1):
        """ """
    def hasSessionData(self):
        """ """
    def clearSessionData(self): ...
    def getSessionDataByKey(self, key): ...
    def getBrowserIdManager(self):
        """ """
    id: Incomplete
    def __init__(self, id, path=None, title: str = "", requestName=None) -> None: ...
    def manage_changeSDM(self, title, path=None, requestName=None, REQUEST=None):
        """ """
    title: str
    def setTitle(self, title) -> None:
        """ """
    obpath: Incomplete
    def setContainerPath(self, path=None) -> None:
        """ """
    def getContainerPath(self):
        """ """
    def hasSessionDataContainer(self):
        """ZMI helper: do we have a valid session data container?"""
    def usesDefaultSessionDataContainer(self):
        """ZMI helper: is the default temporary folder session container used?"""
    def getDefaultSessionDataContainerSettings(self):
        """ZMI helper: Return the session data container default settings"""
    def manage_changeSDCDefaults(
        self,
        title: str = "",
        timeout_mins: int = 20,
        addNotification: str = "",
        delNotification: str = "",
        limit: int = 0,
        period_secs: int = 20,
        REQUEST=None,
    ):
        """Collect settings for the default session data container"""
    def getRequestName(self):
        """ """
    def manage_afterAdd(self, item, container) -> None:
        """Add our traversal hook"""
    def manage_beforeDelete(self, item, container) -> None:
        """Clean up on delete"""
    def updateTraversalData(self, requestSessionName=None) -> None: ...

class SessionDataManagerTraverser(Persistent):
    def __init__(self, requestSessionName, sessionDataManagerName) -> None: ...
    def __call__(self, container, request) -> None:
        """
        This method places a session data object reference in
        the request.  It is called on each and every request to Zope in
        Zopes after 2.5.0 when there is a session data manager installed
        in the root.
        """
