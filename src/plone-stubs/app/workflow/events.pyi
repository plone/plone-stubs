from zope.lifecycleevent import ObjectModifiedEvent

class LocalrolesModifiedEvent(ObjectModifiedEvent):
    """Gets fired after local roles of an object has been changed."""
