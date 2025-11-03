from _typeshed import Incomplete
from DocumentTemplate._DocumentTemplate import TemplateDict
from DocumentTemplate.security import RestrictedDTML
from zope.tales.pythonexpr import PythonExpr

class PythonExpr(PythonExpr):
    text: Incomplete
    def __init__(self, name, expr, engine) -> None: ...
    def __call__(self, econtext): ...

class _SecureModuleImporter:
    __allow_access_to_unprotected_subobjects__: bool
    def __getitem__(self, module): ...

class Rtd(RestrictedDTML, TemplateDict):
    this: Incomplete

def call_with_ns(f, ns, arg: int = 1): ...
