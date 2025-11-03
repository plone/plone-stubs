from zope.interface.interfaces import ObjectEvent

class PloneResourceCreatedEvent(ObjectEvent):
    """A resource has been created"""

class PloneResourceModifiedEvent(ObjectEvent):
    """A resource has been modified"""
