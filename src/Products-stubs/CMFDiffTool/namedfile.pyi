from _typeshed import Incomplete
from Products.CMFDiffTool.BinaryDiff import BinaryDiff
from Products.CMFDiffTool.ListDiff import ListDiff

FILE_FIELD_TYPES: Incomplete

def named_file_as_str(f): ...
def is_same(old_data, old_filename, new_data, new_filename): ...

class NamedFileBinaryDiff(BinaryDiff):
    field: Incomplete
    label: Incomplete
    schemata: Incomplete
    field_name: Incomplete
    oldValue: Incomplete
    newValue: Incomplete
    id1: Incomplete
    id2: Incomplete
    oldFilename: Incomplete
    newFilename: Incomplete
    same: Incomplete
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
    def inline_diff(self): ...

def make_lists_same_length(s1, s2, dummy_element) -> None: ...

class NamedFileListDiff(ListDiff):
    """Specialization of `ListDiff` to handle lists of files better."""

    same_fmt: str
    inlinediff_fmt: Incomplete
    same: bool
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
    def inline_diff(self): ...
