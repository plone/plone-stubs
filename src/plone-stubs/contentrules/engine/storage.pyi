from zope.container.ordered import OrderedContainer

class RuleStorage(OrderedContainer):
    """A container for rules."""

    active: bool
    def __init__(self) -> None: ...
