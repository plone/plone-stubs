from _typeshed import Incomplete

class RuleNamespace:
    """Used to traverse to a rule.

    Traversing to portal/++rule++foo will retrieve the rule with id 'foo'
    stored in context, acquisition-wrapped.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignore): ...

class RuleConditionNamespace:
    """Used to traverse to a rule condition

    Traversing to portal/++rule++foo/++condition++1 will retrieve the second
    condition of the rule rule with id 'foo', acquisition-wrapped.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignore): ...

class RuleActionNamespace:
    """Used to traverse to a rule condition

    Traversing to portal/++rule++foo/++action++1 will retrieve the second
    condition of the rule rule with id 'foo', acquisition-wrapped.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request=None) -> None: ...
    def traverse(self, name, ignore): ...
