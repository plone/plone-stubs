from _typeshed import Incomplete

logger: Incomplete

def userFolderAddUser(
    self, login, password, roles, domains, groups=None, REQUEST=None, **kw
) -> None: ...
def getGroups(self): ...
def getGroupNames(self): ...
def getGroupIds(self): ...
def getGroup(self, group_id):
    """Like getGroupById in groups tool, but doesn't wrap."""

def getGroupByName(self, name, default=None): ...
def getGroupById(self, id, default=None): ...
def getLocalRolesForDisplay(self, object):
    """This is used for plone's local roles display

    This method returns a tuple (massagedUsername, roles, userType,
    actualUserName).  This method is protected by the 'access content
    information' permission. We may change that if it's too
    permissive...

    A GRUF method originally.
    """

def getUsers(self):
    """
    Return a list of all users from plugins that implement the user
    introspection interface.

    Could potentially be very long.
    """

def canListAllUsers(self): ...
def canListAllGroups(self): ...
def userSetPassword(self, userid, password) -> None:
    """Emulate GRUF 3 call for password set, for use with PwRT."""

def credentialsChanged(self, user, name, new_password) -> None:
    """Notifies the authentication mechanism that this user has changed
    passwords.  This can be used to update the authentication cookie.
    Note that this call should *not* cause any change at all to user
    databases.

    For use by CMFCore.MembershipTool.credentialsChanged
    """

def addRole(self, role) -> None: ...
def getAllLocalRoles(self, context): ...
def authenticate(self, name, password, request):
    """See AccessControl.userfolder:BasicUserFolder.authenticate

    Products.PluggableAuthService.PluggableAuthService does not provide this
    method, BasicUserFolder documents it as "Private UserFolder object
    interface". GRUF does provide the method, so not marked as private.

    should be deprecated in future!
    """

def getUserIds(self):
    """method was used at GRUF and is here for bbb. Not good for many users!
    DEPRECATED
    """

def getUserNames(self):
    """method was used at GRUF and is here for bbb. Not good for many users!
    DEPRECATED
    """

def patch_pas() -> None: ...
