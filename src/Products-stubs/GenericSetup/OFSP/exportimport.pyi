from ..utils import ObjectManagerHelpers
from ..utils import PropertyManagerHelpers
from ..utils import XMLAdapterBase
from _typeshed import Incomplete

class FolderXMLAdapter(XMLAdapterBase, ObjectManagerHelpers, PropertyManagerHelpers):
    """XML im- and exporter for Folder."""

    body: Incomplete
