from _typeshed import Incomplete
from plone.app.z3cform.widgets.base import HTMLInputWidget
from z3c.form.button import ButtonAction as ButtonActionBase
from z3c.form.widget import Widget

PRIMARY_BUTTON_NAMES: Incomplete

class SubmitWidget(HTMLInputWidget, Widget):
    """submit widget"""

    klass: str
    @property
    def attributes(self): ...
    def update(self) -> None: ...

def SubmitFieldWidget(field, request): ...

class ButtonAction(SubmitWidget, ButtonActionBase):
    """need to subclass ButtonAction here
    to get our SubmitWidget adapter
    """
