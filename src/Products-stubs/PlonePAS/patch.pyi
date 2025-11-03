from _typeshed import Incomplete

logger: Incomplete
PATTERN: str

def call(self, __name__, *args, **kw): ...

WRAPPER: str
ADDED: str
ORIG_NAME: str

def isWrapperMethod(meth): ...
def wrap_method(
    klass,
    name,
    method,
    pattern=...,
    add: bool = False,
    roles=None,
    deprecated: bool = False,
) -> None:
    """takes a method and set it to a class. Annotates with hints what happened."""

def unwrap_method(klass, name) -> None: ...
