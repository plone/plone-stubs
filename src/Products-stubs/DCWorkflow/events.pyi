from _typeshed import Incomplete
from zope.interface.interfaces import ObjectEvent

class TransitionEvent(ObjectEvent):
    workflow: Incomplete
    old_state: Incomplete
    new_state: Incomplete
    transition: Incomplete
    status: Incomplete
    kwargs: Incomplete
    def __init__(
        self, obj, workflow, old_state, new_state, transition, status, kwargs
    ) -> None: ...

class BeforeTransitionEvent(TransitionEvent): ...
class AfterTransitionEvent(TransitionEvent): ...
