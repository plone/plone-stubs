from Products.ZCTextIndex.BaseIndex import BaseIndex

class CosineIndex(BaseIndex):
    def __init__(self, lexicon) -> None: ...
    def query_weight(self, terms): ...

def doc_term_weight(count):
    """Return the doc-term weight for a term that appears count times."""
