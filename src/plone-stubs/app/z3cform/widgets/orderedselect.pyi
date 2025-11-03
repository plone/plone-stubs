from plone.app.z3cform.widgets.base import HTMLSelectWidget
from z3c.form.browser.orderedselect import (
    OrderedSelectWidget as OrderedSelectWidgetBase,
)

class OrderedSelectWidget(HTMLSelectWidget, OrderedSelectWidgetBase):
    """Implementation of radio widget."""

    klass: str

def OrderedSelectFieldWidget(field, request): ...
def SequenceChoiceSelectFieldWidget(field, value_type, request):
    """IFieldWidget factory for SelectWidget."""
