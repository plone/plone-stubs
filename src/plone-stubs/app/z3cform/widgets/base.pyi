from _typeshed import Incomplete
from z3c.form.browser import widget
from z3c.form.widget import Widget

class PatternNotImplemented(Exception):
    """Raised when method/property is not implemented"""

class BaseWidget(Widget):
    """Base widget for z3c.form."""

    pattern: Incomplete
    pattern_options: Incomplete
    def render(self):
        """Render widget.

        :returns: Widget's HTML.
        :rtype: string
        """
    def is_subform_widget(self): ...

class PatternFormElement(widget.HTMLFormElement):
    """New implementation of pattern widget with z3c.form extendable attributes"""

    pattern: Incomplete
    pattern_options: Incomplete
    def get_pattern_options(self):
        """override this factory to inject the pattern options as
        "data-<self._klass_prefix><self.pattern>" attribute
        """
    @property
    def attributes(self):
        """add "required" attribute"""
    def update(self) -> None: ...
    def is_subform_widget(self): ...

class HTMLInputWidget(PatternFormElement, widget.HTMLInputWidget):
    """InputWidget with pattern options"""

class HTMLTextInputWidget(PatternFormElement, widget.HTMLTextInputWidget):
    """TextInputWidget with pattern options"""
    def update(self) -> None: ...

class HTMLTextAreaWidget(PatternFormElement, widget.HTMLTextAreaWidget):
    """TextAreaWidget with pattern options"""
    def update(self) -> None: ...

class HTMLSelectWidget(PatternFormElement, widget.HTMLSelectWidget):
    """SelectWidget with pattern options"""

    multiple: str
    def update(self) -> None: ...
