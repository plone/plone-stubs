from _typeshed import Incomplete

class PortletRetriever:
    """The default portlet retriever.

    This will examine the context and its parents for contextual portlets,
    provided they provide ILocalPortletAssignable.
    """

    context: Incomplete
    storage: Incomplete
    def __init__(self, context, storage) -> None: ...
    def getPortlets(self):
        """Work out which portlets to display, returning a list of dicts
        describing assignments to render.
        """

class PlacelessPortletRetriever(PortletRetriever):
    """A placeless portlet retriever.

    This will aggregate user portlets, then group portlets.
    """

    context: Incomplete
    storage: Incomplete
    def __init__(self, context, storage) -> None: ...
    def getPortlets(self): ...
