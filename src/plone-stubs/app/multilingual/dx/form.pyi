from _typeshed import Incomplete
from z3c.form.validator import StrictSimpleFieldValidator

def isLanguageIndependent(field): ...

class LanguageIndependentFieldValidator(StrictSimpleFieldValidator):
    """Override validator so we can ignore language independent fields,
    these will be automatically filled later on by subscriber.createdEvent
    """
    def validate(self, value, force: bool = False) -> None: ...

class LanguageIndependentFieldInputTemplate:
    """Override input template for language independent fields with
    display widget, because values will be automatically filled
    by later on by subscriber.createdEvent.
    """

    context: Incomplete
    request: Incomplete
    view: Incomplete
    field: Incomplete
    widget: Incomplete
    def __init__(self, context, request, view, field, widget) -> None: ...
    def __call__(self, widget): ...

class ValueBase:
    context: Incomplete
    request: Incomplete
    field: Incomplete
    form: Incomplete
    widget: Incomplete
    def __init__(self, context, request, form, field, widget) -> None: ...
    @property
    def catalog(self): ...

class AddingLanguageIndependentValue(ValueBase):
    def getTranslationUuid(self): ...
    def get(self): ...
