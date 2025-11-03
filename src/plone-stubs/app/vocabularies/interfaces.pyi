from _typeshed import Incomplete
from zope.interface import Interface
from zope.schema.interfaces import IVocabularyTokenized

class ITermWithDescription(Interface):
    """A term which carries an additional description"""

    description: Incomplete

class IBrowsableTerm(Interface):
    """A term which may be browsed. This interface is only applied to
    terms which are actually browsable (e.g. those representing folders).
    """

    browse_token: Incomplete
    parent_token: Incomplete

class ISlicableVocabulary(IVocabularyTokenized):
    def __getitem__(start, stop) -> None:
        """return a slice of the results"""

class IPermissiveVocabulary(IVocabularyTokenized):
    """Vocabulary with permissive validation of containment"""
    def __contains__(self, value) -> bool:
        """
        Always returns true, for any value; useful for cases where
        validation of containment creates practical problems (e.g.
        vocabulary about to be mutated with insertion of a value not
        yet within).
        """
