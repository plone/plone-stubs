from _typeshed import Incomplete
from MultiMapping import MultiMapping
from Products.CMFCore.Expression import Expression as Expression
from Products.CMFCore.WorkflowCore import ObjectDeleted
from Products.CMFCore.WorkflowCore import ObjectMoved

class SafeMapping(MultiMapping):
    """Mapping with security declarations and limited method exposure.

    Since it subclasses MultiMapping, this class can be used to wrap
    one or more mapping objects.  Restricted Python code will not be
    able to mutate the SafeMapping or the wrapped mappings, but will be
    able to read any value.
    """

    __allow_access_to_unprotected_subobjects__: int
    push: Incomplete
    pop: Incomplete

class StateChangeInfo:
    """
    Provides information for expressions and scripts.
    """

    ObjectDeleted = ObjectDeleted
    ObjectMoved = ObjectMoved
    security: Incomplete
    object: Incomplete
    workflow: Incomplete
    old_state: Incomplete
    new_state: Incomplete
    transition: Incomplete
    status: Incomplete
    kwargs: Incomplete
    def __init__(
        self,
        object,
        workflow,
        status=None,
        transition=None,
        old_state=None,
        new_state=None,
        kwargs=None,
    ) -> None: ...
    def __getitem__(self, name): ...
    def getHistory(self): ...
    def getPortal(self): ...
    def getDateTime(self): ...

def createExprContext(sci):
    """
    An expression context provides names for TALES expressions.
    """
