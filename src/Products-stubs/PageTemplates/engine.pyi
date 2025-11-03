from .Expressions import PathIterator
from _typeshed import Incomplete
from chameleon.tal import RepeatDict
from collections.abc import Mapping
from z3c.pt.pagetemplate import PageTemplate as ChameleonPageTemplate

class _PseudoContext:
    """auxiliary context object.

    Used to bridge between ``chameleon`` and ``zope.tales`` iterators.
    """
    @staticmethod
    def setLocal(*args) -> None: ...

class RepeatDictWrapper(RepeatDict):
    """Wrap ``chameleon``s ``RepeatDict``.

    Aims:

      1. make it safely usable by untrusted code

      2. let it use a ``zope.tales`` compatible ``RepeatItem``
    """

    security: Incomplete
    __allow_access_to_unprotected_subobjects__: bool
    def __call__(self, key, iterable):
        """We coerce the iterable to a tuple and return an iterator
        after registering it in the repeat dictionary."""

class RepeatItem(PathIterator):
    """Iterator compatible with ``chameleon`` and ``zope.tales``."""
    def __iter__(self): ...
    def __next__(self): ...

re_match_pi: Incomplete
logger: Incomplete

class Name2KeyError(Mapping):
    data: Incomplete
    def __init__(self, mapping) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class _C2ZContextWrapperBase:
    """Behaves like "zope" context with vars from "chameleon" context.

    It is assumed that an instance holds the current ``chameleon``
    context in its attribute ``_c_context``.
    """
    @property
    def vars(self): ...
    def getValue(self, name, default=None): ...
    get = getValue
    def setLocal(self, name, value) -> None: ...
    def setGlobal(self, name, value) -> None: ...
    def beginScope(self, *args, **kw) -> None:
        """will not work as the scope is controlled by ``chameleon``."""
    endScope = beginScope
    setSourceFile = beginScope
    setPosition = beginScope
    setRepeat = beginScope
    def getDefault(self): ...

BAD_PATH_CHARS: str
contains_bad_path_chars: Incomplete

class MappedExpr:
    """map expression: ``zope.tales`` --> ``chameleon.tales``."""

    type: Incomplete
    expression: Incomplete
    def __init__(self, type, expression, zt_engine) -> None: ...
    def __call__(self, target, c_engine): ...

class MappedExprType:
    """map expression type: ``zope.tales`` --> ``chameleon.tales``."""

    engine: Incomplete
    type: Incomplete
    def __init__(self, engine, type) -> None: ...
    def __call__(self, expression): ...

class ZtPageTemplate(ChameleonPageTemplate):
    """``ChameleonPageTemplate`` using ``zope.tales.tales._default``.

    Note: this is not necessary when ``chameleon.tales`` is used
    but it does not hurt to use the fixed value to represent ``default``
    rather than a template specific value.
    """

    value_repr: Incomplete

class Program:
    template: Incomplete
    engine: Incomplete
    def __init__(self, template, engine) -> None: ...
    def __call__(self, context, macros, tal: bool = True, **options): ...
    @classmethod
    def cook(cls, source_file, text, engine, content_type): ...
