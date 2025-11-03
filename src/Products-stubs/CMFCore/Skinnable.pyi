from _typeshed import Incomplete
from OFS.ObjectManager import ObjectManager

logger: Incomplete
SKINDATA: Incomplete

class SkinDataCleanup:
    """Cleanup at the end of the request."""

    tid: Incomplete
    def __init__(self, tid) -> None: ...
    def __del__(self) -> None: ...

class SkinnableObjectManager(ObjectManager):
    security: Incomplete
    def __getattr__(self, name):
        """
        Looks for the name in an object with wrappers that only reach
        up to the root skins folder.

        This should be fast, flexible, and predictable.
        """
    @security.private
    def getSkin(self, name=None):
        """Returns the requested skin."""
    @security.public
    def getSkinNameFromRequest(self, REQUEST=None):
        """Returns the skin name from the Request."""
    @security.public
    def changeSkin(self, skinname, REQUEST=None) -> None:
        """Change the current skin.

        Can be called manually, allowing the user to change
        skins in the middle of a request.
        """
    @security.public
    def getCurrentSkinName(self):
        """Return the current skin name."""
    @security.public
    def clearCurrentSkin(self) -> None:
        """Clear the current skin."""
    @security.public
    def setupCurrentSkin(self, REQUEST=None) -> None:
        """
        Sets up skindata so that __getattr__ can find it.

        Can NOT be called manually to change skins in the middle of a
        request! Use changeSkin for that.
        """
