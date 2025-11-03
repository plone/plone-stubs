from _typeshed import Incomplete
from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.interfaces import ITextAreaWidget

_: Incomplete

class IJSONFieldWidget(ITextAreaWidget):
    """JSON Widget"""

class JSONWidget(TextAreaWidget):
    klass: str
    value: Incomplete

def JSONFieldWidget(field, request): ...

class JSONDataConverter:
    """A JSON data converter."""

    field: Incomplete
    widget: Incomplete
    def __init__(self, field, widget) -> None: ...
    def toWidgetValue(self, value):
        """See interfaces.IDataConverter"""
    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""
