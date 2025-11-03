from _typeshed import Incomplete
from plone.base.i18nl10n import datetime_formatvariables as datetime_formatvariables
from plone.base.i18nl10n import monthname_msgid as monthname_msgid
from plone.base.i18nl10n import monthname_msgid_abbr as monthname_msgid_abbr
from plone.base.i18nl10n import name_formatvariables as name_formatvariables
from plone.base.i18nl10n import weekdayname_msgid as weekdayname_msgid
from plone.base.i18nl10n import weekdayname_msgid_abbr as weekdayname_msgid_abbr
from Products.Five import BrowserView

BATCH_DELTA: int
BATCH_SIZE: int
DATEFORMAT_XLATE: Incomplete

def dateformat_xlate(dateformat): ...

class RecurrenceView(BrowserView):
    def __call__(self): ...
    @property
    def json_string(self): ...
    def date_format(self, time, formatstring): ...
