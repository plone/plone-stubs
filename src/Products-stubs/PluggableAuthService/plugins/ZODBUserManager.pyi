from ..plugins.BasePlugin import BasePlugin
from ..utils import csrf_only
from _typeshed import Incomplete
from AccessControl.requestmethod import postonly
from OFS.Cache import Cacheable
from zope.interface import Interface

logger: Incomplete

class IZODBUserManager(Interface):
    """Marker interface."""

manage_addZODBUserManagerForm: Incomplete

def addZODBUserManager(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add a ZODBUserManager to a Pluggable Auth Service."""

class ZODBUserManager(BasePlugin, Cacheable):
    """PAS plugin for managing users in the ZODB."""

    meta_type: str
    zmi_icon: str
    security: Incomplete
    title: Incomplete
    def __init__(self, id, title=None) -> None: ...
    @security.private
    def authenticateCredentials(self, credentials):
        """See IAuthenticationPlugin.

        o We expect the credentials to be those returned by
          ILoginPasswordExtractionPlugin.
        """
    @security.private
    def enumerateUsers(
        self,
        id=None,
        login=None,
        exact_match: bool = False,
        sort_by=None,
        max_results=None,
        **kw,
    ):
        """See IUserEnumerationPlugin."""
    @security.private
    def doAddUser(self, login, password): ...
    def listUserIds(self):
        """-> (user_id_1, ... user_id_n)"""
    def getUserInfo(self, user_id):
        """user_id -> dict"""
    def listUserInfo(self):
        """-> (dict, ...dict)

        o Return one mapping per user, with the following keys:

          - 'user_id'
          - 'login_name'
        """
    def getUserIdForLogin(self, login_name):
        """login_name -> user_id

        o Raise KeyError if no user exists for the login name.
        """
    def getLoginForUserId(self, user_id):
        """user_id -> login_name

        o Raise KeyError if no user exists for that ID.
        """
    @security.private
    def addUser(self, user_id, login_name, password) -> None: ...
    @security.private
    def updateUser(self, user_id, login_name): ...
    @security.private
    def updateEveryLoginName(self, quit_on_first_error: bool = True) -> None: ...
    @security.private
    def removeUser(self, user_id) -> None: ...
    @security.private
    def updateUserPassword(self, user_id, password) -> None: ...
    manage_options: Incomplete
    manage_widgets: Incomplete
    manage_users: Incomplete
    @csrf_only
    @postonly
    def manage_addUser(
        self, user_id, login_name, password, confirm, RESPONSE=None, REQUEST=None
    ) -> None:
        """Add a user via the ZMI."""
    @csrf_only
    @postonly
    def manage_updateUserPassword(
        self, user_id, password, confirm, RESPONSE=None, REQUEST=None
    ) -> None:
        """Update a user's login name / password via the ZMI."""
    @csrf_only
    @postonly
    def manage_updateUser(
        self, user_id, login_name, RESPONSE=None, REQUEST=None
    ) -> None:
        """Update a user's login name via the ZMI."""
    @csrf_only
    @postonly
    def manage_removeUsers(self, user_ids, RESPONSE=None, REQUEST=None) -> None:
        """Remove one or more users via the ZMI."""
    def getOwnUserInfo(self):
        """Return current user's info."""
    manage_updatePasswordForm: Incomplete
    @csrf_only
    @postonly
    def manage_updatePassword(
        self, login_name, password, confirm, RESPONSE=None, REQUEST=None
    ) -> None:
        """Update the current user's password and login name."""

class _ZODBUserFilter:
    def __init__(self, id=None, login=None, **kw) -> None: ...
    def __call__(self, user_info): ...
