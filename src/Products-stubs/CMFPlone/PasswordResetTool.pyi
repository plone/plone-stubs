from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

module_security: Incomplete

class InvalidRequestError(Exception):
    """Request reset URL is invalid"""

    value: Incomplete
    def __init__(self, value: str = "") -> None: ...

class ExpiredRequestError(InvalidRequestError):
    """Request reset URL is expired"""

class PasswordResetTool(UniqueObject, SimpleItem):
    """Provides a default implementation for a password reset scheme.

    From a 'forgotten password' template, you submit your username to
    a handler script that does a 'requestReset', and sends an email
    with an unguessable unique hash in a url as built by 'constructURL'
    to the user.

    The user visits that URL (the 'reset form') and enters their username,
    """

    id: str
    meta_type: str
    security: Incomplete
    def __init__(self) -> None: ...
    def requestReset(self, userid):
        """Ask the system to start the password reset procedure for
        user 'userid'.

        Returns a dictionary with the random string that must be
        used to reset the password in 'randomstring', the expiration date
        as a datetime in 'expires', and the userid (for convenience) in
        'userid'. Returns None if no such user.
        """
    @security.public
    def resetPassword(self, userid, randomstring, password) -> None:
        """Set the password (in 'password') for the user who maps to
        the string in 'randomstring' iff the entered 'userid' is equal
        to the mapped userid. (This can be turned off with the
        'toggleUserCheck' method.)

        Note that this method will *not* check password validity: this
        must be done by the caller.

        Throws an 'ExpiredRequestError' if request is expired.
        Throws an 'InvalidRequestError' if no such record exists,
        or 'userid' is not in the record.
        """
    def setExpirationTimeout(self, timedelta) -> None:
        """Set the length of time a reset request will be valid in days."""
    @security.public
    def getExpirationTimeout(self):
        """Get the length of time a reset request will be valid."""
    @security.public
    def checkUser(self):
        """Returns a boolean representing the state of 'user check' as described
        in 'toggleUserCheck'. True means on, and is the default."""
    @security.public
    def verifyKey(self, key) -> None:
        """Verify a key. Raises an exception if the key is invalid or expired."""
    @security.private
    def clearExpired(self, days: int = 0) -> None:
        """Destroys all expired reset request records.
        Parameter controls how many days past expired it must be to disappear.
        """
    @security.private
    def uniqueString(self, userid):
        """Returns a string that is random and unguessable, or at
        least as close as possible.

        This is used by 'requestReset' to generate the auth
        string. Override if you wish different format.

        This implementation ignores userid and simply generates a
        UUID. That parameter is for convenience of extenders, and
        will be passed properly in the default implementation.
        """
    @security.private
    def expirationDate(self):
        """Returns a DateTime for exipiry of a request from the
        current time.

        This is used by housekeeping methods (like clearEpired)
        and stored in reset request records."""
    @security.private
    def getValidUser(self, userid):
        """Returns the member with 'userid' if available and None otherwise."""
    @security.private
    def expired(self, dt, now=None):
        """Tells whether a DateTime or timestamp 'datetime' is expired
        with regards to either 'now', if provided, or the current
        time."""
