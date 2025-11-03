from _typeshed import Incomplete
from z3c.form.browser.text import TextWidget
from z3c.form.interfaces import ITextWidget

_: Incomplete

class IEmailWidget(ITextWidget):
    """Email Widget"""

class EmailWidget(TextWidget):
    klass: str
    value: Incomplete

def EmailFieldWidget(field, request): ...
