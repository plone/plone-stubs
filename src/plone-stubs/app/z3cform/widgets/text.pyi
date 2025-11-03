from plone.app.z3cform.widgets.base import HTMLTextAreaWidget
from plone.app.z3cform.widgets.base import HTMLTextInputWidget
from z3c.form.widget import Widget

class TextWidget(HTMLTextInputWidget, Widget):
    """enhanced text widget"""

    klass: str

def TextFieldWidget(field, request): ...

class TextAreaWidget(HTMLTextAreaWidget, Widget):
    """enhanced textarea widget"""

    klass: str

def TextAreaFieldWidget(field, request): ...

class TextLinesWidget(HTMLTextAreaWidget, Widget):
    """enhanced textarea widget"""

    klass: str

def TextLinesFieldWidget(field, request): ...
def TextLinesFieldWidgetFactory(field, value_type, request): ...
