from .interfaces import UniqueIdError
from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

UID_ATTRIBUTE_NAME: str

class UniqueIdHandlerTool(UniqueObject, SimpleItem):
    __doc__ = __doc__
    id: str
    manage_options: Incomplete
    alternative_id: str
    meta_type: str
    UID_ATTRIBUTE_NAME = UID_ATTRIBUTE_NAME
    UniqueIdError = UniqueIdError
    security: Incomplete
    def register(self, obj):
        """See IUniqueIdSet."""
    def unregister(self, obj) -> None:
        """See IUniqueIdSet."""
    def queryUid(self, obj, default=None):
        """See IUniqueIdQuery."""
    def getUid(self, obj):
        """See IUniqueIdQuery."""
    def setUid(self, obj, uid, check_uniqueness: bool = True) -> None:
        """See IUniqueIdSet."""
    def queryBrain(self, uid, default=None):
        """See IUniqueIdBrainQuery."""
    def getBrain(self, uid):
        """See IUniqueIdBrainQuery."""
    def getObject(self, uid):
        """See IUniqueIdQuery."""
    def queryObject(self, uid, default=None):
        """See IUniqueIdQuery."""
    def unrestrictedQueryBrain(self, uid, default=None):
        """See IUniqueIdUnrestrictedQuery."""
    def unrestrictedGetBrain(self, uid):
        """See IUniqueIdUnrestrictedQuery."""
    def unrestrictedGetObject(self, uid):
        """See IUniqueIdUnrestrictedQuery."""
    def unrestrictedQueryObject(self, uid, default=None):
        """See IUniqueIdUnrestrictedQuery."""
    manage_queryObject: Incomplete
