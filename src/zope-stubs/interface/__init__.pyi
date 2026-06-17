"""Partial stubs for :mod:`zope.interface`.

These stubs replace the ``mypy-zope`` plugin for the common surface used by
Plone code, so that interfaces behave as *types* for every PEP 561 type
checker (mypy, pyright, pylance), not just mypy.

The package is marked *partial* (see ``zope-stubs/py.typed``): submodules not
stubbed here fall back to the runtime package.
"""

from collections.abc import Callable
from typing import Any

class _InterfaceClass(type):
    """Metaclass for :class:`Interface`.

    Models the parts of ``InterfaceClass`` that callers use against the
    interface *object* itself (``IFoo.providedBy(obj)``, adaptation via
    ``IFoo(obj)``).
    """

    __name__: str
    __doc__: str | None
    __module__: str

    def providedBy(cls, obj: object) -> bool: ...
    def implementedBy(cls, obj: object) -> bool: ...
    def names(cls, all: bool = ...) -> tuple[str, ...]: ...
    def extends(cls, other: Any, strict: bool = ...) -> bool: ...
    def isOrExtends(cls, other: Any) -> bool: ...
    def __iter__(cls) -> Any: ...
    # Adaptation: ``IFoo(obj)`` returns something providing ``IFoo``.
    def __call__[T](cls: type[T], obj: Any = ..., default: Any = ...) -> T: ...

class Interface(metaclass=_InterfaceClass):
    """Base class for interfaces.

    A subclass declared in a stub (``class IFoo(Interface): ...``) is usable
    as a type in annotation position. The permissive ``__init__`` models
    adaptation-by-call (``IFoo(obj)``), which would otherwise be rejected as
    an argument error.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Attribute:
    """Interface attribute declaration."""

    __name__: str
    __doc__: str | None

    def __init__(self, name: str = ..., doc: str = ...) -> None: ...

def implementer[C: type](*interfaces: Any) -> Callable[[C], C]:
    """Class decorator declaring that instances provide ``interfaces``.

    Typed as identity so the decorated class is returned unchanged.
    """

def implementer_only[C: type](*interfaces: Any) -> Callable[[C], C]: ...
def provider[C: type](*interfaces: Any) -> Callable[[C], C]:
    """Class decorator declaring that the class itself provides ``interfaces``."""

def classImplements(cls: type, *interfaces: Any) -> None: ...
def classProvides(*interfaces: Any) -> None: ...
def directlyProvides(object: Any, *interfaces: Any) -> None: ...
def alsoProvides(object: Any, *interfaces: Any) -> None: ...
def noLongerProvides(object: Any, interface: Any) -> None: ...
def providedBy(object: object) -> Any: ...
def implementedBy(class_: type) -> Any: ...
def invariant[T](call: T) -> T: ...
def taggedValue(key: Any, value: Any) -> None: ...

class Invalid(Exception):
    """Raised by interface invariants when validation fails."""
