from _typeshed import Incomplete
from zope.schema.vocabulary import SimpleTerm

def safe_encode(value): ...
def safe_simpleterm_from_value(value):
    """create SimpleTerm from an untrusted value.

    - token need cleaned up: Vocabulary term tokens *must* be 7 bit values
    - tokens cannot contain newlines
    - anything for display has to be cleaned up, titles *must* be unicode
    """

def safe_simplevocabulary_from_values(values, query=None):
    """Creates (filtered) SimpleVocabulary from iterable of untrusted values."""

class TermWithDescription(SimpleTerm):
    """
    >>> term = TermWithDescription('value', 'token', 'title')
    >>> term.value, term.token, term.title, term.description
    ('value', 'token', 'title', None)

    >>> term = TermWithDescription('value', 'token', 'title',
    ...                            description='description')
    >>> term.value, term.token, term.title, term.description
    ('value', 'token', 'title', 'description')
    """

    description: Incomplete
    def __init__(self, value, token, title, description=None) -> None: ...

class BrowsableTerm(TermWithDescription):
    """
    >>> term = BrowsableTerm('value')
    >>> term.value, term.token, term.title, term.description
    ('value', 'value', None, None)
    >>> IBrowsableTerm.providedBy(term)
    False

    >>> term = BrowsableTerm('value', 'token', 'title',
    ...                      description='description',
    ...                      browse_token='browse_token',
    ...                      parent_token='parent_token')
    >>> term.value, term.token, term.title, term.description
    ('value', 'token', 'title', 'description')
    >>> term.browse_token, term.parent_token
    ('browse_token', 'parent_token')
    >>> IBrowsableTerm.providedBy(term)
    True
    """

    browse_token: Incomplete
    parent_token: Incomplete
    def __init__(
        self,
        value,
        token=None,
        title=None,
        description=None,
        browse_token=None,
        parent_token=None,
    ) -> None: ...
