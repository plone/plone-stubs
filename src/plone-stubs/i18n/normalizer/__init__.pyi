from _typeshed import Incomplete

FILENAME_REGEX: Incomplete
IGNORE_REGEX: Incomplete
NON_WORD_REGEX: Incomplete
DANGEROUS_CHARS_REGEX: Incomplete
URL_DANGEROUS_CHARS_REGEX: Incomplete
MULTIPLE_DASHES_REGEX: Incomplete
EXTRA_DASHES_REGEX: Incomplete
UNDERSCORE_START_REGEX: Incomplete
LOCALE_SPLIT_REGEX: Incomplete
MAX_LENGTH: int
MAX_FILENAME_LENGTH: int
MAX_URL_LENGTH: int

def cropName(base, maxLength=...): ...

class IDNormalizer:
    """
    This normalizer can normalize any unicode string and returns a
    version that only contains of ASCII characters allowed in a typical
    scripting or programming language id, such as CSS class names or Python
    variable names for example.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IIDNormalizer, IDNormalizer)
      True
    """
    def normalize(self, text, locale=None, max_length=...):
        """
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt-BR', 'sr@Latn' or 'de'
        """

class FileNameNormalizer:
    """
    This normalizer can normalize any unicode string and returns a version
    that only contains of ASCII characters allowed in a file name.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IFileNameNormalizer, FileNameNormalizer)
      True
    """
    def normalize(self, text, locale=None, max_length=...):
        """
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt-BR', 'sr@Latn' or 'de'
        """

class URLNormalizer:
    """
    This normalizer can normalize any unicode string and returns a URL-safe
    version that only contains of ASCII characters allowed in a URL.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IURLNormalizer, URLNormalizer)
      True
    """
    def normalize(self, text, locale=None, max_length=...):
        """
        Returns a normalized text. text has to be a unicode string and locale
        should be a normal locale, for example: 'pt-BR', 'sr@Latn' or 'de'
        """

idnormalizer: Incomplete
filenamenormalizer: Incomplete
urlnormalizer: Incomplete
