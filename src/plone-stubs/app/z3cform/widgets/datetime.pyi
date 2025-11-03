from _typeshed import Incomplete
from plone.app.z3cform.widgets.base import HTMLTextInputWidget
from z3c.form.widget import Widget

def get_date_options(request): ...

class DateTimeWidgetBase(HTMLTextInputWidget, Widget):
    default_timezone: Incomplete
    default_time: str
    @property
    def attributes(self): ...
    def get_pattern_options(self): ...
    def render(self):
        """Render widget.

        :returns: Widget's HTML.
        :rtype: string
        """

class DateWidget(DateTimeWidgetBase):
    """Date widget for z3c.form."""

    pattern: str
    klass: str

def DateFieldWidget(field, request): ...

class DatetimeWidget(DateTimeWidgetBase):
    """Datetime widget for z3c.form."""

    pattern: str
    klass: str

def DatetimeFieldWidget(field, request): ...

class TimeWidget(DateTimeWidgetBase):
    """TimeWidget for z3c.form."""

    klass: str
    pattern: str

def TimeFieldWidget(field, request): ...
