from _typeshed import Incomplete
from plone.autoform.view import WidgetsView
from plone.supermodel import model
from zope.interface import Interface

class IRichText(Interface): ...

class IRichTextBehavior(model.Schema):
    text: Incomplete

class RichText:
    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def text(self): ...
    @text.setter
    def text(self, value) -> None: ...

class WidgetView(WidgetsView):
    schema = IRichTextBehavior
