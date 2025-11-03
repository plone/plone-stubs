from .ActionProviderBase import ActionProviderBase
from .utils import UniqueObject
from _typeshed import Incomplete
from Products.ZCatalog.ZCatalog import ZCatalog
from zope.interface.declarations import ObjectSpecificationDescriptor

CATALOG_OPTIMIZATION_DISABLED: Incomplete

class IndexableObjectSpecification(ObjectSpecificationDescriptor):
    def __get__(self, inst, cls=None): ...

class IndexableObjectWrapper:
    __providedBy__: Incomplete
    def __init__(self, ob, catalog) -> None: ...
    def __getattr__(self, name): ...
    def allowedRolesAndUsers(self):
        """
        Return a list of roles and users with View permission.
        Used by PortalCatalog to filter out items you're not allowed to see.
        """
    def cmf_uid(self):
        """
        Return the CMFUid UID of the object while making sure
        it is not accidentally acquired.
        """
    @property
    def portal_type(self):
        """Return portal_type or an empty string if portal_type is None.

        Products.ZCatalog 3 indexes can no longer handle None values.
        """

class CatalogTool(UniqueObject, ZCatalog, ActionProviderBase):
    """This is a ZCatalog that filters catalog queries."""

    id: str
    meta_type: str
    zmi_icon: str
    security: Incomplete
    manage_options: Incomplete
    def __init__(self) -> None: ...
    manage_overview: Incomplete
    def searchResults(self, REQUEST=None, **kw):
        """
        Calls ZCatalog.searchResults with extra arguments that
        limit the results to what the user is allowed to see.
        """
    __call__ = searchResults
    @security.private
    def unrestrictedSearchResults(self, REQUEST=None, **kw):
        """Calls ZCatalog.searchResults directly without restrictions.

        This method returns every also not yet effective and already expired
        objects regardless of the roles the caller has.

        CAUTION: Care must be taken not to open security holes by
        exposing the results of this method to non authorized callers!

        If you're in doubt if you should use this method or
        'searchResults' use the latter.
        """
    manage_catalogFind: Incomplete
    def catalog_object(
        self, obj, uid=None, idxs=None, update_metadata: int = 1, pghandler=None
    ) -> None: ...
    @security.private
    def indexObject(self, object) -> None: ...
    @security.private
    def unindexObject(self, object) -> None: ...
    @security.private
    def reindexObject(
        self, object, idxs=[], update_metadata: int = 1, uid=None
    ) -> None: ...
