from _typeshed import Incomplete
from Products.CMFCore.CatalogTool import CatalogTool as BaseTool
from Products.CMFPlone.PloneBaseTool import PloneBaseTool

logger: Incomplete
DENIED_INTERFACES: Incomplete
BLACKLISTED_INTERFACES = DENIED_INTERFACES

def allowedRolesAndUsers(obj):
    """Return a list of roles and users with View permission.
    Used to filter out items you're not allowed to see.
    """

def object_provides(obj): ...
def zero_fill(matchobj): ...

num_sort_regex: Incomplete

def sortable_title(obj):
    """Helper method for to provide FieldIndex for Title."""

def getObjPositionInParent(obj):
    """Helper method for catalog based folder contents."""

def getObjSize(obj):
    """Helper method for catalog based folder contents."""

def is_folderish(obj):
    """Should this item be treated as a folder?

    Checks isPrincipiaFolderish, as well as the INonStructuralFolder
    interfaces.
    """

def is_default_page(obj):
    """Is this the default page in its folder"""

def getIcon(obj):
    """
    geticon redefined in Plone > 5.0
    see https://github.com/plone/Products.CMFPlone/issues/1226

    reuse of metadata field,
    now used for showing thumbs in content listings etc.
    when obj is an image or has a lead image
    or has an image field with name 'image': true else false
    """

def mime_type(obj): ...

class CatalogTool(PloneBaseTool, BaseTool):
    """Plone's catalog tool"""

    meta_type: str
    security: Incomplete
    toolicon: str
    manage_catalogAdvanced: Incomplete
    manage_options: Incomplete
    def __init__(self) -> None: ...
    @security.private
    def indexObject(self, object, idxs=None) -> None: ...
    def catalog_object(
        self, object, uid=None, idxs=None, update_metadata: int = 1, pghandler=None
    ) -> None: ...
    def uncatalog_object(self, *args, **kwargs): ...
    @security.private
    def getCounter(self): ...
    @security.private
    def allow_inactive(self, query_kw):
        """Check, if the user is allowed to see inactive content.
        First, check if the user is allowed to see inactive content site-wide.
        Second, if there is a 'path' key in the query, check if the user is
        allowed to see inactive content for these paths.
        Conservative check: as soon as one path is disallowed, return False.
        If a path cannot be traversed, ignore it.
        """
    def searchResults(self, query=None, **kw): ...
    __call__ = searchResults
    def search(
        self, query, sort_index=None, reverse: int = 0, limit=None, merge: int = 1
    ): ...
    def clearFindAndRebuild(self) -> None: ...
    def manage_catalogRebuild(self, RESPONSE=None, URL1=None) -> None:
        """Clears the catalog and indexes all objects with an 'indexObject'
        method. This may take a long time.
        """
