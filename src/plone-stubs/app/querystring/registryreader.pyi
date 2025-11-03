from _typeshed import Incomplete

logger: Incomplete

class DottedDict(dict):
    """A dictionary where you can access nested dicts with dotted names"""
    def get(self, k, default=None): ...

class QuerystringRegistryReader:
    """Adapts a registry object to parse the querystring data."""

    prefix: str
    context: Incomplete
    vocab_context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def parseRegistry(self):
        """Make a dictionary structure for the values in the registry"""
    def getVocabularyValues(self, values):
        """Get all vocabulary values if a vocabulary is defined"""
    def mapOperations(self, values):
        """Get the operations from the registry and put them in the key
        'operators' with the short name as key
        """
    def mapSortableIndexes(self, values):
        """Map sortable indexes"""
    def __call__(self):
        """Return the registry configuration in JSON format"""
