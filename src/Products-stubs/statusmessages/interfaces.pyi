from _typeshed import Incomplete
from zope.interface import Interface

class IMessage(Interface):
    """A single status message."""

    message: Incomplete
    type: Incomplete

class IStatusMessage(Interface):
    """An adapter for the BrowserRequest to handle status messages."""
    def addStatusMessage(text, type: str = "info") -> None:
        """Add a status message."""
    def add(text, type: str = "info") -> None:
        """Add a status message."""
    def showStatusMessages() -> None:
        """Removes all status messages and returns them for display."""
    def show() -> None:
        """Removes all status messages and returns them for display."""
