from Products.CMFDiffTool.BaseDiff import BaseDiff

class FieldDiff(BaseDiff):
    """Text difference"""

    meta_type: str
    same_fmt: str
    inlinediff_fmt: str
    def getLineDiffs(self): ...
    def testChanges(self, ob) -> None:
        """
        Test the specified object to determine if the change set
        will apply without errors
        """
    def applyChanges(self, ob) -> None:
        """Update the specified object with the difference"""
    def ndiff(self):
        """Return a textual diff"""
    def inline_diff(self): ...

def dump(tag, x, lo, hi, r) -> None: ...
def plain_replace(a, alo, ahi, b, blo, bhi, r) -> None: ...
