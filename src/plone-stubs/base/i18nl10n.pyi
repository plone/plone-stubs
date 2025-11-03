from _typeshed import Incomplete

logger: Incomplete
datetime_formatvariables: Incomplete
name_formatvariables: Incomplete
all_formatvariables = datetime_formatvariables | name_formatvariables
ENGLISH_NAMES: Incomplete

def setDefaultDateFormat(localeid, value) -> None: ...
def setDefaultTimeFormat(localeid, value) -> None: ...
def utranslate(
    domain, msgid, mapping=None, context=None, target_language=None, default=None
): ...
def get_formatstring_from_registry(msgid):
    """If the Enabled record is True, return a format string."""

def ulocalized_time(
    time,
    long_format=None,
    time_only: bool = False,
    context=None,
    domain: str = "plonelocales",
    request=None,
    target_language=None,
):
    """unicode aware localized time method (l10n)"""

def monthname_english(number, format=None): ...
def weekdayname_english(number, format=None): ...
def monthname_msgid(number): ...
def monthname_msgid_abbr(number): ...
def weekdayname_msgid(number): ...
def weekdayname_msgid_abbr(number): ...
def weekdayname_msgid_short(number): ...
