from _typeshed import Incomplete
from AccessControl.Permissions import manage_vocabulary
from AccessControl.Permissions import query_vocabulary
from Acquisition import Implicit
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent
from Products.ZCTextIndex.Lexicon import Lexicon

index_types: Incomplete

class ZCTextIndex(Persistent, Implicit, SimpleItem):
    """Persistent text index."""

    meta_type: str
    zmi_icon: str
    operators: Incomplete
    useOperator: str
    query_options: Incomplete
    manage_options: Incomplete
    security: Incomplete
    id: Incomplete
    lexicon_id: Incomplete
    index: Incomplete
    def __init__(
        self,
        id,
        extra=None,
        caller=None,
        index_factory=None,
        field_name=None,
        lexicon_id=None,
    ) -> None: ...
    @security.private
    def getLexicon(self):
        """Get the lexicon for this index."""
    def query(self, query, nbest: int = 10):
        """Return pair (mapping from docids to scores, num results).

        The num results is the total number of results before trimming
        to the nbest results.
        """
    def index_object(self, documentId, obj, threshold=None):
        """Wrapper for  index_doc()  handling indexing of multiple attributes.

        Enter the document with the specified documentId in the index
        under the terms extracted from the indexed text attributes,
        each of which should yield either a string or a list of
        strings (Unicode or otherwise) to be passed to index_doc().
        """
    def unindex_object(self, docid) -> None: ...
    def query_index(self, record, resultset=None): ...
    def getEntryForObject(self, documentId, default=None):
        """Return the list of words indexed for documentId"""
    def uniqueValues(self, name=None, withLengths: int = 0) -> None: ...
    def numObjects(self):
        """Return number of unique words in the index"""
    def indexSize(self):
        """Return the number of indexes objects"""
    def clear(self) -> None:
        """reinitialize the index (but not the lexicon)"""
    manage_main: Incomplete
    def getIndexSourceNames(self):
        """Return sequence of names of indexed attributes"""
    def getIndexQueryNames(self):
        """Indicate that this index applies to queries for the index's name."""
    def getIndexType(self):
        """Return index type string"""
    def getLexiconURL(self):
        """Return the url of the lexicon used by the index"""

def manage_addZCTextIndex(self, id, extra=None, REQUEST=None, RESPONSE=None):
    """Add a text index"""

manage_addZCTextIndexForm: Incomplete
manage_addLexiconForm: Incomplete

def manage_addLexicon(self, id, title: str = "", elements=[], REQUEST=None):
    """Add ZCTextIndex Lexicon"""

LexiconQueryPerm = query_vocabulary
LexiconMgmtPerm = manage_vocabulary

class PLexicon(Lexicon, Implicit, SimpleItem):
    """Lexicon for ZCTextIndex."""

    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    security: Incomplete
    id: Incomplete
    title: Incomplete
    def __init__(self, id, title: str = "", *pipeline) -> None: ...
    def getPipelineNames(self):
        """Return list of names of pipeline element classes"""
    def queryLexicon(
        self, REQUEST, words=None, page: int = 0, rows: int = 20, cols: int = 4
    ):
        """Lexicon browser/query user interface"""
    manage_main: Incomplete
