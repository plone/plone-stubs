from _typeshed import Incomplete
from zope.interface.interfaces import ObjectEvent

class CheckoutEvent(ObjectEvent):
    working_copy: Incomplete
    relation: Incomplete
    def __init__(self, baseline, wc, relation) -> None: ...

class CheckinEvent(ObjectEvent):
    baseline: Incomplete
    relation: Incomplete
    message: Incomplete
    def __init__(self, wc, baseline, relation, message) -> None: ...

class AfterCheckinEvent(ObjectEvent):
    message: Incomplete
    def __init__(self, new_baseline, checkin_message) -> None: ...

class CancelCheckoutEvent(ObjectEvent):
    baseline: Incomplete
    def __init__(self, wc, baseline) -> None: ...

class WorkingCopyDeletedEvent(ObjectEvent):
    baseline: Incomplete
    relation: Incomplete
    def __init__(self, wc, baseline, relation) -> None: ...

class BeforeCheckoutEvent(ObjectEvent): ...

def handleDeletion(reference, event) -> None: ...
def cancelOnDelete(wc, event) -> None: ...
