from _typeshed import Incomplete

logger: Incomplete

def importVarious(context) -> None:
    """
    Import various settings.

    Provisional handler that does initialization that is not yet taken
    care of by other handlers.
    """

def installSkipRegistryBasesPointersModifier(context) -> None:
    """Upgrade step to install the component registry bases modifier."""

def removeBrokenModifiers(context) -> None:
    """Remove broken modifiers.

    For Plone 6 we have removed Archetypes support.
    This includes removing classes for four Archetypes modifiers.
    During normal usage you should not notice this.
    But it is still better to remove them.
    """

def removeSkinLayer(context) -> None:
    """Remove our skin layer."""
