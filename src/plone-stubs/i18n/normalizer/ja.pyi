from _typeshed import Incomplete

MAX_LENGTH: int
TABLE: str
TABLE_LEN: Incomplete

def ja_normalize(text, max_length=...):
    """
    This function is normalize for Japanese.
    exchange from unicode string to hash and base64 string.
    """

class Normalizer:
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters.

    Let\'s make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(INormalizer, Normalizer)
      True

    Strings that contain only ASCII characters are returned decoded.

      >>> norm = Normalizer()
      >>> text = u"test page"
      >>> norm.normalize(text)
      \'test page\'

    Text that contains non-ASCII characters are normalized.

      >>> norm = Normalizer()
      >>> text = u"公開テストページ"
      >>> normalized = norm.normalize(text)
      >>> all(s in allowed for s in normalized)
      True

    We expect the default length of 6.
    Report the normalized value in case of failure.

      >>> 5 <= len(normalized) <= 6 or (len(normalized), normalized)
      True

    The max_length argument is respected.
      >>> normalized = norm.normalize(text, max_length=8)
      >>> 7 <= len(normalized) <= 8 or (len(normalized), normalized)
      True
    """
    def normalize(self, text, locale=None, max_length=...):
        """
        Returns a normalized text. text has to be a unicode string.
        """

normalizer: Incomplete
