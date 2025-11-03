from _typeshed import Incomplete
from zope.interface import Interface

class IPropertiesTool(Interface):
    """Manage properties of the site as a whole."""

    id: Incomplete
    def editProperties(props) -> None:
        """Change portal settings.

        Permission --  Manage portal
        """
    def smtp_server() -> None:
        """Get local SMTP server.

        Returns -- String
        """

class ISimpleItemWithProperties(Interface): ...
