from _typeshed import Incomplete
from ExtensionClass import Base

fti_meta_type: Incomplete

class BrowserDefaultMixin(Base):
    """Mixin class for content types using the dynamic view FTI

    Allow the user to select a layout template (in the same way as
    TemplateMixin in Archetypes does), and/or to set a contained
    object's id as a default_page (acting in the same way as index_html)

    Note: folderish content types should overwrite HEAD like ATContentTypes
    """

    aliases: Incomplete
    default_view: str
    suppl_views: Incomplete
    security: Incomplete
    def defaultView(self, request=None): ...
    def __call__(self):
        """
        Resolve and return the selected view template applied to the object.
        This should not consider the default page.
        """
    def getDefaultPage(self): ...
    def getLayout(self, **kw): ...
    @security.public
    def canSetDefaultPage(self): ...
    def setDefaultPage(self, objectId) -> None: ...
    def setLayout(self, layout) -> None: ...
    def getDefaultLayout(self): ...
    @security.public
    def canSetLayout(self): ...
    def getAvailableLayouts(self): ...

def check_default_page(obj, event) -> None:
    """event subscriber, unset default page if target no longer exists

    used by default for zope.container.interfaces.IContainerModifiedEvent
    """

def rename_default_page(obj, event) -> None:
    """event subscriber, rename default page if target was renamed

    used by default for zope.lifecycleevent.interfaces.IObjectMovedEvent
    """
