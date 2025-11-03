from AccessControl.users import BasicUser

class PropertiedUser(BasicUser):
    """User objects which manage propertysheets, obtained from decorators."""
    def __init__(self, id, login=None) -> None: ...
    def getId(self):
        """-> user ID"""
    def getUserName(self):
        """-> login name"""
    def getRoles(self):
        """-> [role]

        o Include only "global" roles.
        """
    def getGroups(self):
        """-> [group]

        o Return the groups the user is in.
        """
    def getDomains(self):
        """-> [domain]

        o The list represents the only domains from which the user is
          allowed to access the system.
        """
    def getRolesInContext(self, object):
        """Return the list of roles assigned to the user.

        o Include local roles assigned in context of the passed-in object.

        o Include *both* local roles assigned directly to us *and* those
          assigned to our groups.

        o Ripped off from AccessControl.User.BasicUser, which provides
          no other extension mechanism. :(
        """
    def allowed(self, object, object_roles=None):
        """Check whether the user has access to object.

        o The user must have one of the roles in object_roles to allow access.

        o Include *both* local roles assigned directly to us *and* those
          assigned to our groups.

        o Ripped off from AccessControl.User.BasicUser, which provides
          no other extension mechanism. :(
        """
    def listPropertysheets(self):
        """-> [propertysheet_id]"""
    def getPropertysheet(self, id):
        """id -> sheet

        o Raise KeyError if no such seet exists.
        """
    __getitem__ = getPropertysheet
    def addPropertysheet(self, id, data) -> None:
        """Add a new propertysheet.

        o Raise KeyError if a sheet of the given ID already exists.
        """
