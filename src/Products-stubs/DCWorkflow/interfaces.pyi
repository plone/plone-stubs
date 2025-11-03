from _typeshed import Incomplete
from zope.interface import Interface
from zope.interface.interfaces import IObjectEvent

class IDCWorkflowDefinition(Interface):
    """Web-configurable workflow definition."""

class ITransitionEvent(IObjectEvent):
    """An event that's fired upon a workflow transition."""

    workflow: Incomplete
    old_state: Incomplete
    new_state: Incomplete
    transition: Incomplete
    status: Incomplete
    kwargs: Incomplete

class IBeforeTransitionEvent(ITransitionEvent):
    """An event fired before a workflow transition."""

class IAfterTransitionEvent(ITransitionEvent):
    """An event that's fired after a workflow transition."""
