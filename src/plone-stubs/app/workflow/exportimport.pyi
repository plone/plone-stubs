from _typeshed import Incomplete
from persistent import Persistent
from Products.GenericSetup.utils import XMLAdapterBase

PMF: Incomplete

class PersistentSharingPageRole(Persistent):
    """These are registered as local utilities when managing the sharing
    page roles.
    """

    title: str
    required_permission: Incomplete
    required_interface: Incomplete
    def __init__(
        self, title: str = "", required_permission=None, required_interface=None
    ) -> None: ...

class SharingXMLAdapter(XMLAdapterBase):
    name: str
    info_tag: str

def import_sharing(context) -> None: ...
def export_sharing(context) -> None: ...
