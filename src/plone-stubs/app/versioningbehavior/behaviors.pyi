from _typeshed import Incomplete
from plone.supermodel import model
from zope.interface import Interface

class IVersionable(model.Schema):
    """Behavior for enabling CMFEditions's versioning for dexterity
    content types. Be sure to enable versioning in the plone types
    control-panel for your content type.
    """

    changeNote: Incomplete
    versioning_enabled: Incomplete

class IVersioningSupport(Interface):
    """
    Marker Interface for the IVersionable behavior.
    """

class Versionable:
    """The Versionable adapter prohibits dexterity from saving the changeNote
    on the context. It stores it in a request-annotation for later use in
    event-handlers

    The versioning_enabled flag is stored at the context itself.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def changeNote(self): ...
    @changeNote.setter
    def changeNote(self, value) -> None: ...
    @property
    def versioning_enabled(self): ...
    @versioning_enabled.setter
    def versioning_enabled(self, value) -> None: ...
