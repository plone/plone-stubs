from plone.app.z3cform.widgets.base import HTMLInputWidget
from z3c.form.browser.radio import RadioWidget as RadioWidgetBase

class RadioWidget(HTMLInputWidget, RadioWidgetBase):
    """Implementation of radio widget."""

    klass: str
    def update(self) -> None: ...

def RadioFieldWidget(field, request): ...
