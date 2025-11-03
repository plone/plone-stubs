from _typeshed import Incomplete
from Persistence import Persistent

MAX32: Incomplete

class EventLog(Persistent):
    """An EventLog encapsulates a collection of log entries."""
    def __init__(self) -> None: ...
    security: Incomplete
    @security.private
    def addEntry(self, entry) -> None:
        """Add a new log entry."""
    @security.private
    def getEntries(self):
        """Return a sequence of log entries."""
    def __len__(self) -> int: ...
    def __nonzero__(self): ...

class LogEntry(Persistent):
    """A LogEntry contains audit information about a version control
    operation. Actions that cause audit records to be created include
    checkout and checkin. Log entry information can be read (but
    not changed) by restricted code."""

    ACTION_CHECKOUT: int
    ACTION_CHECKIN: int
    ACTION_UNCHECKOUT: int
    ACTION_UPDATE: int
    timestamp: Incomplete
    version_id: Incomplete
    action: Incomplete
    message: Incomplete
    user_id: Incomplete
    path: Incomplete
    def __init__(self, version_id, action, path=None, message: str = "") -> None: ...
