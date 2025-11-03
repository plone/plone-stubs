from _typeshed import Incomplete
from AccessControl import safe_builtins
from MultiMapping import MultiMapping
from zope.pagetemplate.engine import ZopeEngine as Z3Engine
from zope.tales.expressions import PathExpr
from zope.tales.expressions import StringExpr
from zope.tales.expressions import SubPathExpr
from zope.tales.tales import Context
from zope.tales.tales import ErrorInfo as BaseErrorInfo
from zope.tales.tales import Iterator

SecureModuleImporter: Incomplete
LOG: Incomplete
ZopeUndefs: Incomplete

def boboAwareZopeTraverse(object, path_items, econtext):
    """Traverses a sequence of names, first trying attributes then items.

    This uses zope.traversing path traversal where possible and interacts
    correctly with objects providing OFS.interface.ITraversable when
    necessary (bobo-awareness).
    """

def trustedBoboAwareZopeTraverse(object, path_items, econtext):
    """Traverses a sequence of names, first trying attributes then items.

    This uses zope.traversing path traversal where possible and interacts
    correctly with objects providing OFS.interface.ITraversable when
    necessary (bobo-awareness).
    """

def render(ob, ns):
    """Calls the object, possibly a document template, or just returns
    it if not callable.  (From DT_Util.py)
    """

class _CombinedMapping:
    """Minimal auxiliary class to combine several mappings.

    Earlier mappings take precedence.
    """

    mappings: Incomplete
    def __init__(self, *ms) -> None: ...
    def get(self, key, default): ...

class UntrustedSubPathExpr(SubPathExpr):
    ALLOWED_BUILTINS = safe_builtins

class TrustedSubPathExpr(SubPathExpr):
    ALLOWED_BUILTINS: Incomplete

class ZopePathExpr(PathExpr):
    SUBEXPR_FACTORY = UntrustedSubPathExpr
    def __init__(self, name, expr, engine) -> None: ...

class TrustedZopePathExpr(ZopePathExpr):
    SUBEXPR_FACTORY = TrustedSubPathExpr

class StructureExpr:
    """
    An expression that tells the template engine to
    render the value as structure (i.e. with markup).

    Note: will only work with ``chameleon`` template engine.
    """
    def __init__(self, name, expr, engine) -> None: ...
    def __call__(self, econtext): ...

class SafeMapping(MultiMapping):
    """Mapping with security declarations and limited method exposure.

    Since it subclasses MultiMapping, this class can be used to wrap
    one or more mapping objects.  Restricted Python code will not be
    able to mutate the SafeMapping or the wrapped mappings, but will be
    able to read any value.
    """

    __allow_access_to_unprotected_subobjects__: bool
    push: Incomplete
    pop: Incomplete

class ZopeContext(Context):
    vars: Incomplete
    def __init__(self, engine, contexts) -> None: ...
    def translate(self, msgid, domain=None, mapping=None, default=None): ...
    def evaluateBoolean(self, expr): ...
    def evaluateStructure(self, expr):
        """customized version in order to get rid of unicode
        errors for all and ever
        """
    def evaluateText(self, expr):
        """customized version in order to get rid of unicode
        errors for all and ever
        """
    def createErrorInfo(self, err, position): ...
    def evaluateCode(self, lang, code) -> None:
        """See ITALExpressionEngine.

        o This method is a fossil:  nobody actually calls it, but the
          interface requires it.
        """

class ErrorInfo(BaseErrorInfo):
    """Information about an exception passed to an on-error handler."""

    __allow_access_to_unprotected_subobjects__: bool

class ZopeEngine(Z3Engine): ...

class ZopeIterator(Iterator):
    __allow_access_to_unprotected_subobjects__: bool
    @property
    def index(self): ...
    @property
    def start(self): ...
    @property
    def end(self): ...
    @property
    def item(self): ...
    def first(self, name=None): ...
    def last(self, name=None): ...
    def same_part(self, name, ob1, ob2): ...
    def __next__(self): ...
    def next(self): ...

class PathIterator(ZopeIterator):
    """A TALES Iterator with the ability to use first() and last() on
    subpaths of elements."""
    def traverse(self, name, furtherPath): ...
    def same_part(self, name, ob1, ob2): ...

class UnicodeAwareStringExpr(StringExpr):
    def __call__(self, econtext): ...

def createZopeEngine(zpe=..., untrusted: bool = True): ...
def createTrustedZopeEngine(): ...
def getEngine(): ...
def getTrustedEngine(): ...
