from .utils import UniqueObject
from _typeshed import Incomplete
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent

class MemberDataTool(UniqueObject, SimpleItem, PropertyManager):
    """This tool wraps user objects, making them act as Member objects."""

    id: str
    meta_type: str
    zmi_icon: str
    email: str
    fullname: str
    last_login_time: Incomplete
    listed: bool
    login_time: Incomplete
    portal_skin: str
    security: Incomplete
    manage_options: Incomplete
    manage_overview: Incomplete
    manage_showContents: Incomplete
    def __init__(self) -> None: ...
    @security.private
    def getMemberDataContents(self):
        """
        Return the number of members stored in the _members
        BTree and some other useful info
        """
    @security.private
    def searchMemberData(self, search_param, search_term, attributes=()):
        """Search members."""
    @security.private
    def searchMemberDataContents(self, search_param, search_term):
        """Search members. This method will be deprecated soon."""
    @security.private
    def pruneMemberDataContents(self) -> None:
        """Delete data contents of all members not listet in acl_users."""
    @security.private
    def wrapUser(self, u):
        """
        If possible, returns the Member object that corresponds
        to the given User object.
        """
    @security.private
    def registerMemberData(self, m, id) -> None:
        """Add the given member data to the _members btree."""
    @security.private
    def deleteMemberData(self, member_id):
        """Delete member data of specified member."""

class MemberData(Persistent):
    id: Incomplete
    def __init__(self, id) -> None: ...

class MemberAdapter:
    """Member data adapter."""

    security: Incomplete
    __parent__: Incomplete
    def __init__(self, user, tool) -> None: ...
    @security.private
    def notifyModified(self) -> None: ...
    @security.public
    def getUser(self): ...
    @security.public
    def getMemberId(self): ...
    def setProperties(self, properties=None, **kw) -> None:
        """Allows the authenticated member to set his/her own properties.
        Accepts either keyword arguments or a mapping for the "properties"
        argument.
        """
    @security.private
    def setMemberProperties(self, mapping) -> None:
        """Sets the properties of the member."""
    @security.public
    def getProperty(self, id, default=...): ...
    @security.private
    def getPassword(self):
        """Return the password of the user."""
    @security.private
    def setSecurityProfile(self, password=None, roles=None, domains=None) -> None:
        """Set the user's basic security profile"""
    @security.public
    def getId(self):
        """Get the ID of the user."""
    @security.public
    def getUserName(self):
        """Get the name used by the user to log into the system."""
    @security.public
    def getRoles(self):
        """Get a sequence of the global roles assigned to the user."""
    @security.public
    def getRolesInContext(self, object):
        """Get a sequence of the roles assigned to the user in a context."""
    @security.public
    def getDomains(self):
        """Get a sequence of the domain restrictions for the user."""
    @security.public
    def has_role(self, roles, object=None):
        """Check to see if a user has a given role or roles."""
