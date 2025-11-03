from _typeshed import Incomplete
from App.special_dtml import DTMLFile

LOGGER: Incomplete

class NoThemeDTMLFile(DTMLFile):
    """DTMLFile that automatically sets the X-Theme-Disabled header"""

NO_THEME_DTML: Incomplete

def disable_theming(func): ...
def patch_zmi() -> None: ...
