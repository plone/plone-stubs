from _typeshed import Incomplete
from zope.interface import Interface

class IBehaviorDirective(Interface):
    """Directive which registers a new behavior type.

    The registration consists of:

        * a global named utility registered by interface identifier
        * a global named utility registered by lookup name
        * an associated global and unnamed behavior adapter
    """

    name: Incomplete
    title: Incomplete
    description: Incomplete
    provides: Incomplete
    marker: Incomplete
    factory: Incomplete
    for_: Incomplete
    name_only: Incomplete
    former_dotted_names: Incomplete

def behaviorDirective(
    _context,
    title,
    provides,
    name=None,
    description=None,
    marker=None,
    factory=None,
    for_=None,
    name_only: bool = False,
    former_dotted_names: str = "",
) -> None: ...
