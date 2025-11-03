from .utils import UniqueObject
from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

class RegistrationTool(UniqueObject, SimpleItem):
    """Create and modify users by making calls to portal_membership."""

    id: str
    meta_type: str
    member_id_pattern: str
    default_member_id_pattern: str
    security: Incomplete
    manage_options: Incomplete
    manage_overview: Incomplete
    manage_configuration: Incomplete
    def manage_editIDPattern(self, pattern, REQUEST=None):
        """Edit the allowable member ID pattern TTW"""
    def getIDPattern(self):
        """Return the currently-used member ID pattern"""
    def getDefaultIDPattern(self):
        """Return the currently-used member ID pattern"""
    @security.public
    def isRegistrationAllowed(self, REQUEST):
        """Returns a boolean value indicating whether the user
        is allowed to add a member to the portal.
        """
    @security.public
    def testPasswordValidity(self, password, confirm=None) -> None:
        """If the password is valid, returns None.  If not, returns
        a string explaining why.
        """
    @security.public
    def testPropertiesValidity(self, new_properties, member=None) -> None:
        """If the properties are valid, returns None.  If not, returns
        a string explaining why.
        """
    @security.public
    def generatePassword(self):
        """Generate a valid password."""
    def addMember(
        self,
        id,
        password,
        roles=("Member",),
        domains: str = "",
        properties=None,
        REQUEST=None,
    ): ...
    def isMemberIdAllowed(self, id):
        """Returns 1 if the ID is not in use and is not reserved."""
    @security.public
    def afterAdd(self, member, id, password, properties) -> None:
        """Called by portal_registration.addMember()
        after a member has been added successfully."""
    def mailPassword(self, forgotten_userid, REQUEST) -> None:
        """Email a forgotten password to a member.  Raises an exception
        if user ID is not found.
        """
