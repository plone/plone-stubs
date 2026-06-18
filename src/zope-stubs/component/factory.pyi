"""Partial stubs for :mod:`zope.component.factory`."""

from collections.abc import Callable
from typing import Any

class Factory:
    title: str
    description: str

    def __init__(
        self,
        callable: Callable[..., Any],
        title: str = ...,
        description: str = ...,
        interfaces: Any = ...,
    ) -> None: ...
    def __call__(self, *args: Any, **kw: Any) -> Any: ...
    def getInterfaces(self) -> Any: ...
