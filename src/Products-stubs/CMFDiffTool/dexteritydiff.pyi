from _typeshed import Incomplete
from Products.CMFDiffTool.FieldDiff import FieldDiff

FIELDS_AND_DIFF_TYPES_RELATION: Incomplete
FALL_BACK_DIFF_TYPE = FieldDiff
VALUE_TYPES_AND_DIFF_TYPES_RELATION: Incomplete
EXCLUDED_FIELDS: Incomplete

class DexterityCompoundDiff:
    """text difference for Dexterity"""

    meta_type: str
    id1: Incomplete
    id2: Incomplete
    obj1: Incomplete
    def __init__(self, obj1, obj2, field, id1=None, id2=None) -> None: ...
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
