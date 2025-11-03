from _typeshed import Incomplete
from plone.schemaeditor.fields import FieldFactory
from zope import schema

class RelationFieldFactory(FieldFactory):
    def available(self): ...

class IRelationFieldSettings(schema.interfaces.IField):
    portal_type: Incomplete

def getRelationChoiceEditFormSchema(field): ...

class RelationChoiceEditFormAdapter:
    field: Incomplete
    def __init__(self, field) -> None: ...
    @property
    def portal_type(self): ...
    @portal_type.setter
    def portal_type(self, value) -> None: ...

RelationChoiceFactory: Incomplete

def getRelationListEditFormSchema(field): ...

class RelationListEditFormAdapter:
    field: Incomplete
    def __init__(self, field) -> None: ...
    @property
    def portal_type(self): ...
    @portal_type.setter
    def portal_type(self, value) -> None: ...

RelationListFactory: Incomplete
