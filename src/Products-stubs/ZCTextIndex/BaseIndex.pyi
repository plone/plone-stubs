from Persistence import Persistent

SCALE_FACTOR: float

def scaled_int(f, scale=...): ...
def unique(l):
    """Return a list of the unique elements in l."""

class BaseIndex(Persistent):
    def __init__(self, lexicon) -> None: ...
    def length(self):
        """Return the number of words in the index."""
    def document_count(self):
        """Return the number of documents in the index"""
    def get_words(self, docid):
        """Return a list of the wordids for a given docid."""
    def index_doc(self, docid, text): ...
    def has_doc(self, docid): ...
    def unindex_doc(self, docid) -> None: ...
    def search(self, term): ...
    def search_glob(self, pattern): ...
    def search_phrase(self, phrase): ...
    def query_weight(self, terms) -> None: ...
    DICT_CUTOFF: int

def inverse_doc_frequency(term_count, num_items):
    """Return the inverse doc frequency for a term,

    that appears in term_count items in a collection with num_items
    total items.
    """
