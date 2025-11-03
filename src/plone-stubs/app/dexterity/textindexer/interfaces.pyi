from zope.interface import Interface

INDEXER_NAMESPACE: str
INDEXER_PREFIX: str

class IDexterityTextIndexFieldConverter(Interface):
    """Interface for a multi-adapter which converts the field value of the
    adapted field into a human readable, translated text for indexing in
    the searchable text index.
    """
    def __init__(self, context, field, widget) -> None:
        """The multi-adpater adapts the context, the field and the widget."""
    def convert(self) -> None:
        """Returns a string containing the words to index. Translatable
        Message-objects are already translated into normal strings. On a
        multi-language site the
        """

class IDynamicTextIndexExtender(Interface):
    """Adapter interface for a named adapter which extends the dynamic
    text indexer.
    """
