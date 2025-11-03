from _typeshed import Incomplete
from plone.dexterity.content import Container
from Products.CMFCore.Skinnable import SkinnableObjectManager

class PloneSite(Container, SkinnableObjectManager):
    """The Plone site object."""

    security: Incomplete
    meta_type: str
    portal_type: str
    manage_main: Incomplete
    def __getattr__(self, name): ...
    def __setattr__(self, name, obj) -> None: ...
    def __delattr__(self, name): ...
    manage_options: Incomplete
    __ac_permissions__: Incomplete
    has_order_support: int
    management_page_charset: str
    title: str
    description: str
    icon: str
    def __init__(self, id, title: str = "") -> None: ...
    def __before_publishing_traverse__(self, arg1, arg2=None) -> None:
        """Pre-traversal hook."""
    def tpValues(self): ...
    def __browser_default__(self, request):
        """Set default so we can return whatever we want instead
        of index_html"""
    def index_html(self):
        """Acquire if not present."""
    index_html: Incomplete
    removal_inprogress: int
    def manage_beforeDelete(self, container, item) -> None: ...
    def manage_delObjects(self, ids=None, REQUEST=None):
        """We need to enforce security."""
    def view(self):
        """Ensure that we get a plain view of the object, via a delegation to
        __call__(), which is defined in BrowserDefaultMixin
        """
    def folderlistingFolderContents(self, contentFilter=None):
        """Calls listFolderContents in protected only by ACI so that
        folder_listing can work without the List folder contents permission.

        This is copied from Archetypes Basefolder and is needed by the
        reference browser.
        """
    def isEffective(self, date): ...
