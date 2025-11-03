from _typeshed import Incomplete
from plone.app.dexterity.textindexer.interfaces import INDEXER_NAMESPACE
from plone.app.dexterity.textindexer.interfaces import INDEXER_PREFIX
from zope.interface import Interface

_: Incomplete

class ISearchableTextField(Interface):
    searchable: Incomplete

class SearchableTextField:
    namespace = INDEXER_NAMESPACE
    prefix = INDEXER_PREFIX
    field: Incomplete
    schema: Incomplete
    def __init__(self, field) -> None: ...
    searchable: Incomplete

def get_searchabletext_schema(schema_context, field): ...
