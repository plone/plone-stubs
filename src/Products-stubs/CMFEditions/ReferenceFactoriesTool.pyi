from _typeshed import Incomplete
from OFS.OrderedFolder import OrderedFolder
from Products.CMFCore.utils import UniqueObject

class ReferenceFactoriesTool(UniqueObject, OrderedFolder):
    __doc__ = __doc__
    id: str
    alternative_id: str
    meta_type: str
    security: Incomplete
    def invokeFactory(self, repo_clone, source, selector=None):
        """See IReferenceFactories"""
    def hasBeenMoved(self, obj, source):
        """See IReferenceFactories"""
