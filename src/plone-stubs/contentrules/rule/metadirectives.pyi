from _typeshed import Incomplete
from zope.interface import Interface

class IRuleElementDirective(Interface):
    """Directive which registers a new rule element.

    The actual directives will use IRuleActionDirective or IRuleConditionDirective
    """

    name: Incomplete
    title: Incomplete
    description: Incomplete
    for_: Incomplete
    event: Incomplete
    addview: Incomplete
    editview: Incomplete
    schema: Incomplete
    factory: Incomplete

class IRuleActionDirective(IRuleElementDirective):
    """An element directive describing what is logically an action element."""

class IRuleConditionDirective(IRuleElementDirective):
    """An element directive describing what is logically a condition element."""
