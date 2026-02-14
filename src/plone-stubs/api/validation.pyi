from collections.abc import Callable
from typing import Any
from typing import TypeVar

_F = TypeVar("_F", bound=Callable[..., Any])

def required_parameters(*required_params: str) -> Callable[[_F], _F]:
    """Test whether all of the specified parameters have been supplied and are not None.

    Usage::

        @required_parameters('a', 'b')
        def foo(a=None, b=None, c=None):
            pass
    """
def mutually_exclusive_parameters(*exclusive_params: str) -> Callable[[_F], _F]:
    """Raise an exception if more than one of the specified parameters has been supplied.

    Usage::

        @mutually_exclusive_parameters('a', 'b')
        def foo(a=None, b=None, c=None):
            pass
    """
def at_least_one_of(*candidate_params: str) -> Callable[[_F], _F]:
    """Raise an exception if none of the specified parameters has been supplied.

    Can be used in conjunction with mutually_exclusive_parameters to enforce exactly one.

    Usage::

        @at_least_one_of('a', 'b')
        def foo(a=None, b=None, c=None):
            pass
    """
