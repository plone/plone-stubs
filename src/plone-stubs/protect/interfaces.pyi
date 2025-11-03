from zope.interface import Interface

class IAuthenticatorView(Interface):
    def token() -> None:
        """return token value"""
    def authenticator() -> None:
        """Return an xhtml snippet which sets an authenticator.

        This must be included inside a <form> element.
        """
    def verify() -> None:
        """
        Verify if the request contains a valid authenticator.
        """

class IDisableCSRFProtection(Interface):
    """
    Be able to disable on a per-request basis
    """

class IConfirmView(Interface): ...
