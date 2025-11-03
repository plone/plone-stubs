from plone.app.z3cform.widgets.base import HTMLTextInputWidget
from z3c.form.widget import Widget

def get_querystring_options(context, querystring_view): ...

class QueryStringWidget(HTMLTextInputWidget, Widget):
    """QueryString widget for z3c.form."""

    pattern: str
    querystring_view: str
    def get_pattern_options(self):
        """querystring pattern options"""

def QueryStringFieldWidget(field, request, extra=None): ...
