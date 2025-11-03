from _typeshed import Incomplete
from plone.memoize.view import memoize
from Products.Five import BrowserView

logger: Incomplete
MAX_BATCH_SIZE: int
DEFAULT_PERMISSION: str
DEFAULT_PERMISSION_SECURE: str
PERMISSIONS: Incomplete
TRANSLATED_IGNORED: Incomplete

class VocabLookupException(Exception): ...

class BaseVocabularyView(BrowserView):
    def get_translated_ignored(self): ...
    def get_base_path(self, context): ...
    def __call__(self):
        """
        Accepts GET parameters of:
        name: Name of the vocabulary
        field: Name of the field the vocabulary is being retrieved for
        query: string or json object of criteria and options.
            json value consists of a structure:
                {
                    criteria: object,
                    sort_on: index,
                    sort_order: (asc|reversed)
                }
        attributes: comma separated, or json object list
        batch: {
            page: 1-based page of results,
            size: size of paged results
        }
        """
    def parsed_query(self): ...

class VocabularyView(BaseVocabularyView):
    """Queries a named vocabulary and returns JSON-formatted results."""
    def get_context(self): ...
    def get_vocabulary(self): ...

class SourceView(BaseVocabularyView):
    """Queries a field's source and returns JSON-formatted results."""
    def get_context(self): ...
    @property
    @memoize
    def default_permission(self): ...
    def get_vocabulary(self): ...
