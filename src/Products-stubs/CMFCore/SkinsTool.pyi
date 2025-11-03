from .ActionProviderBase import ActionProviderBase
from .SkinsContainer import SkinsContainer
from .utils import UniqueObject
from _typeshed import Incomplete
from OFS.Folder import Folder
from OFS.ObjectManager import REPLACEABLE

def modifiedOptions(): ...

class SkinsTool(UniqueObject, SkinsContainer, Folder, ActionProviderBase):
    """This tool is used to supply skins to a portal."""

    id: str
    meta_type: str
    allow_any: int
    cookie_persistence: int
    default_skin: str
    request_varname: str
    selections: Incomplete
    security: Incomplete
    manage_options: Incomplete
    def __init__(self) -> None: ...
    manage_overview: Incomplete
    manage_propertiesForm: Incomplete
    manage_findForm: Incomplete
    manage_compareResults: Incomplete
    def manage_skinLayers(
        self,
        chosen=(),
        add_skin: int = 0,
        del_skin: int = 0,
        skinname: str = "",
        skinpath: str = "",
        REQUEST=None,
    ):
        """Change the skinLayers."""
    def isFirstInSkin(self, template_path, skin=None):
        """
        Is the specified template the one that would get returned
        from the current skin?
        """
    def manage_properties(
        self,
        default_skin: str = "",
        request_varname: str = "",
        allow_any: int = 0,
        chosen=(),
        add_skin: int = 0,
        del_skin: int = 0,
        skinname: str = "",
        skinpath: str = "",
        cookie_persistence: int = 0,
        REQUEST=None,
    ):
        """Changes portal_skin properties."""
    @security.private
    def PUT_factory(self, name, typ, body):
        """
        Dispatcher for PUT requests to non-existent IDs.  Returns
        an object of the appropriate type (or None, if we don't
        know what to do).
        """
    PUT_factory__replaceable__ = REPLACEABLE
    @security.private
    def testSkinPath(self, p) -> None:
        """Calls SkinsContainer.getSkinByPath()."""
    def getSkinPath(self, name):
        """Convert a skin name to a skin path."""
    def getDefaultSkin(self):
        """Get the default skin name."""
    def getRequestVarname(self):
        """Get the variable name to look for in the REQUEST."""
    def getAllowAny(self):
        """
        Used by the management UI.  Returns a flag indicating whether
        users are allowed to use arbitrary skin paths.
        """
    def getCookiePersistence(self):
        """
        Used by the management UI.  Returns a flag indicating whether
        the skins cookie is persistent or not.
        """
    def getSkinPaths(self):
        """
        Used by the management UI.  Returns the list of skin name to
        skin path mappings as a sorted list of tuples.
        """
    @security.public
    def getSkinSelections(self):
        """Get the sorted list of available skin names."""
    def updateSkinCookie(self):
        """If needed, updates the skin cookie based on the member preference."""
    def clearSkinCookie(self) -> None:
        """Expire the skin cookie."""
    def addSkinSelection(
        self, skinname, skinpath, test: int = 0, make_default: int = 0
    ) -> None:
        """
        Adds a skin selection.
        """
    def getDiff(self, item_one_path, item_two_path, reverse: int = 0):
        """Return a diff between one and two."""
