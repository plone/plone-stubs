from _typeshed import Incomplete
from zope.interface import Interface

PMF: Incomplete

class IFieldLanguageIndependent(Interface):
    languageindependent: Incomplete

class FieldLanguageIndependentAdapter:
    field: Incomplete
    def __init__(self, field) -> None: ...
    languageindependent: Incomplete

def get_li_schema(schema_context, field): ...
