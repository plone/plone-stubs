from .utils import UniqueObject
from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

class UndoTool(UniqueObject, SimpleItem):
    """This tool is used to undo changes."""

    id: str
    meta_type: str
    zmi_icon: str
    security: Incomplete
    manage_options: Incomplete
    manage_overview: Incomplete
    def listUndoableTransactionsFor(
        self,
        object,
        first_transaction=None,
        last_transaction=None,
        PrincipiaUndoBatchSize=None,
    ):
        """List all transaction IDs the user is allowed to undo on 'object'."""
    @security.public
    def undo(self, object, transaction_info) -> None:
        """
        Undo the list of transactions passed in 'transaction_info',
        first verifying that the current user is allowed to undo them.
        """
