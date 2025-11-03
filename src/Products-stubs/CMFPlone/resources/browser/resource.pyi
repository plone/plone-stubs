from _typeshed import Incomplete
from plone.app.layout.viewlets.common import ViewletBase

logger: Incomplete
REQUEST_CACHE_KEY: str
GRACEFUL_DEPENDENCY_REWRITE: Incomplete

class ResourceBase:
    """Information for script rendering.

    This is a mixin base class for a browser view, a viewlet or a tile
    or anything similar with a context and a request set on
    initialization.
    """
    @staticmethod
    def is_external_url(resource): ...
    rendered: Incomplete
    portal_state: Incomplete
    registry: Incomplete
    def update(self): ...
    def status_message_factory(
        self, status_message, status_type: str = "error"
    ) -> None:
        """Create a status message in a resource rendering error case for
        website admins, so that they can react to it.

        Don't show the error to regular users.
        """

class ResourceView(ResourceBase, ViewletBase):
    """Viewlet Information for resource rendering."""

class ScriptsView(ResourceView):
    """Script Viewlet."""
    def index(self): ...

class StylesView(ResourceView):
    """Styles Viewlet."""
    def index(self): ...

def update_resource_registry_mtime() -> None:
    """Update the last modification time of the resource registry.

    Call this when you change anything that may influence the resource registry
    and any of its rendered cache.
    See discussion in https://github.com/plone/Products.CMFPlone/issues/3505
    and https://github.com/plone/Products.CMFPlone/pull/3771
    """
