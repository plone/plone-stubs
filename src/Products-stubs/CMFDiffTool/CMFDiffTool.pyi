from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

class CMFDiffTool(UniqueObject, SimpleItem):
    """ """

    id: str
    meta_type: str
    security: Incomplete
    manage_options: Incomplete
    def __init__(self) -> None: ...
    manage_difftypes: Incomplete
    def manage_editDiffFields(self, updates, REQUEST=None):
        """Edit the portal type fields"""
    def manage_addDiffField(self, pt_name, field, diff, REQUEST=None):
        """Add a new diff field from the ZMI"""
    def setDiffField(self, pt_name, field, diff) -> None:
        """
        Set the diff type for 'field' on the portal type 'pt_name' to 'diff'
        """
    def listDiffTypes(self):
        """List the names of the registered difference types"""
    def getDiffType(self, diff):
        """Return a class corresponding to the specified diff type.
        Instances of the class will implement the IDifference
        interface"""
    def setDiffForPortalType(self, pt_name, mapping) -> None:
        """Set the difference type(self, s) for the specific portal type

        mapping is a dictionary where each key is an attribute or
        method on the given portal type, and the value is the name of
        a difference type."""
    def getDiffForPortalType(self, pt_name):
        """Returns a dictionary where each key is an attribute or
        method on the given portal type, and the value is the name of
        a difference type."""
    def computeDiff(self, ob1, ob2, id1=None, id2=None):
        """Compute the differences between two objects and return the
        results as a list.  Each object in the list will implement the
        IDifference interface"""
    def createChangeSet(self, ob1, ob2, id1=None, id2=None):
        """Returns a ChangeSet object that represents the differences
        between ob1 and ob2 (ie. ob2 - ob1) ."""

def registerDiffType(klass) -> None:
    """Register a class for computing differences.

    Instances of the class must implement the IDifference
    interface."""

def unregisterDiffType(klass) -> None:
    """Register a class for computing differences.

    Instances of the class must implement the IDifference
    interface."""
