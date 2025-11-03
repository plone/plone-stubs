from _typeshed import Incomplete
from OFS.PropertyManager import PropertyManager
from Products.PluginIndexes.unindex import UnIndex
from zope.interface import Interface

LOG: Incomplete

class IDateRecurringIndex(Interface):
    attr_recurdef: Incomplete
    attr_until: Incomplete

class DateRecurringIndex(UnIndex, PropertyManager):
    """Index for dates with recurrence support."""

    meta_type: str
    query_options: Incomplete
    manage_main: Incomplete
    manage_browse: Incomplete
    manage_options: Incomplete
    attr_recurdef: Incomplete
    attr_until: Incomplete
    def __init__(
        self, id, ignore_ex=None, call_methods=None, extra=None, caller=None
    ) -> None:
        """Initialize the index
        @ param extra.recurdef:
        @ param extral.until:
        """
    def index_object(self, documentId, obj, threshold=None):
        """index an object, normalizing the indexed value to an integer

        o Normalized value has granularity of one minute.

        o Objects which have 'None' as indexed value are *omitted*,
          by design.

        o Repeat by recurdef - a RFC2445 reccurence definition string

        """
    def unindex_object(self, documentId) -> None:
        """Carefully unindex the object with integer id 'documentId'"""

manage_addDRIndexForm: Incomplete

def manage_addDRIndex(self, id, extra=None, REQUEST=None, RESPONSE=None, URL3=None):
    """Add a DateRecurringIndex"""
