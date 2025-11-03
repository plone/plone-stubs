from _typeshed import Incomplete

class DefaultRulesetLookup:
    """Default ruleset lookup.

    Only override this if you have very special needs. The safest option is
    to use ``z3c.caching`` to set rulesets.
    """

    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def __call__(self): ...
