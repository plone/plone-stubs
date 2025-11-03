from _typeshed import Incomplete
from Acquisition import Implicit
from OFS.Cache import Cacheable
from OFS.Folder import Folder

security: Incomplete
logger: Incomplete

def reraise(plugin) -> None: ...

MultiPlugins: Incomplete

def registerMultiPlugin(meta_type) -> None:
    """Register a 'multi-plugin' in order to expose it to the Add List"""

class DumbHTTPExtractor(Implicit):
    security: Incomplete
    @security.private
    def extractCredentials(self, request):
        """Pull HTTP credentials out of the request."""

class EmergencyUserAuthenticator(Implicit):
    security: Incomplete
    @security.private
    def authenticateCredentials(self, credentials):
        """Check credentials against the emergency user."""

class PluggableAuthService(Folder, Cacheable):
    """All-singing, all-dancing user folder."""

    security: Incomplete
    meta_type: str
    zmi_icon: str
    zmi_show_add_dialog: bool
    id: str
    maxlistusers: int
    login_transform: str
    def getId(self): ...
    def getUser(self, name):
        """See IUserFolder."""
    def getUserById(self, id, default=None):
        """See IUserFolder."""
    @security.public
    def validate(self, request, auth: str = "", roles=...):
        """See IUserFolder."""
    def searchUsers(self, **kw):
        """Search for users"""
    def searchGroups(self, **kw):
        """Search for groups"""
    def searchPrincipals(self, groups_first: bool = False, **kw):
        """Search for principals (users, groups, or both)"""
    @security.private
    def __creatable_by_emergency_user__(self): ...
    manage_search: Incomplete
    manage_options: Incomplete
    def resultsBatch(
        self, results, REQUEST, size: int = 20, orphan: int = 2, overlap: int = 0
    ):
        """ZMI helper for getting batching for displaying search results"""
    @security.public
    def all_meta_types(self):
        """What objects can be put in here?"""
    @security.private
    def manage_beforeDelete(self, item, container) -> None: ...
    @security.private
    def manage_afterAdd(self, item, container) -> None: ...
    def __call__(self, container, req) -> None:
        """The __before_publishing_traverse__ hook."""
    @security.private
    def applyTransform(self, value):
        """Transform for login name.

        Possibly transform the login, for example by making it lower
        case.

        value must be a string (or unicode) or it may be a sequence
        (list, tuple), in which case we need to iterate over it.
        """
    @security.private
    def lower(self, value):
        """Transform for login name.

        Strip the value and lowercase it.

        To use this, set login_tranform to 'lower'.
        """
    @security.private
    def upper(self, value):
        """Transform for login name.

        Strip the value and uppercase it.

        To use this, set login_tranform to 'upper'.
        """
    def challenge(self, request, response): ...
    @security.public
    def hasUsers(self):
        """Zope quick start sacrifice.

        The quick start page expects a hasUsers() method.
        """
    @security.public
    def updateCredentials(self, request, response, login, new_password) -> None:
        """Central updateCredentials method

        This method is needed for cases where the credentials storage and
        the credentials extraction is handled by different plugins. Example
        case would be if the CookieAuthHelper is used as a Challenge and
        Extraction plugin only to take advantage of the login page feature
        but the credentials are not stored in the CookieAuthHelper cookie
        but somewhere else, like in a Session.
        """
    @security.public
    def logout(self, REQUEST) -> None:
        """Publicly accessible method to log out a user"""
    @security.public
    def resetCredentials(self, request, response) -> None:
        """Reset credentials by informing all active resetCredentials plugins"""
    def updateLoginName(self, user_id, login_name) -> None:
        """Update login name of user."""
    @security.public
    def updateOwnLoginName(self, login_name) -> None:
        """Update own login name of authenticated user."""
    def updateAllLoginNames(self, quit_on_first_error: bool = True) -> None:
        """Update login names of all users to their canonical value.

        This should be done after changing the login_transform
        property of PAS.

        You can set quit_on_first_error to False to report all errors
        before quitting with an error.  This can be useful if you want
        to know how many problems there are, if any.
        """

class ResponseCleanup:
    resp: Incomplete
    def __init__(self, resp) -> None: ...
    def __del__(self) -> None: ...

def addPluggableAuthService(
    dispatcher,
    base_profile=None,
    extension_profiles=(),
    create_snapshot: bool = True,
    setup_tool_id: str = "setup_tool",
    REQUEST=None,
) -> None:
    """Add a PluggableAuthService to 'dispatcher'.

    o BBB for non-GenericSetup use.
    """

def addConfiguredPASForm(dispatcher):
    """Wrap the PTF in 'dispatcher', including 'profile_registry' in options."""

def addConfiguredPAS(
    dispatcher,
    base_profile,
    extension_profiles=(),
    create_snapshot: bool = True,
    setup_tool_id: str = "setup_tool",
    REQUEST=None,
) -> None:
    """Add a PluggableAuthService to 'self."""
