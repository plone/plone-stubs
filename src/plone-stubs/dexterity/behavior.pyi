from _typeshed import Incomplete
from collections.abc import Generator

class DexterityBehaviorAssignable:
    """Support plone.behavior behaviors stored in the FTI"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def supports(self, behavior_interface): ...
    def enumerateBehaviors(self) -> Generator[Incomplete, Incomplete]: ...
