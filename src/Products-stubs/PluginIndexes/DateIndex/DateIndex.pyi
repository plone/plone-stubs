from _typeshed import Incomplete
from datetime import tzinfo
from OFS.PropertyManager import PropertyManager
from Products.PluginIndexes.unindex import UnIndex

LOG: Incomplete
ZERO: Incomplete
STDOFFSET: Incomplete
DSTOFFSET: Incomplete
DSTOFFSET = STDOFFSET
DSTDIFF: Incomplete
MAX32: Incomplete

class LocalTimezone(tzinfo):
    def utcoffset(self, dt): ...
    def dst(self, dt): ...
    def tzname(self, dt): ...

Local: Incomplete

class DateIndex(UnIndex, PropertyManager):
    """Index for dates."""

    meta_type: str
    query_options: Incomplete
    index_naive_time_as_local: bool
    precision: int
    manage: Incomplete
    manage_main: Incomplete
    manage_browse: Incomplete
    manage_options: Incomplete
    def clear(self) -> None:
        """Complete reset"""

manage_addDateIndexForm: Incomplete

def manage_addDateIndex(self, id, REQUEST=None, RESPONSE=None, URL3=None):
    """Add a Date index"""
