from _typeshed import Incomplete

def localPortletAssignmentMappingAdapter(context, manager):
    """When adapting (context, manager), get an IPortletAssignmentMapping
    by finding one in the object's annotations. The container will be created
    if necessary.
    """

class LocalPortletAssignmentManager:
    """Default implementation of ILocalPortletAssignmentManager which stores
    information in an annotation.
    """

    context: Incomplete
    manager: Incomplete
    def __init__(self, context, manager) -> None: ...
    def setBlacklistStatus(self, category, status) -> None: ...
    def getBlacklistStatus(self, category): ...

class BlockingLocalPortletAssignmentManager(LocalPortletAssignmentManager):
    """Implementation of ILocalPortletAssignmentManager which by default blocks
    parent contextual portlets.
    """
    def getBlacklistStatus(self, category): ...
