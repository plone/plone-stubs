from plone.app.z3cform.widgets.base import HTMLInputWidget
from z3c.form.browser.checkbox import CheckBoxWidget as CheckBoxWidgetBase

class CheckBoxWidget(HTMLInputWidget, CheckBoxWidgetBase):
    """Implementation checkbox widget."""

    klass: str
    def update(self) -> None: ...

def CheckBoxFieldWidget(field, request): ...
