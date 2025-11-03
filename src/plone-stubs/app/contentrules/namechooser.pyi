from _typeshed import Incomplete
from zope.container.contained import NameChooser

ATTEMPTS: int

class RuleNameChooser(NameChooser):
    """A name chooser for content rules."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def chooseName(self, name, object): ...
