from _typeshed import Incomplete
from plone.app.textfield.widget import RichTextWidget as patext_RichTextWidget
from plone.app.z3cform.widgets.base import HTMLTextAreaWidget

logger: Incomplete

def get_tinymce_options(context, field, request):
    """
    We're just going to be looking up settings from
    plone pattern options
    """

class RichTextWidgetBase(HTMLTextAreaWidget, patext_RichTextWidget):
    @property
    def richtext_value(self): ...

class RichTextWidget(RichTextWidgetBase):
    klass: str
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def pattern(self):
        """dynamically grab the actual pattern name so it will
        work with custom visual editors"""
    def get_pattern_options(self): ...
    def render(self):
        """Render widget.

        :returns: Widget's HTML.
        :rtype: string
        """
    def render_input_mode(self): ...

def tinymce_richtextwidget_render(widget): ...
def RichTextFieldWidget(field, request): ...
