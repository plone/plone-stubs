from _typeshed import Incomplete
from Products.CMFEditions.interfaces._tools import IArchivistTool as IArchivistTool
from Products.CMFEditions.interfaces._tools import (
    IPortalModifierTool as IPortalModifierTool,
)
from Products.CMFEditions.interfaces._tools import IPurgePolicyTool as IPurgePolicyTool
from Products.CMFEditions.interfaces._tools import IStorageTool as IStorageTool
from zope import interface

class IVersioned(interface.Interface):
    """Marker interface for objects that carry a version id, and are
    thus versioned.
    """

    version_id: Incomplete
