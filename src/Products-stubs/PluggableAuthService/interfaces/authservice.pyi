from zope.interface import Interface

class IBasicUser(Interface):
    """Specify the interface called out in AccessControl.User.BasicUser
    as the "Public User object interface", except that \'_getPassword\'
    is *not* part of the contract!
    """
    def getId(self) -> None:
        """Get the ID of the user.

        o The ID can be used, at least from Python, to get the user from
          the user's UserDatabase
        """
    def getUserName(self) -> None:
        """Return the name used by the user to log into the system.

        o Note that this may not be identical to the user's 'getId'
          (to allow users to change their login names without changing
          their identity).
        """
    def getRoles(self) -> None:
        """Return the roles assigned to a user "globally"."""
    def getRolesInContext(self, object) -> None:
        """Return the roles assigned to the user in context of 'object'.

        o Roles include both global roles (ones assigned to the user
          directly inside the user folder) and local roles (assigned
          in context of the passed in object.
        """
    def getDomains(self) -> None:
        """Return the list of domain restrictions for a user."""

class IPropertiedUser(IBasicUser):
    """A user which has property sheets associated with it,
    i.e. a mapping from strings (property sheet ids)
    to objects implementing IPropertySheet
    """
    def addPropertysheet(self, id, data) -> None:
        """Add a new property sheet to the user.

        The property sheet has to be a map or an IPropertySheet instance.
        """
    def listPropertysheets(self) -> None:
        """Return a sequence of property sheet ids

        o for each id in the list getPropertysheet(id)
          returns a IPropertySheet
        """
    def getPropertysheet(self, id) -> None:
        """Return a property sheet for the given id

        o the returned object implements IPropertySheet
          and has the same id as the value passed to this method

        o if there is no property sheet for the given id,
          raise a KeyError

          An alternative way to get the property sheet is via item access,
          i.e. user.getPropertysheet(id) == user[ id ]
        """

class IUserFolder(Interface):
    """Specify the interface called out in AccessControl.User.BasicUserFolder
        as the "Public UserFolder object interface":

    o N.B: "enumeration" methods (\'getUserNames\', \'getUsers\') are *not*
           part of the contract!  See IEnumerableUserFolder.
    """
    def getUser(self, name) -> None:
        """Return the named user object or None."""
    def getUserById(self, id, default=None) -> None:
        """Return the user corresponding to the given id.

        o If no such user can be found, return 'default'.
        """
    def validate(self, request, auth: str = "", roles=...) -> None:
        """Perform identification, authentication, and authorization.

        o Return an IUser-conformant user object, or None if we can't
          identify / authorize the user.

        o 'request' is the request object

        o 'auth' is any credential information already extracted by
          the caller

        o roles is the list of roles the caller
        """

class IPluggableAuthService(IUserFolder):
    """The full, default contract for the pluggable authentication service."""
    def searchUsers(self, **kw) -> None:
        """Search for users.  Returns a sequence of dicts, each dict
        representing a user matching the query, with the keys
        'userid','id', 'login', 'title', and 'principal_type',
        possibly among others.  'principal_type' is always 'user'.

        Possible keywords include the following:

        o id: user id

        o name: user name

        o max_results: an int (or value castable to int) indicating
          the maximum number of results the method should return

        o sort_by: the key in the user dictionary that should be used
          to sort the results

        o login: user login
        """
    def searchGroups(self, **kw) -> None:
        """Search for groups.  Returns a sequence of dicts, each dict
        representing a group matching the query, with the keys
        'groupid','id', 'title', and 'principal_type', possibly among
        others.  'principal_type' is always 'group'.

        Possible keywords include the following:

        o id: user id

        o name: user name

        o max_results: an int (or value castable to int) indicating
          the maximum number of results the method should return

        o sort_by: the key in the user dictionary that should be used
          to sort the results
        """
    def searchPrincipals(self, groups_first: bool = False, **kw) -> None:
        """Search for principals (users, groups, or both).  Returns a
        sequence of dicts, each dict representing a principal (group
        or user) matching the query.  groups will be represented with
        dictionaries as described in searchGroups, and users as
        described in searchUsers.  Possible keywords include id, name,
        max_results, sort_by, and login.
        """
    def updateCredentials(self, request, response, login, new_password) -> None:
        """Central updateCredentials method

        This method is needed for cases where the credentials storage
        and the credentials extraction is handled by different
        plugins. Example case would be if the CookieAuthHelper is used
        as a Challenge and Extraction plugin only to take advantage of
        the login page feature but the credentials are not stored in
        the CookieAuthHelper cookie but somewhere else, like in a
        Session.
        """
    def logout(self, REQUEST) -> None:
        """Publicly accessible method to log out a user. A wrapper
        around resetCredentials that may implement some policy (the
        default implementation redirects to HTTP_REFERER).
        """
    def resetCredentials(self, request, response) -> None:
        """Reset credentials by informing all active resetCredentials
        plugins
        """
    def updateLoginName(self, user_id, login_name) -> None:
        """Update login name of user."""
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

class IMutableUserFolder(Interface):
    """Specify the interface called out in
        AccessControl.User.BasicUserFolder as the
        "Public UserFolder object interface":

    o N.B: "enumeration" methods (\'getUserNames\', \'getUsers\') are *not*
           part of the contract!  See IEnumerableUserFolder.
    """
    def userFolderAddUser(self, name, password, roles, domains, **kw) -> None:
        """Create a new user object."""
    def userFolderEditUser(self, name, password, roles, domains, **kw) -> None:
        """Change user object attributes."""
    def userFolderDelUsers(self, names) -> None:
        """Delete one or more user objects."""

class IEnumerableUserFolder(IUserFolder):
    """Interface for user folders which can afford to enumerate their users."""
    def getUserNames(self) -> None:
        """Return a list of usernames."""
    def getUsers(self) -> None:
        """Return a list of user objects."""
