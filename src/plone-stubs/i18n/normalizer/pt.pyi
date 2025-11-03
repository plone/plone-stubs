from _typeshed import Incomplete

mapping: Incomplete

class Normalizer:
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(INormalizer, Normalizer)
      True

      >>> norm = Normalizer()
      >>> norm.normalize(u'ã')
      'ã'
      >>> norm.normalize(u'ê')
      'ê'
      >>> norm.normalize(u'õ')
      'õ'
      >>> norm.normalize(u'ç')
      'ç'
    """
    def normalize(self, text, locale=None, max_length=None):
        """
        Returns a normalized text. text has to be a unicode string.
        """

normalizer: Incomplete
