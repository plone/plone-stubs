from _typeshed import Incomplete
from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.converter import BaseDataConverter
from z3c.form.interfaces import ITextAreaWidget

class IRichTextWidget(ITextAreaWidget):
    def allowedMimeTypes() -> None:
        """Get allowed MIME types"""

class RichTextWidget(TextAreaWidget):
    klass: str
    value: Incomplete
    def update(self) -> None: ...
    def wrapped_context(self): ...
    def extract(self, default=...): ...
    def allowedMimeTypes(self): ...
    def getWysiwygEditor(self): ...

def RichTextFieldWidget(field, request):
    """IFieldWidget factory for RichTextWidget."""

class RichTextConverter(BaseDataConverter):
    """Data converter for the RichTextWidget"""
    def toWidgetValue(self, value): ...
    def toFieldValue(self, value): ...

class RichTextAreaConverter(BaseDataConverter):
    """Data converter for the original z3cform TextWidget

    This converter ignores the fact allowed_mime_types might be set,
    because the widget has no way to select it.
    It always assumes the default_mime_type was used.
    """
    def toWidgetValue(self, value): ...
    def toFieldValue(self, value): ...
