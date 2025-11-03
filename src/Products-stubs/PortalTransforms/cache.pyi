from _typeshed import Incomplete

class Cache:
    obj: Incomplete
    context: Incomplete
    def __init__(self, obj, context=None, _id: str = "_v_transform_cache") -> None: ...
    def setCache(self, key, value):
        """cache a value indexed by key"""
    def getCache(self, key):
        """try to get a cached value for key

        return None if not present
        else return a tuple (time spent in cache, value)
        """
    def purgeCache(self, key=None) -> None:
        """Remove cache"""
