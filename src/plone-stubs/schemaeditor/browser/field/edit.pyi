from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from z3c.form import form
from z3c.form.datamanager import AttributeField
from zope.cachedescriptors.property import Lazy as lazy_property
from zope.interface import Interface
from zope.interface.declarations import ObjectSpecificationDescriptor

class IFieldTitle(Interface):
    title: Incomplete

class FieldTitleAdapter:
    field: Incomplete
    def __init__(self, field) -> None: ...
    title: Incomplete

class IFieldProxy(Interface):
    """Marker interface for field being edited by schemaeditor"""

class FieldProxySpecification(ObjectSpecificationDescriptor):
    def __get__(self, inst, cls=None): ...

class FieldProxy:
    __providedBy__: Incomplete
    __class__: Incomplete
    __dict__: Incomplete
    def __init__(self, context) -> None: ...

class FieldDataManager(AttributeField):
    def get(self): ...
    def set(self, value) -> None: ...

class FieldEditForm(AutoExtensibleForm, form.EditForm):
    id: str
    field: Incomplete
    def __init__(self, context, request) -> None: ...
    def getContent(self): ...
    schema = Interface
    @lazy_property
    def additionalSchemata(self): ...
    @lazy_property
    def label(self): ...
    fields: Incomplete
    def updateFields(self) -> None: ...
    status: Incomplete
    def handleSave(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...
    def redirectToParent(self) -> None: ...

EditView: Incomplete
