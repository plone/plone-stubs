from _typeshed import Incomplete
from plone.supermodel import model
from zope.interface import Interface

class INextPreviousEnabled(Interface):
    """Behavior interface to enable next previous navigation for all items of
    a type.
    """

class INextPreviousToggle(model.Schema):
    """Behavior interface to enable next previous navigation per item."""

    nextPreviousEnabled: Incomplete

def getNextPreviousParentValue(adapter_): ...

DefaultNextPreviousEnabled: Incomplete

class NextPreviousBase:
    """adapter for acting as a next/previous provider"""

    context: Incomplete
    vat: Incomplete
    security: Incomplete
    order: Incomplete
    def __init__(self, context) -> None: ...
    def getNextItem(self, obj):
        """return info about the next item in the container"""
    def getPreviousItem(self, obj):
        """return info about the previous item in the container"""
    def getData(self, obj):
        """return the expected mapping, see `INextPreviousProvider`"""

class INextPreviousProvider(Interface):
    """A folderish component capable of describing the next and previous
    item relative to a particular id.
    """

    enabled: Incomplete
    def getNextItem(obj) -> None:
        """Returns information about next item in the container relative to
        the given object.

        This is a dict with the following keys:

            - obj, the object itself
            - id, the id of the object
            - url, the url of the object
            - title, the title of the object
            - description, a description of the object
            - portal_type, the object's portal type
        """
    def getPreviousItem(obj) -> None:
        """Returns the previous item in the container relative to the given
        object
        """

class NextPreviousToggle(NextPreviousBase):
    """adapter for acting as a next/previous provider"""
    @property
    def enabled(self): ...

class NextPreviousEnabled(NextPreviousBase):
    """adapter for acting as a next/previous provider"""

    enabled: bool
