from _typeshed import Incomplete

class RuleExecutor:
    """An object that can execute rules in its context."""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self, event, bubbled: bool = False, rule_filter=None) -> None: ...
