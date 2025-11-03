from .utils import XMLAdapterBase
from _typeshed import Incomplete

BLACKLIST_SELF: Incomplete

class ComponentRegistryXMLAdapter(XMLAdapterBase):
    """XML im- and exporter for a local component registry."""

    name: str

def importComponentRegistry(context) -> None:
    """Import local components."""

def exportComponentRegistry(context) -> None:
    """Export local components."""
