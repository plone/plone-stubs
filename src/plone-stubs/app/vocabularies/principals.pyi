from _typeshed import Incomplete
from zope.schema.vocabulary import SimpleVocabulary

GETTER: Incomplete
SOURCES: Incomplete

def token_from_principal_info(info, prefix: bool = False): ...
def merge_principal_infos(infos, prefix: bool = False): ...

class PrincipalsVocabulary(SimpleVocabulary):
    """Vocabulary dealing with users/ groups (or in theory any other principal)"""
    @property
    def principal_source(self): ...
    @principal_source.setter
    def principal_source(self, value) -> None: ...
    def __contains__(self, value) -> bool:
        """Checks if the principal exists in current subset or in PAS."""
    def getTerm(self, value):
        """Checks also for values not in the current subset.
        This allows to lookup already saved values.
        """
    def getTermByToken(self, token):
        """Checks also for tokens not in the current subset.
        This allows to lookup already saved values by token.
        """
    def __getitem__(self, start, stop=None):
        """Sliceable"""

class BaseFactory:
    """Factory creating a PrincipalsVocabulary"""

    source: Incomplete
    def should_search(self, query):
        """Test if we should search for users"""
    def use_principal_triple(self, principal_triple):
        """Used by ``functools.filter`` to decide if the triple should be used.

        principal_triple
            A triple (value, token, title).
            Like (johndoe, johndoe, 'John Doe') (unprefixed).
            Value might be a prefixed Id by principal_type, like
            (user:johndoe, user__johndoe, 'John Doe') or
            (group:editors, group__editors, 'Editors').

        returns whether the triple shall be included in the vocabulary or not
        (bool).

        Meant to be overridden in subclasses for post-filtering result.
        """
    def __call__(self, context, query: str = ""): ...

class PrincipalsFactory(BaseFactory):
    source: str

class UsersFactory(BaseFactory):
    source: str

class GroupsFactory(BaseFactory):
    source: str
