from _typeshed import Incomplete
from plone.restapi.services import Service

class WorkflowTransition(Service):
    """Trigger workflow transition"""

    transition: Incomplete
    wftool: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def reply(self): ...
    def recurse_transition(
        self, objs, comment, publication_dates, include_children: bool = False
    ) -> None: ...
    def is_same_state(self, obj):
        """
        Return True if the object is already in the transition's destination state.
        """
