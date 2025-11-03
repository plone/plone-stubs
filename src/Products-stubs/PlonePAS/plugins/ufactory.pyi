from _typeshed import Incomplete
from Products.PluggableAuthService.plugins.BasePlugin import BasePlugin
from Products.PluggableAuthService.PropertiedUser import PropertiedUser

manage_addPloneUserFactoryForm: Incomplete

def manage_addPloneUserFactory(self, id, title: str = "", RESPONSE=None):
    """
    Add a plone user factory
    """

class PloneUserFactory(BasePlugin):
    security: Incomplete
    meta_type: str
    id: Incomplete
    title: Incomplete
    def __init__(self, id, title: str = "") -> None: ...
    @security.private
    def createUser(self, user_id, name): ...

class PloneUser(PropertiedUser):
    security: Incomplete
    def __init__(self, id, login=None) -> None: ...
    @security.public
    def isGroup(self):
        """Return 1 if this user is a group abstraction"""
    @security.public
    def getName(self):
        """Get user's or group's name.
        This is the id. PAS doesn't do prefixes and such like GRUF.
        """
    @security.public
    def getUserId(self):
        """Get user's or group's name.
        This is the id. PAS doesn't do prefixes and such like GRUF.
        """
    @security.public
    def getGroupNames(self):
        """Return ids of this user's groups. GRUF compat."""
    getGroupIds = getGroupNames
    @security.public
    def getPropertysheet(self, id):
        """-> propertysheet (wrapped if supported)"""
    @security.private
    def addPropertysheet(self, id, data) -> None:
        """-> add a prop sheet, given data which is either
        a property sheet or a raw mapping.
        """
    @security.private
    def getOrderedPropertySheets(self): ...
    def getRolesInContext(self, object): ...
    def allowed(self, object, object_roles=None): ...
    def setProperties(self, properties=None, **kw) -> None:
        """Set properties on a given user.

        Accepts either keyword arguments or a mapping for the ``properties``
        argument. The ``properties`` argument will take precedence over
        keyword arguments if both are provided; no merging will occur.
        """
    def getProperty(self, id, default=...): ...
