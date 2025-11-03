from _typeshed import Incomplete
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from ZODB.PersistentMapping import PersistentMapping

_: Incomplete

def manage_addZODBMutablePropertyProvider(
    self, id, title: str = "", RESPONSE=None, schema=None, **kw
) -> None:
    """
    Create an instance of a mutable property manager.
    """

manage_addZODBMutablePropertyProviderForm: Incomplete

def isStringType(data): ...

class ZODBMutablePropertyProvider(BasePlugin):
    """Storage for mutable properties in the ZODB for users/groups.

    API sounds like it's only for users, but groups work as well.
    """

    meta_type: str
    security: Incomplete
    id: Incomplete
    title: Incomplete
    def __init__(self, id, title: str = "", schema=None, **kw) -> None:
        """Create in-ZODB mutable property provider.

        Provide a schema either as a list of (name,type,value) tuples
        in the 'schema' parameter or as a series of keyword parameters
        'name=value'. Types will be guessed in this case.

        The 'value' is meant as the default value, and will be used
        unless the user provides data.

        If no schema is provided by constructor, the properties of the
        portal_memberdata object will be used.

        Types available: string, text, boolean, int, long, float, lines, date
        """
    @security.private
    def getPropertiesForUser(self, user, request=None):
        """Get property values for a user or group.
        Returns a dictionary of values or a PropertySheet.

        This implementation will always return a MutablePropertySheet.

        NOTE: Must always return something, or else the property sheet
        won't get created and this will screw up portal_memberdata.
        """
    @security.private
    def setPropertiesForUser(self, user, propertysheet) -> None:
        """Set the properties of a user or group based on the contents of a
        property sheet.
        """
    @security.private
    def deleteUser(self, user_id) -> None:
        """Delete all user properties"""
    @security.private
    def testMemberData(self, memberdata, criteria, exact_match: bool = False):
        """Test if a memberdata matches the search criteria."""
    @security.private
    def enumerateUsers(self, id=None, login=None, exact_match: bool = False, **kw):
        """See IUserEnumerationPlugin."""
    def updateUser(self, user_id, login_name) -> None:
        """Update the login name of the user with id user_id.

        This is a new part of the IUserEnumerationPlugin interface, but
        not interesting for us.
        """
    def updateEveryLoginName(self, quit_on_first_error: bool = True) -> None:
        """Update login names of all users to their canonical value.

        This is a new part of the IUserEnumerationPlugin interface, but
        not interesting for us.
        """

class PersistentProperties(PersistentMapping): ...
