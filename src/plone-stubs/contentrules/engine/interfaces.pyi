from _typeshed import Incomplete
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.container.interfaces import IContainerNamesContainer
from zope.container.interfaces import IOrderedContainer
from zope.interface import Interface
from zope.location.interfaces import IContained

class StopRule(Exception):
    """An event that informs us that rule execution should be aborted."""

    rule: Incomplete
    def __init__(self, rule) -> None: ...

class IRuleStorage(IOrderedContainer, IContainerNamesContainer):
    """A storage for rules. This is registered as a local utility."""

    active: Incomplete

class IRuleAssignable(IAttributeAnnotatable):
    """Marker interface for objects that can be assigned rules"""

class IRuleAssignment(IContained):
    """An assignment of a rule to a context"""

    enabled: Incomplete
    bubbles: Incomplete

class IRuleAssignmentManager(IOrderedContainer):
    """An object that is capable of being assigned rules.

    Normally, an object will be adapted to IRuleAssignmentManager in order
    to manipulate the rule assignments in this location.
    """
    def getRules(event, bubbled: bool = False) -> None:
        """Get all enabled rules registered for the given event and
        assigned to this context. If bubbled is True, only rules that are
        bubbleable will be returned.
        """

class IRuleExecutor(Interface):
    """An object that is capable of executing rules.

    Typically, a content object will be adapted to this interface
    """
    def __call__(event, bubbled: bool = False, rule_filter=None) -> None:
        """Execute all rules applicable in the current context

        event is the triggering event. bubbled should be True if the rules
        are being executed as part of a bubbling up of events (i.e. this
        is a parent of the context where the event was triggered). filter,
        if given, is a callable that will be passed each rule in turn and
        can vote on whether it should be executed by returning True or
        False. It should take the arguments (context, rule, event).
        """
