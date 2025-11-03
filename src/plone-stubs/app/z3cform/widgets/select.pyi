from _typeshed import Incomplete
from collections.abc import Generator
from plone.app.z3cform.widgets.base import HTMLInputWidget
from plone.app.z3cform.widgets.base import HTMLSelectWidget
from z3c.form.browser.select import SelectWidget as SelectWidgetBase
from z3c.form.widget import Widget

class SelectWidget(HTMLSelectWidget, SelectWidgetBase):
    klass: str
    @property
    def items(self):
        """
        Optionally handle ITreeVocabulary vocabs as dicts.
        """

def SelectFieldWidget(field, request, extra=None): ...
def CollectionChoiceSelectFieldWidget(field, value_type, request):
    """IFieldWidget factory for SelectWidget."""

class Select2Widget(SelectWidget):
    """Select widget for z3c.form."""

    pattern: str
    separator: str
    noValueToken: str
    noValueMessage: str
    orderable: bool
    def get_pattern_options(self): ...
    def extract(self, default=...):
        """Override extract to handle delimited response values.
        Skip the vocabulary validation provided in the parent
        method, since it's not ever done for single selects."""

def Select2FieldWidget(field, request): ...

class AjaxSelectWidget(HTMLInputWidget, Widget):
    """Ajax select widget for z3c.form."""

    pattern: str
    separator: str
    vocabulary: Incomplete
    vocabulary_view: str
    orderable: bool
    def get_vocabulary(self): ...
    def display_items(self) -> Generator[Incomplete]: ...
    def has_multiple_values(self): ...
    def update(self) -> None: ...
    def get_pattern_options(self): ...

def AjaxSelectFieldWidget(field, request, extra=None): ...
