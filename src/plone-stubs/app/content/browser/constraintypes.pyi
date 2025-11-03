from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from z3c.form import form
from zope.interface import Interface
from zope.interface import invariant

ACQUIRE: int
DISABLED: int
ENABLED: int

def ST(key, title): ...

_: Incomplete
possible_constrain_types: Incomplete

class ValidTypes:
    def __call__(self, context): ...

ValidTypesFactory: Incomplete

class IConstrainForm(Interface):
    constrain_types_mode: Incomplete
    allowed_types: Incomplete
    secondary_types: Incomplete
    @invariant
    def legal_not_immediately_addable(data): ...

class FormContentAdapter:
    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def constrain_types_mode(self): ...
    @property
    def allowed_types(self): ...
    @property
    def secondary_types(self): ...

class ConstrainsFormView(AutoExtensibleForm, form.EditForm):
    schema = IConstrainForm
    label: Incomplete
    template: Incomplete
    def getContent(self): ...
    def updateFields(self) -> None: ...
    def updateWidgets(self) -> None: ...
    def updateActions(self) -> None: ...
    status: Incomplete
    def handleSave(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...
