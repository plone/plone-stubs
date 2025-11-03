from plone.app.z3cform.widgets.base import HTMLTextInputWidget
from z3c.form.widget import Widget

class PasswordWidget(HTMLTextInputWidget, Widget):
    """enhanced text widget"""

    klass: str

def PasswordFieldWidget(field, request): ...
