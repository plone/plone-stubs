from Products.CMFDiffTool.FieldDiff import FieldDiff

class TextDiff(FieldDiff):
    """Text difference"""

    meta_type: str
    inlinediff_fmt: str
    def unified_diff(self):
        """Return a unified diff"""
    def html_diff(self, context: bool = True, wrapcolumn: int = 40):
        """Return an HTML table showing differences"""
    def inline_diff(self):
        """Simple inline diff that just assumes that either the filename
        has changed, or the text has been completely replaced."""

class AsTextDiff(TextDiff):
    """
    Specialization of `TextDiff` that converts any value to text in order to
    provide an inline diff visualization. Also translated (i18n) the
    strings `True` and `False`.
    """
