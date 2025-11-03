from _typeshed import Incomplete
from plone.formwidget.recurrence import _ as _
from z3c.form.interfaces import IWidget
from zope.schema import ValidationError
from zope.schema.interfaces import IText

class IRecurrenceField(IText): ...
class IRecurrenceWidget(IWidget): ...

class RecurrenceValidationError(ValidationError):
    __doc__: Incomplete
