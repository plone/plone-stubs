from _typeshed import Incomplete
from Acquisition import Implicit

logger: Incomplete

class BaseChangeSet(Implicit):
    """A ChangeSet represents the set of differences between two objects"""

    __allow_access_to_unprotected_subobjects__: int
    security: Incomplete
    id: Incomplete
    title: Incomplete
    ob1_path: Incomplete
    ob2_path: Incomplete
    recursive: int
    def __init__(self, id, title: str = "") -> None:
        """ChangeSet constructor"""
    def getId(self):
        """ChangeSet id"""
    def __getitem__(self, key): ...
    same: Incomplete
    def computeDiff(
        self, ob1, ob2, recursive: int = 1, exclude=None, id1=None, id2=None
    ) -> None:
        """Compute the differences from ob1 to ob2 (ie. ob2 - ob1).

        The results can be accessed through getDiffs()"""
    def testChanges(self, ob) -> None:
        """
        Test the specified object to determine if the change set
        will apply without errors
        """
    def applyChanges(self, ob) -> None:
        """Apply the change set to the specified object"""
    def getDiffs(self):
        """
        Returns the list differences between the two objects.

        Each difference is a single object implementing
        the IDifference interface
        """
    def getSubDiffs(self):
        """If the ChangeSet was computed recursively, returns a list
        of ChangeSet objects representing subjects differences

        Each ChangeSet will have the same ID as the objects whose
        difference it represents.
        """
    def getAddedItems(self):
        """If the ChangeSet was computed recursively, returns the list
        of IDs of items that were added.

        A copy of these items is available as a cubject of the ChangeSet
        """
    def getRemovedItems(self):
        """If the ChangeSet was computed recursively, returns the list
        of IDs of items that were removed"""
