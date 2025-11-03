from _typeshed import Incomplete
from zope.interface import Interface
from zope.interface.interfaces import IInterface
from zope.location.interfaces import IContained

__docformat__: str

class IRuleElementData(Interface):
    """Metadata for rule element data (the configuration of actions
    or conditions).
    """

    element: Incomplete
    summary: Incomplete

class IRuleElement(Interface):
    """Base interface for rule elements (actions and conditions)

    A rule element is either a condition or an action that can be combined to
    form a rule.Rules can be constructed by the user and invoked by the
    IRuleExecuter
    """

    title: Incomplete
    description: Incomplete
    for_: Incomplete
    event: Incomplete
    addview: Incomplete
    editview: Incomplete
    schema: Incomplete
    factory: Incomplete

class IRuleCondition(IRuleElement):
    """A condition of a rule

    Rule execution will stop if the condition fails. If the condition does not
    fail, the next element will be executed.
    """

class IRuleAction(IRuleElement):
    """An action executed as part of a rule.

    Actions can perform operations, presuming preceding conditions do not fail.
    Once an action is finished, the next element will be executed.
    """

class IRuleEventType(IInterface):
    """Marker interface for event interfaces that can be used as the 'event'
    type of an IRule.
    """

class IRuleConfiguration(Interface):
    """Configurable options for a rule"""

    title: Incomplete
    description: Incomplete
    event: Incomplete
    enabled: Incomplete
    stop: Incomplete
    cascading: Incomplete

class IRule(IContained, IRuleConfiguration):
    """A rule - a collection of rule elements.

    A rule is composed, normally through the user interface, of conditions and
    actions. Upon some event, rules that are relevant in the given context will
    be executed by adapting them to IExecutable and running its execute()
    method.

    When saved in a rule storage, it will be given a name.
    """

    conditions: Incomplete
    actions: Incomplete

class IExecutable(Interface):
    """An item which can be executed.

    The execution of a rule involves the execution of each one of its elements
    (i.e. conditions and actions). The IRule will be adapted to IExecutable in
    order to execute it (e.g. by iterating through the elements and executing
    each one), in a multi-adaptation of (context, rule, event), making it
    possible to customise the execution based on the type of event or context.

    Similarly, any object created via the 'addview' of an IRuleElement (i.e.
    the configuration object for that particular instance of that particular
    condition or action) will be adapted to IExecutable, in a multi-adaptation
    from (context, element, event),  in order to be executed when the rule that
    contains it is executed.
    """
    def __call__() -> None:
        """Execute the rule or rule element.

        If this method returns False, execution will stop. If it returns True,
        execution will continue if possible.
        """
