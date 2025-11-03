from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

manage_addModifierForm: Incomplete

class ConditionalModifier(SimpleItem):
    """This is a wrapper for a modifier."""

    modifierEditForm: Incomplete
    manage = modifierEditForm
    manage_main = modifierEditForm
    manage_options: Incomplete
    id: Incomplete
    title: Incomplete
    meta_type: Incomplete
    def __init__(self, id, modifier, title: str = "") -> None:
        """See IConditionalModifier."""
    def edit(self, enabled=None, title: str = "", REQUEST=None):
        """See IConditionalModifier."""
    def isBroken(self):
        """Is the modifier broken?

        This happens if the underlying class no longer exists.
        """
    def isApplicable(self, obj, portal=None):
        """See IConditionalModifier."""
    def isEnabled(self):
        """See IConditionalModifier."""
    def getModifier(self):
        """See IConditionalModifier."""

manage_addTalesModifierForm: Incomplete

class ConditionalTalesModifier(ConditionalModifier):
    """This is a wrapper with a tales condition for a modifier."""

    modifierEditForm: Incomplete
    manage_options: Incomplete
    def __init__(self, id, modifier, title: str = "") -> None:
        """See IConditionalTalesModifier."""
    def edit(self, enabled=None, condition=None, title: str = "", REQUEST=None):
        """See IConditionalTalesModifier."""
    def isApplicable(self, obj, portal=None):
        """See IConditionalTalesModifier."""
    def getTalesCondition(self):
        """See IConditionalTalesModifier."""

def createExpressionContext(obj, portal=None, **more_symbols):
    """Creates a valid context for the expression.

    Tal expressions need a context in order to do the evaluation.
    obj is the object that will be mapped to "object" in the
    expression\'s context.
    Other symbols like "repo_clone" and "obj_clone" can be passed as keyword
    arguments.
    """
