from _typeshed import Incomplete
from Products.PluginIndexes.unindex import UnIndex

class FieldIndex(UnIndex):
    """Index for simple fields."""

    meta_type: str
    query_options: Incomplete
    manage_options: Incomplete
    manage: Incomplete
    manage_main: Incomplete
    manage_browse: Incomplete

manage_addFieldIndexForm: Incomplete

def manage_addFieldIndex(self, id, extra=None, REQUEST=None, RESPONSE=None, URL3=None):
    """Add a field index"""
