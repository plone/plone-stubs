from _typeshed import Incomplete

ORDER_ATTR: str

class PartialOrdering:
    """this implementation uses a list to store order information on a
    regular attribute of the folderish object;  explicit ordering
    is supported"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def order(self): ...
    @order.setter
    def order(self, value) -> None: ...
    def notifyAdded(self, id) -> None:
        """see interfaces.py"""
    def notifyRemoved(self, id) -> None:
        """see interfaces.py"""
    def idsInOrder(self, onlyOrderables: bool = False):
        """see interfaces.py"""
    def moveObjectsByDelta(
        self, ids, delta, subset_ids=None, suppress_events: bool = False
    ):
        """see interfaces.py"""
    def moveObjectsUp(self, ids, delta: int = 1, subset_ids=None):
        """see interfaces.py"""
    def moveObjectsDown(self, ids, delta: int = 1, subset_ids=None):
        """see interfaces.py"""
    def moveObjectsToTop(self, ids, subset_ids=None):
        """see interfaces.py"""
    def moveObjectsToBottom(self, ids, subset_ids=None):
        """see interfaces.py"""
    def moveObjectToPosition(self, id, position, suppress_events: bool = False):
        """see interfaces.py"""
    def orderObjects(self, key=None, reverse=None):
        """see interfaces.py"""
    def getObjectPosition(self, id):
        """see interfaces.py"""
