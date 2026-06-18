from zope.interface import Interface

class ITranslationServiceTool(Interface):
    """Utility methods to access the translation machinery"""
    def translate(self, *args, **kw) -> None:
        """Translate method to access the translation service
        from restricted code like skins.
        """
    def encode(
        self, m, input_encoding=None, output_encoding=None, errors: str = "strict"
    ) -> None:
        """Encode a give unicode type or string type to string type in encoding
        output_encoding
        """
    def asunicodetype(self, m, input_encoding=None, errors: str = "strict") -> None:
        """Create type unicode from type string"""
    def ulocalized_time(
        self,
        time,
        long_format=None,
        time_only=None,
        context=None,
        domain: str = "plonelocales",
    ) -> None:
        """Returns localized time."""
    def day_msgid(self, number, format: str = "") -> None:
        """Returns the msgid which can be passed to the translation service for
        l10n of weekday names. Format is either '', 'a' or 's'.
        """
    def month_msgid(self, number, format: str = "") -> None:
        """Returns the msgid which can be passed to the translation service for
        l10n of month names. Format is either '' or 'a' (long or
        abbreviation).
        """
    def month_english(self, number, format: str = "") -> None:
        """Returns the english name of month by number. Format is either '' or
        'a' (long or abbreviation).
        """
    def weekday_english(self, number, format: str = "") -> None:
        """Returns the english name of a week by number. Format is either '',
        'a' or 'p'.
        """
