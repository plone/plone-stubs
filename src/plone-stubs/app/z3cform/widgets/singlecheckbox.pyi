from _typeshed import Incomplete
from plone.app.z3cform.widgets.base import HTMLInputWidget
from z3c.form.browser.checkbox import SingleCheckBoxWidget

class SingleCheckBoxBoolWidget(HTMLInputWidget, SingleCheckBoxWidget):
    """Single Input type checkbox widget implementation."""

    klass: str
    def update(self) -> None: ...
    @property
    def label(self): ...
    @label.setter
    def label(self, value) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, value) -> None: ...
    terms: Incomplete
    def updateTerms(self): ...
    @property
    def items(self): ...

def SingleCheckBoxBoolFieldWidget(field, request):
    """IFieldWidget factory for CheckBoxWidget."""
