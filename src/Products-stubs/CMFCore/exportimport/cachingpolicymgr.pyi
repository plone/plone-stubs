from _typeshed import Incomplete
from Products.GenericSetup.utils import NodeAdapterBase
from Products.GenericSetup.utils import XMLAdapterBase

class CachingPolicyNodeAdapter(NodeAdapterBase):
    """Node im- and exporter for CachingPolicy."""

    node: Incomplete

class CachingPolicyManagerXMLAdapter(XMLAdapterBase):
    """XML im- and exporter for CachingPolicyManager."""

    name: str

def importCachingPolicyManager(context) -> None:
    """Import caching policy manager settings from an XML file."""

def exportCachingPolicyManager(context) -> None:
    """Export caching policy manager settings as an XML file."""
