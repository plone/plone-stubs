from _typeshed import Incomplete
from zope.interface.interfaces import ObjectEvent

class WorkflowException(Exception):
    """Exception while invoking workflow."""

class ObjectDeleted(Exception):
    """Raise to tell the workflow tool that the object has been deleted.

    Swallowed by the workflow tool.
    """
    def __init__(self, result=None) -> None: ...
    def getResult(self): ...

class ObjectMoved(Exception):
    """Raise to tell the workflow tool that the object has moved.

    Swallowed by the workflow tool.
    """
    def __init__(self, new_ob, result=None) -> None: ...
    def getResult(self): ...
    def getNewObject(self): ...

class WorkflowActionEvent(ObjectEvent):
    workflow: Incomplete
    action: Incomplete
    def __init__(self, object, workflow, action) -> None: ...

class ActionWillBeInvokedEvent(WorkflowActionEvent): ...

class ActionRaisedExceptionEvent(WorkflowActionEvent):
    exc: Incomplete
    def __init__(self, object, workflow, action, exc) -> None: ...

class ActionSucceededEvent(WorkflowActionEvent):
    result: Incomplete
    def __init__(self, object, workflow, action, result) -> None: ...
