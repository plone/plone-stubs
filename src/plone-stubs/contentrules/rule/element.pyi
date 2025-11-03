from _typeshed import Incomplete
from zope.interface import Interface

class RuleElement:
    """A rule element.

    Ordinarily, rule elements will be created via ZCML directives, which will
    register them as utilities.
    """

    title: str
    description: str
    for_ = Interface
    event: Incomplete
    addview: Incomplete
    editview: Incomplete
    schema: Incomplete
    factory: Incomplete

class RuleCondition(RuleElement):
    """A rule condition.

    Rule conditions are just rule elements, but are registered under a more
    specific interface to enable the UI to differentate between different types
    of elements.
    """

class RuleAction(RuleElement):
    """A rule action.

    Rule action are just rule elements, but are registered under a more
    specific interface to enable the UI to differentate between different types
    of elements.
    """
