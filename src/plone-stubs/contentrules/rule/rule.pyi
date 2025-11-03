from _typeshed import Incomplete
from persistent import Persistent

class Rule(Persistent):
    """A rule."""

    title: str
    description: str
    event: Incomplete
    enabled: bool
    stop: bool
    cascading: bool
    __parent__: Incomplete
    conditions: Incomplete
    actions: Incomplete
    def __init__(self) -> None: ...

class RuleExecutable:
    """An adapter capable of executing a rule"""

    context: Incomplete
    rule: Incomplete
    event: Incomplete
    def __init__(self, context, rule, event) -> None: ...
    def __call__(self): ...
