from _typeshed import Incomplete
from ast import NodeTransformer
from z3c.pt import expressions
from zope.tales.tales import ExpressionEngine

zope2_exceptions: Incomplete

def static(obj): ...

class BoboAwareZopeTraverse:
    traverse_method: str
    @classmethod
    def traverse(cls, base, request, path_items):
        """See ``zope.app.pagetemplate.engine``."""
    def __call__(self, base, econtext, call, path_items): ...

class TrustedBoboAwareZopeTraverse(BoboAwareZopeTraverse):
    traverse_method: str
    def __call__(self, base, econtext, call, path_items): ...

class PathExpr(expressions.PathExpr):
    exceptions = zope2_exceptions
    traverser: Incomplete

class TrustedPathExpr(PathExpr):
    traverser: Incomplete

class NocallExpr(expressions.NocallExpr, PathExpr): ...

class ExistsExpr(expressions.ExistsExpr):
    exceptions = zope2_exceptions

class RestrictionTransform(NodeTransformer):
    secured: Incomplete
    def visit_Name(self, node): ...

class UntrustedPythonExpr(expressions.PythonExpr):
    restricted_python_transformer: Incomplete
    page_templates_expression_transformer: Incomplete
    builtins: Incomplete
    def parse(self, string): ...

class ChameleonEngine(ExpressionEngine):
    """Expression engine for ``chameleon.tales``.

    Only partially implemented: its ``compile`` is currently unusable
    """
    def compile(self, expression) -> None: ...

types: Incomplete

def createChameleonEngine(types=..., untrusted: bool = True, **overrides): ...
def createTrustedChameleonEngine(**overrides): ...
def getEngine(): ...
def getTrustedEngine(): ...
