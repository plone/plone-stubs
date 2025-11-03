from z3c.form import converter
from z3c.form import interfaces
from z3c.form.browser import textarea
from z3c.form.browser.textlines import (
    TextLinesFieldWidgetFactory as TextLinesFieldWidgetFactory,
)
from z3c.form.converter import TextLinesConverter

__docformat__: str

class ITextLinesWidget(interfaces.IWidget):
    """Text lines widget."""

class TextLinesWidget(textarea.TextAreaWidget):
    """Input type sequence widget implementation."""

class TextLinesConverter(converter.BaseDataConverter):
    """Data converter for ITextLinesWidget."""
    def toWidgetValue(self, value):
        """Convert from text lines to HTML representation."""
    def toFieldValue(self, value):
        """See interfaces.IDataConverter"""

class TextLinesSetConverter(TextLinesConverter):
    """Data converter for ITextLinesWidget operating on a set."""
    def toWidgetValue(self, value):
        """Convert from text lines to HTML representation."""

class TextLinesFrozenSetConverter(TextLinesConverter):
    """Data converter for ITextLinesWidget operating on a frozenset."""
    def toWidgetValue(self, value):
        """Convert from text lines to HTML representation."""
