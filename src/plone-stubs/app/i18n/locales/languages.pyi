from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.i18n.locales.languages import ContentLanguageAvailability
from plone.i18n.locales.languages import LanguageAvailability
from plone.i18n.locales.languages import MetadataLanguageAvailability

class Languages(SimpleItem, LanguageAvailability):
    """A base implementation for persistent utilities implementing
    IModifiableLanguageAvailability.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IModifiableLanguageAvailability, Languages)
      True
    """

    languages: Incomplete
    combined: Incomplete
    def __init__(self) -> None: ...
    def getAvailableLanguages(self, combined: bool = False):
        """Returns a sequence of language tags for available languages."""
    def setAvailableLanguages(self, languages, combined: bool = False) -> None:
        """Sets a list of available language tags."""

class ContentLanguages(Languages, ContentLanguageAvailability):
    """A local utility storing a list of available content languages.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IContentLanguages, ContentLanguages)
      True
    """

    id: str
    title: str
    meta_type: str

class MetadataLanguages(Languages, MetadataLanguageAvailability):
    """A local utility storing a list of available metadata languages.

    Let's make sure that this implementation actually fulfills the API.

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IMetadataLanguages, MetadataLanguages)
      True
    """

    id: str
    title: str
    meta_type: str
