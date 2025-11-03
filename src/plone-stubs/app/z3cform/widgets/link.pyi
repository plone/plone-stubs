from plone.app.z3cform.widgets.base import HTMLTextInputWidget
from z3c.form.widget import Widget

class LinkWidget(HTMLTextInputWidget, Widget):
    """Implementation of enhanced link widget.

    .. note::
        Unlike the others here, this is not a pattern based widget
        and it uses it's own template.
    """
    def pattern_data(self): ...
    def extract(self, default=...): ...

def LinkFieldWidget(field, request): ...
