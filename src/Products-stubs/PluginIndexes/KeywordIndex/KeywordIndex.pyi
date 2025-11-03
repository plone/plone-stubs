from _typeshed import Incomplete
from Products.PluginIndexes.unindex import UnIndex

LOG: Incomplete

class KeywordIndex(UnIndex):
    """Like an UnIndex only it indexes sequences of items.

    Searches match any keyword.

    This should have an _apply_index that returns a relevance score
    """

    meta_type: str
    query_options: Incomplete
    manage_options: Incomplete
    def unindex_objectKeywords(self, documentId, keywords) -> None:
        """carefully unindex the object with integer id 'documentId'"""
    def unindex_object(self, documentId) -> None:
        """carefully unindex the object with integer id 'documentId'"""
    manage: Incomplete
    manage_main: Incomplete
    manage_browse: Incomplete

manage_addKeywordIndexForm: Incomplete

def manage_addKeywordIndex(
    self, id, extra=None, REQUEST=None, RESPONSE=None, URL3=None
):
    """Add a keyword index"""
