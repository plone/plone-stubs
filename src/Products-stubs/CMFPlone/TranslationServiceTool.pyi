from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject
from Products.CMFPlone.PloneBaseTool import PloneBaseTool

class TranslationServiceTool(PloneBaseTool, UniqueObject, SimpleItem):
    """Utility methods to access the translation machinery"""

    id: str
    meta_type: str
    toolicon: str
    security: Incomplete
    def utranslate(self, *args, **kw): ...
    def translate(
        self,
        msgid,
        domain=None,
        mapping=None,
        context=None,
        target_language=None,
        default=None,
    ): ...
    def encode(
        self, m, input_encoding=None, output_encoding=None, errors: str = "strict"
    ): ...
    def asunicodetype(self, m, input_encoding=None, errors: str = "strict"): ...
    def ulocalized_time(
        self,
        time,
        long_format=None,
        time_only=None,
        context=None,
        domain: str = "plonelocales",
        request=None,
    ): ...
    def day_msgid(self, number, format=None):
        """Returns the msgid which can be passed to the translation service
        for l10n of weekday names. Format is either None, 'a' or 's'.

        >>> ttool = TranslationServiceTool()

        >>> ttool.day_msgid(0)
        'weekday_sun'

        >>> ttool.day_msgid(6)
        'weekday_sat'

        >>> ttool.day_msgid(0, format='a')
        'weekday_sun_abbr'

        >>> ttool.day_msgid(3, format='s')
        'weekday_wed_short'
        """
    def month_msgid(self, number, format=None):
        """Returns the msgid which can be passed to the translation service
        for l10n of month names. Format is either '' or 'a' (long or
        abbreviation).

        >>> ttool = TranslationServiceTool()

        >>> ttool.month_msgid(1)
        'month_jan'

        >>> ttool.month_msgid(12)
        'month_dec'

        >>> ttool.month_msgid(6, format='a')
        'month_jun_abbr'
        """
    def month_english(self, number, format=None):
        """Returns the english name of month by number. Format is either '' or
        'a' (long or abbreviation).

        >>> ttool = TranslationServiceTool()

        >>> ttool.month_english(1)
        'January'

        >>> ttool.month_english(1, 'a')
        'Jan'
        """
    def month(self, number, format=None, default=None):
        """Returns a Message with the month name, that can be translated by
        the TAL engine. Format is either None or 'a' (long or abbreviation).
        """
    def weekday_english(self, number, format=None):
        """Returns the english name of a week by number. Format is
        either None, 'a' or 'p'.

        >>> ttool = TranslationServiceTool()

        >>> ttool.weekday_english(0)
        'Sunday'

        >>> ttool.weekday_english(6)
        'Saturday'

        >>> ttool.weekday_english(0, format='a')
        'Sun'

        >>> ttool.weekday_english(3, format='p')
        'Wed.'
        """
