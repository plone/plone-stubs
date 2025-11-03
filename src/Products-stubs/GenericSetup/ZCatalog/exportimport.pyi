from ..utils import ObjectManagerHelpers
from ..utils import PropertyManagerHelpers
from ..utils import XMLAdapterBase

class _extra: ...

class ZCatalogXMLAdapter(XMLAdapterBase, ObjectManagerHelpers, PropertyManagerHelpers):
    """XML im- and exporter for ZCatalog."""

    name: str
