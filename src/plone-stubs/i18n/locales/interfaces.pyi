from zope.i18n.interfaces import ILanguageAvailability as IBaseLanguageAvailability
from zope.interface import Interface

class ICcTLDInformation(Interface):
    """A list of country code top level domains their relevant languages."""
    def getAvailableTLDs(self) -> None:
        """Return a sequence of country code top level domains."""
    def getTLDs(self) -> None:
        """Return a sequence of ccTLDs and their languages."""
    def getLanguagesForTLD(self, tld) -> None:
        """Return the relevant languages for a top level domain."""

class ICountryAvailability(Interface):
    """A list of available countries."""
    def getAvailableCountries(self) -> None:
        """Return a sequence of country tags for available countries."""
    def getCountries(self) -> None:
        """Return a sequence of Country objects for available countries."""
    def getCountryListing(self) -> None:
        """Return a sequence of country code and country name tuples."""

class ILanguageAvailability(IBaseLanguageAvailability):
    """A list of available languages."""
    def getLanguages(self, combined: bool = False) -> None:
        """Return a sequence of Language objects for available languages."""
    def getLanguageListing(self, combined: bool = False) -> None:
        """Return a sequence of language code and language name tuples."""

class IContentLanguageAvailability(ILanguageAvailability):
    """A list of available content languages."""

class IMetadataLanguageAvailability(ILanguageAvailability):
    """A list of available metadata languages."""

class IModifiableLanguageAvailability(ILanguageAvailability):
    """A modifiable list of available languages."""
    def setAvailableLanguages(self, languages, combined: bool = False) -> None:
        """Set a list of available language tags."""

class IModifiableCountryAvailability(ICountryAvailability):
    """A modifiable list of available countries."""
    def setAvailableCountries(self, countries) -> None:
        """Set a list of available country tags."""
