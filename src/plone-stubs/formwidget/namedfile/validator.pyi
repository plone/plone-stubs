from _typeshed import Incomplete
from plone.formwidget.namedfile import _ as _
from plone.namedfile.interfaces import INamedField as INamedField
from z3c.form import validator
from zope.schema import ValidationError

class InvalidState(ValidationError):
    __doc__: Incomplete

class NamedFileWidgetValidator(validator.SimpleFieldValidator):
    def validate(self, value, force: bool = False): ...
