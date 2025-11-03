from _typeshed import Incomplete
from zope.interface import Interface

logger: Incomplete

class IIncludePluginsDirective(Interface):
    """Auto-include any ZCML in the dependencies of this package."""

    target: Incomplete
    file: Incomplete

def includePluginsDirective(context, target: str = "", file=None) -> None: ...
def includePluginsOverridesDirective(context, target: str = "", file=None) -> None: ...
