from _typeshed import Incomplete

class LanguageAvailability:
    """A list of available languages."""
    def getAvailableLanguages(self, combined: bool = False):
        """Return a sequence of language tags for available languages."""
    def getLanguages(self, combined: bool = False):
        """Return a sequence of Language objects for available languages."""
    def getLanguageListing(self, combined: bool = False):
        """Return a sequence of language code and language name tuples."""

class ContentLanguageAvailability(LanguageAvailability):
    """A list of available content languages."""

contentlanguages: Incomplete

class MetadataLanguageAvailability(LanguageAvailability):
    """A list of available metadata languages."""

metadatalanguages: Incomplete
value: Incomplete
