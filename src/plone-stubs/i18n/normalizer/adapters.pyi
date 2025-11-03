from _typeshed import Incomplete

class UserPreferredFileNameNormalizer:
    """
    An adapter for the HTTPRequest to provide user preferred language
    dependent normalization.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(
      ...     IUserPreferredFileNameNormalizer,
      ...     UserPreferredFileNameNormalizer)
      True
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def normalize(self, text):
        """Returns a normalized Unicode string."""

class UserPreferredURLNormalizer:
    """
    An adapter for the HTTPRequest to provide user preferred language
    dependent normalization.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IUserPreferredURLNormalizer, UserPreferredURLNormalizer)
      True
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def normalize(self, text):
        """Returns a normalized Unicode string."""
