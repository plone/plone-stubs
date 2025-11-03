from _typeshed import Incomplete
from zope.interface import Interface

class IComment(Interface):
    """Dummy interface if there is no plone.app.discussion available."""

class DuplicateRuleFilter:
    """A filter which can prevent rules from being executed more than once
    regardless of context.
    """
    def __init__(self) -> None: ...
    executed: Incomplete
    in_progress: bool
    cascade: bool
    def reset(self) -> None: ...
    def __call__(self, context, rule, event): ...

def init() -> None: ...
def close(event) -> None:
    """Close the event processing when the request ends"""

def execute(context, event) -> None:
    """Execute all rules relative to the context, and bubble as appropriate."""

def execute_rules(event) -> None:
    """When an action is invoked on an object,
    execute rules assigned to its parent.
    Base action executor handler"""

def added(event) -> None:
    """When an object is added, execute rules assigned to its new parent."""

def removed(event) -> None:
    """When an IObjectRemovedEvent was received, execute rules assigned to its
    previous parent.
    """

def modified(event) -> None:
    """When an object is modified, execute rules assigned to its parent"""

def copied(event) -> None:
    """When an object is copied, execute rules assigned to its parent"""

def workflow_action(event) -> None:
    """When a workflow action is invoked on an object, execute rules assigned
    to its parent.
    """

def execute_user_rules(event) -> None: ...
def user_created(event) -> None:
    """When a user has been created, execute rules assigned to the Plonesite."""

def user_logged_in(event) -> None:
    """When a user is logged in, execute rules assigned to the Plonesite."""

def user_logged_out(event) -> None:
    """When a user is logged out, execute rules assigned to the Plonesite."""
