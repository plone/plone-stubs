from _typeshed import Incomplete
from z3c.form.browser.text import TextWidget
from z3c.form.interfaces import ITextWidget

class IURIWidget(ITextWidget):
    """URI Widget"""

class URIWidget(TextWidget):
    klass: str
    value: Incomplete

def URIFieldWidget(field, request): ...
