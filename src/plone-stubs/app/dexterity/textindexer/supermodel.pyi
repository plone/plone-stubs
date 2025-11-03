from plone.app.dexterity.textindexer.interfaces import INDEXER_NAMESPACE
from plone.app.dexterity.textindexer.interfaces import INDEXER_PREFIX

class IndexerSchema:
    """Support the indexer: namespace in model definitions."""

    namespace = INDEXER_NAMESPACE
    prefix = INDEXER_PREFIX
    def read(self, fieldNode, schema, field) -> None: ...
    def write(self, fieldNode, schema, field) -> None: ...
