from ..plugins.BasePlugin import BasePlugin
from _typeshed import Incomplete
from zope.interface import Interface

class IDomainAuthHelper(Interface):
    """Marker interface."""

class EqualsFilter:
    match_string: Incomplete
    def __init__(self, matchstring) -> None: ...
    def __call__(self, candidate): ...

class StartsWithFilter:
    match_string: Incomplete
    def __init__(self, matchstring) -> None: ...
    def __call__(self, candidate): ...

class EndsWithFilter:
    match_string: Incomplete
    def __init__(self, matchstring) -> None: ...
    def __call__(self, candidate): ...

class RegexFilter:
    regex: Incomplete
    def __init__(self, matchstring) -> None: ...
    def __call__(self, candidate): ...

class IPFilter:
    ip: Incomplete
    def __init__(self, matchstring) -> None: ...
    def __call__(self, candidate): ...

manage_addDomainAuthHelperForm: Incomplete

def manage_addDomainAuthHelper(self, id, title: str = "", REQUEST=None) -> None:
    """Factory method to instantiate a DomainAuthHelper"""

class DomainAuthHelper(BasePlugin):
    """Domain Authentication plugin for the PluggableAuthService"""

    security: Incomplete
    meta_type: str
    zmi_icon: str
    manage_map: Incomplete
    manage_genericmap: Incomplete
    manage_options: Incomplete
    id: Incomplete
    title: Incomplete
    def __init__(self, id, title: str = "") -> None:
        """Initialize a new instance"""
    @security.private
    def extractCredentials(self, request):
        """Extract credentials from 'request'."""
    @security.private
    def authenticateCredentials(self, credentials):
        """Fulfill AuthenticationPlugin requirements"""
    @security.private
    def getRolesForPrincipal(self, user, request=None):
        """Fulfill RolesPlugin requirements"""
    def listMatchTypes(self):
        """Return a sequence of possible match types"""
    def listMappingsForUser(self, user_id: str = ""):
        """List the mappings for a specific user"""
    def manage_addMapping(
        self,
        user_id: str = "",
        match_type: str = "",
        match_string: str = "",
        username: str = "",
        roles=[],
        REQUEST=None,
    ):
        """Add a mapping for a user"""
    def manage_removeMappings(self, user_id: str = "", match_ids=[], REQUEST=None):
        """Remove mappings"""
