from _typeshed import Incomplete

class RecordEvent:
    record: Incomplete
    def __init__(self, record) -> None: ...

class RecordAddedEvent(RecordEvent):
    """record added"""

class RecordRemovedEvent(RecordEvent):
    """record removed"""

class RecordModifiedEvent(RecordEvent):
    oldValue: Incomplete
    newValue: Incomplete
    def __init__(self, record, oldValue, newValue) -> None: ...

def redispatchInterfaceAwareRecordEvents(event) -> None:
    """When an interface-aware record received a record event,
    redispatch the event in a similar manner to the IObjectEvent redispatcher.

    Note that this means one IRecordModifiedEvent will be fired for each
    change to a record.
    """
