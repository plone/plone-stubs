from _typeshed import Incomplete

class ContentContext:
    """A portlet context for regular content items.

    Note - we register this for Interface so that it can also work for
    tools and other non-content items. This may hijack the context in non-CMF
    contexts, but that is doubtfully going to be an issue.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def uid(self): ...
    def getParent(self): ...
    def globalPortletCategories(self, placeless: bool = False): ...

class PortalRootContext(ContentContext):
    """A portlet context for the site root."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def getParent(self) -> None: ...
