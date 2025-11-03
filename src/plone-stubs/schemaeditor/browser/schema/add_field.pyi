from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from z3c.form import form
from zope.cachedescriptors.property import Lazy as lazy_property
from zope.interface import Interface

class FieldAddForm(AutoExtensibleForm, form.AddForm):
    fields: Incomplete
    label: Incomplete
    id: str
    schema = Interface
    @lazy_property
    def additionalSchemata(self): ...
    def create(self, data): ...
    def add(self, new_field) -> None: ...
    def updateWidgets(self) -> None: ...
    def nextURL(self): ...

FieldAddFormPage: Incomplete
