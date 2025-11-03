from Products.CMFDiffTool.FieldDiff import FieldDiff

class BinaryDiff(FieldDiff):
    """Simple binary difference"""

    meta_type: str
    inlinediff_fmt: str
    def testChanges(self, ob) -> None:
        """
        Test the specified object to determine if the change set will
        apply without errors
        """
    def applyChanges(self, ob) -> None:
        """Update the specified object with the difference"""
    def inline_diff(self):
        """Simple inline diff that just checks that the filename
        has changed."""
