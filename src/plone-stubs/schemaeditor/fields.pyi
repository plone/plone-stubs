from _typeshed import Incomplete
from z3c.form import validator

def getFirstFieldSchema(field): ...

class FieldFactory:
    title: str
    fieldcls: Incomplete
    args: Incomplete
    kw: Incomplete
    def __init__(self, fieldcls, title, *args, **kw) -> None: ...
    def __call__(self, *args, **kw): ...
    def available(self):
        """field is addable in the current context"""
    def editable(self, field):
        """test whether a given instance of a field is editable"""
    def protected(self, field):
        """test whether a given instance of a field is protected"""

def FieldsVocabularyFactory(context): ...

TextLineFactory: Incomplete
TextFactory: Incomplete
IntFactory: Incomplete
FloatFactory: Incomplete
BoolFactory: Incomplete
PasswordFactory: Incomplete
DatetimeFactory: Incomplete
DateFactory: Incomplete

def getChoiceFieldSchema(field): ...

ChoiceFactory: Incomplete

class TextLineChoiceField:
    def __init__(self, field) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...
    def __delattr__(self, name): ...

class VocabularyValuesValidator(validator.SimpleFieldValidator):
    """Ensure duplicate vocabulary terms are not submitted"""
    def validate(self, values): ...

class VocabularyNameValidator(validator.SimpleFieldValidator):
    """Ensure user has not submitted a vocabulary values AND a factory"""
    def validate(self, values): ...

def getMultiChoiceFieldSchema(field): ...

MultiChoiceFactory: Incomplete

class TextLineMultiChoiceField(TextLineChoiceField):
    def __init__(self, field) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...

def setBoolWidget(field, event) -> None: ...
