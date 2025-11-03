from _typeshed import Incomplete

ATTEMPTS: int

class NormalizingNameChooser:
    """A name chooser for a Zope object manager.

    If the object is adaptable to or provides INameFromTitle, use the
    title to generate a name.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def checkName(self, name, obj): ...
    def chooseName(self, name, obj): ...
