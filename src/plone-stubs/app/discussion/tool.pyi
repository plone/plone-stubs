from OFS.SimpleItem import SimpleItem
from Products.CMFCore.utils import UniqueObject

class CommentingTool(UniqueObject, SimpleItem):
    meta_type: str
    id: str
    def reindexObject(self, object): ...
    indexObject = reindexObject
    def unindexObject(self, object): ...
    def uniqueValuesFor(self, name): ...
    def searchResults(self, REQUEST=None, **kw): ...

def index_object(obj, event) -> None:
    """Index the object when added to the conversation"""

def unindex_object(obj, event) -> None:
    """Unindex the object when removed"""
