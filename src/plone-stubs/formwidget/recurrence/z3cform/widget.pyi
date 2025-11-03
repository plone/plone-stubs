from _typeshed import Incomplete
from plone.formwidget.recurrence.browser.i18n import translations as translations
from plone.formwidget.recurrence.z3cform.interfaces import (
    IRecurrenceField as IRecurrenceField,
)
from plone.formwidget.recurrence.z3cform.interfaces import (
    IRecurrenceWidget as IRecurrenceWidget,
)
from z3c.form.browser.textarea import TextAreaWidget

class RecurrenceWidget(TextAreaWidget):
    klass: str
    value: str
    start_field: Incomplete
    show_repeat_forever: bool
    def site_url(self): ...
    @property
    def read_only(self): ...
    def get_start_field(self): ...
    def get_start_date(self): ...
    def first_day(self): ...
    def get_pattern_options(self): ...

def RecurrenceFieldWidget(field, request): ...
