from Products.CMFDiffTool.TextDiff import TextDiff

class CMFDTHtmlDiff(TextDiff):
    """Text difference"""

    meta_type: str
    def inline_diff(self):
        """Return a specialized diff for HTML"""
