from _typeshed import Incomplete
from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
from Products.GenericSetup.utils import XMLAdapterBase

def importViewletSettingsStorage(context) -> None:
    """Import viewlet settings."""

def exportViewletSettingsStorage(context) -> None:
    """Export viewlet settings."""

class ViewletSettingsStorageNodeAdapter(XMLAdapterBase):
    __used_for__ = IViewletSettingsStorage
    skins: Incomplete
    def __init__(self, context, environ) -> None: ...
