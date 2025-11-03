from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from z3c.form import form
from zope.interface import Interface

logger: Incomplete

class FakeEnv:
    def getLogger(self, name): ...
    def shouldPurge(self): ...

def checkFieldName(val): ...

class IAddFieldForm(Interface):
    name: Incomplete
    title: Incomplete
    field_type: Incomplete
    required: Incomplete

class RecordsControlPanel(AutoExtensibleForm, form.Form):
    schema = IAddFieldForm
    ignoreContext: bool
    submitted: bool
    template: Incomplete
    @property
    def action(self): ...
    def updateActions(self) -> None: ...
    def action_addfield(self, action): ...
    def import_registry(self): ...
    def export_registry(self): ...
    @property
    def control_panel_url(self): ...
    prefixes: Incomplete
    records: Incomplete
    def __call__(self): ...
