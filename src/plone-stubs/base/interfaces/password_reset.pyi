from _typeshed import Incomplete
from zope.interface import Interface

class IPasswordResetToolView(Interface):
    """BrowserView with utility methods"""
    def encode_mail_header(text) -> None:
        """Encodes text into correctly encoded email header"""
    def encoded_mail_sender() -> None:
        """returns encoded version of Portal name <portal_email>"""
    def registered_notify_subject() -> None:
        """returns encoded version of registered notify template subject line"""
    def mail_password_subject() -> None:
        """returns encoded version of mail password template subject line"""

class IPWResetTool(Interface):
    """Defines an interface for a tool that provides a facility to
    reset forgotten passwords.

    This interface is rather sparse, but sufficient to describe the
    task. (In this manner we void being dependent on a specific
    process) The details of the process are in the implementation,
    where they belong."""

    id: Incomplete
    def requestReset(userid) -> None:
        """Ask the system to start the password reset procedure for
        user 'userid'.

        Returns the random string that must be used to reset the
        password."""
    def resetPassword(userid, randomstring, password) -> None:
        """Set the password (in 'password') for the user who maps to
        the string in 'randomstring'. The 'userid' parameter is provided
        in case extra authentication is needed."""
