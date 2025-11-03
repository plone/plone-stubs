from zope.interface.interfaces import ObjectEvent

class EditBegunEvent(ObjectEvent):
    """An edit operation was begun"""

class AddBegunEvent(ObjectEvent):
    """An add operation was begun. The event context is the folder,
    since the object does not exist yet.
    """

class EditCancelledEvent(ObjectEvent):
    """An edit operation was cancelled"""

class AddCancelledEvent(ObjectEvent):
    """An add operation was cancelled. The event context is the folder,
    since the object does not exist yet.
    """

class EditFinishedEvent(ObjectEvent):
    """Edit was finished and contents are saved. This event is fired
    even when no changes happen (and no modified event is fired.)
    """
