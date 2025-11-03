from .CMFCatalogAware import CMFCatalogAware
from .DynamicType import DynamicType
from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

class PortalContent(DynamicType, CMFCatalogAware, SimpleItem):
    """Base class for portal objects.

    Provides hooks for reviewing, indexing, and CMF UI.

    Derived classes must implement the interface described in
    interfaces/DublinCore.py.
    """

    manage_options: Incomplete
    security: Incomplete
    def failIfLocked(self):
        """Check if isLocked via webDav."""
    def SearchableText(self):
        """Returns a concatination of all searchable text.

        Should be overriden by portal objects.
        """
    def __call__(self):
        """Invokes the default view."""
