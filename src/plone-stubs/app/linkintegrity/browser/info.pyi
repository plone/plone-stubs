from _typeshed import Incomplete
from Products.Five import BrowserView

logger: Incomplete

class DeleteConfirmationInfo(BrowserView):
    template: Incomplete
    breach_count: Incomplete
    linkintegrity_enabled: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    breaches: Incomplete
    def __call__(self, items=None): ...
    def get_breaches(self, items=None):
        """Return breaches for multiple items.

        Breaches coming from objects in the list of items
        or their children (if a object is a folder) will be ignored.
        """
    def get_breaches_for_item(self, obj=None):
        """Get breaches for one object and its children.

        Breaches coming from the children of a folder are ignored by default.
        """
    def check_object(self, obj, excluded_path=None, excluded_paths=None):
        """Check one object for breaches.
        Breaches originating from excluded_paths are ignored.
        """
    def get_portal_type_title(self, obj):
        """Get the portal type title of the object."""
    def is_accessible(self, obj): ...
    def objects(self): ...
