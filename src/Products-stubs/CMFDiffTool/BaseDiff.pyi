from _typeshed import Incomplete

class BaseDiff:
    """Basic diff type"""

    __allow_access_to_unprotected_subobjects__: int
    meta_type: str
    field: Incomplete
    oldValue: Incomplete
    newValue: Incomplete
    same: Incomplete
    id1: Incomplete
    id2: Incomplete
    label: Incomplete
    schemata: Incomplete
    oldFilename: Incomplete
    newFilename: Incomplete
    def __init__(
        self,
        obj1,
        obj2,
        field,
        id1=None,
        id2=None,
        field_name=None,
        field_label=None,
        schemata=None,
    ) -> None: ...
    def testChanges(self, ob) -> None:
        """Test the specified object to determine if the change set
        will apply without errors"""
    def applyChanges(self, ob) -> None:
        """Update the specified object with the difference"""
    def filenameTitle(self, filename):
        """Translate the filename leading text"""
