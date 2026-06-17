from _typeshed import Incomplete
from zope.interface import Interface

class IMessage(Interface):
    """A single status message."""

    message: Incomplete
    type: Incomplete

class IStatusMessage(Interface):
    """An adapter for the BrowserRequest to handle status messages."""
    def addStatusMessage(self, text, type: str = "info") -> None:
        """Add a status message."""
    def add(self, text, type: str = "info") -> None:
        """Add a status message."""
    def showStatusMessages(self) -> None:
        """Removes all status messages and returns them for display."""
    def show(self) -> None:
        """Removes all status messages and returns them for display."""
