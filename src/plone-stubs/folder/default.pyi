from _typeshed import Incomplete

class DefaultOrdering:
    """This implementation uses annotations to store the order on the
    object, and supports explicit ordering."""

    ORDER_KEY: str
    POS_KEY: str
    context: Incomplete
    def __init__(self, context) -> None: ...
    def notifyAdded(self, obj_id) -> None:
        """see interfaces.py"""
    def notifyRemoved(self, obj_id) -> None:
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
    def moveObjectToPosition(self, obj_id, position, suppress_events: bool = False):
        """see interfaces.py"""
    def orderObjects(self, key=None, reverse=None):
        """see interfaces.py"""
    def getObjectPosition(self, obj_id):
        """see interfaces.py"""
    def idsInOrder(self):
        """see interfaces.py"""
    def __getitem__(self, index): ...
