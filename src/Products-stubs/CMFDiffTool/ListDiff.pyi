from Products.CMFDiffTool.FieldDiff import FieldDiff

class ListDiff(FieldDiff):
    """Text difference"""

    meta_type: str
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
    def chk_hashable(self, value): ...

class RelationListDiff(FieldDiff):
    meta_type: str
    same_fmt: str
    inlinediff_fmt: str
    def inline_diff(self): ...
    def ndiff(self):
        """Return a textual diff"""
