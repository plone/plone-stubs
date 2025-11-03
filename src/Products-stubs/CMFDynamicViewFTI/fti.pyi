from _typeshed import Incomplete
from Products.CMFCore.TypesTool import FactoryTypeInformation

def safe_hasattr(obj, name, _marker=...):
    """Make sure we don't mask exceptions like hasattr().

    We don't want exceptions other than AttributeError to be masked,
    since that too often masks other programming errors.
    Three-argument getattr() doesn't mask those, so we use that to
    implement our own hasattr() replacement.
    """

def safe_callable(obj):
    """Make sure our callable checks are ConflictError safe."""

def om_has_key(context, key):
    """Object Manager has_key method with optimization for btree folders

    Zope's OFS.ObjectManager has no method for checking if an object with an id
    exists inside a folder.
    """

fti_meta_type: str

class DynamicViewTypeInformation(FactoryTypeInformation):
    """FTI with dynamic views

    A value of (dynamic view) as alias is replaced by the output of
    defaultView()
    """

    meta_type = fti_meta_type
    security: Incomplete
    default_view: str
    view_methods: Incomplete
    default_view_fallback: bool
    def manage_changeProperties(self, **kw) -> None:
        """Overwrite change properties to verify that default_view is in the method
        list
        """
    def getDefaultViewMethod(self, context): ...
    def getAvailableViewMethods(self, context): ...
    def getViewMethod(
        self, context, enforce_available: bool = False, check_exists: bool = False
    ): ...
    def getDefaultPage(self, context, check_exists: bool = False): ...
    def defaultView(self, context): ...
    @security.public
    def queryMethodID(self, alias, default=None, context=None): ...
