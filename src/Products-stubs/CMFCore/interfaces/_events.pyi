from _typeshed import Incomplete
from zope.interface.interfaces import IObjectEvent

class IWorkflowActionEvent(IObjectEvent):
    """Base interface for events around workflow action invocation"""

    __module__: str
    workflow: Incomplete
    action: Incomplete

class IActionWillBeInvokedEvent(IWorkflowActionEvent):
    """Event fired immediately before a workflow action is invoked"""

    __module__: str

class IActionRaisedExceptionEvent(IWorkflowActionEvent):
    """Event fired when a workflow action raised an exception"""

    __module__: str
    exc: Incomplete

class IActionSucceededEvent(IWorkflowActionEvent):
    """Event fired when a workflow action succeeded"""

    __module__: str
    result: Incomplete
