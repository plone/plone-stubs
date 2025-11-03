from _typeshed import Incomplete
from Products.PluggableAuthService.plugins.ZODBUserManager import (
    ZODBUserManager as BasePlugin,
)

manage_addUserManagerForm: Incomplete

def manage_addUserManager(dispatcher, id, title=None, REQUEST=None) -> None:
    """Add a UserManager to a Pluggable Auth Service."""

class UserManager(BasePlugin):
    """PAS plugin for managing users. (adds write API)"""

    meta_type: str
    security: Incomplete
    def addUser(self, user_id, login_name, password) -> None:
        """Original ZODBUserManager.addUser, modified to check if
        incoming password is already encrypted.

        This support clean migration from default user source.
        Should go into PAS.
        """
    @security.private
    def doDeleteUser(self, userid):
        """Given a user id, delete that user"""
    @security.private
    def doChangeUser(self, principal_id, password) -> None:
        """Change a user's password"""
    @security.public
    def allowDeletePrincipal(self, principal_id):
        """True iff this plugin can delete a certain user/group.
        This is true if this plugin manages the user.
        """
    @security.public
    def allowPasswordSet(self, principal_id):
        """True iff this plugin can set the password a certain user.
        This is true if this plugin manages the user.
        """
    def getUserIds(self):
        """
        Return a list of user ids
        """
    def getUserNames(self):
        """
        Return a list of usernames
        """
    def getUsers(self):
        """
        Return a list of users
        """
