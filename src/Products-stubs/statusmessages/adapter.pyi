from _typeshed import Incomplete

logger: Incomplete

class StatusMessage:
    """Adapter for the BrowserRequest to handle status messages.

    Let's make sure that this implementation actually fulfills the
    'IStatusMessage' API::

        >>> from zope.interface.verify import verifyClass
        >>> verifyClass(IStatusMessage, StatusMessage)
        True
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def add(self, text, type: str = "info") -> None:
        """Add a status message."""
    def show(self):
        """Removes all status messages and returns them for display."""
    addStatusMessage = add
    showStatusMessages = show
