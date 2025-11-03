class datastream:
    """A transformation datastream packet"""
    def __init__(self, name_) -> None: ...
    def name(self): ...
    def setData(self, value) -> None:
        """set the main data produced by a transform,
        i.e. usually a native string"""
    def getData(self):
        """provide access to the transformed data object,
        i.e. usually a native string
        This data may references subobjects.
        """
    def setSubObjects(self, objects) -> None:
        """set a dict-like object containing subobjects.
        keys should be object's identifier (e.g. usually a filename) and
        values object's content.
        """
    def getSubObjects(self):
        """return a dict-like object with any optional subobjects associated
        with the data"""
    def getMetadata(self):
        """return a dict-like object with any optional metadata from
        the transform"""
    def isCacheable(self):
        """Return a bool which indicates whether the result should be cached

        Default is true
        """
    def setCacheable(self, value) -> None:
        """Set cacheable flag to yes or no"""
