from _typeshed import Incomplete
from BTrees.IOBTree import IOBTree
from BTrees.OOBTree import OOBTree
from OFS.SimpleItem import SimpleItem
from Persistence import Persistent

SPARE_BUCKETS: int
BUCKET_CLASS = OOBTree
DATA_CLASS = IOBTree
STRICT: Incomplete
DEBUG: Incomplete
LOG: Incomplete

def setStrict(on: str = "") -> None:
    """Turn on assertions (which may cause conflicts)"""

def TLOG(*args) -> None: ...

constructTransientObjectContainerForm: Incomplete

def constructTransientObjectContainer(
    self,
    id,
    title: str = "",
    timeout_mins: int = 20,
    addNotification=None,
    delNotification=None,
    limit: int = 0,
    period_secs: int = 20,
    REQUEST=None,
):
    """ """

class MaxTransientObjectsExceeded(Exception): ...

class TransientObjectContainer(SimpleItem):
    """Object which contains items that are automatically flushed
    after a period of inactivity"""

    security: Incomplete
    meta_type: str
    zmi_icon: str
    manage_options: Incomplete
    manage_container: Incomplete
    finalize_lock: Incomplete
    replentish_lock: Incomplete
    gc_lock: Incomplete
    id: Incomplete
    title: Incomplete
    def __init__(
        self,
        id,
        title: str = "",
        timeout_mins: int = 20,
        addNotification=None,
        delNotification=None,
        limit: int = 0,
        period_secs: int = 20,
    ) -> None: ...
    def keys(self): ...
    def raw(self, current_ts): ...
    def items(self): ...
    def values(self): ...
    def __getitem__(self, k): ...
    def __setitem__(self, k, v) -> None: ...
    def __delitem__(self, k) -> None: ...
    def __len__(self) -> int: ...
    def get(self, k, default=None): ...
    def __contains__(self, k) -> bool: ...
    @security.private
    def notifyAdd(self, item) -> None: ...
    @security.private
    def notifyDel(self, item) -> None: ...
    def getId(self): ...
    def new_or_existing(self, key): ...
    def new(self, key): ...
    def setTimeoutMinutes(self, timeout_mins, period_secs: int = 20) -> None:
        """The period_secs parameter is defaulted to preserve backwards API
        compatibility.  In older versions of this code, period was
        hardcoded to 20."""
    def getTimeoutMinutes(self):
        """ """
    def getPeriodSeconds(self):
        """ """
    def getSubobjectLimit(self):
        """ """
    def setSubobjectLimit(self, limit) -> None:
        """ """
    def getAddNotificationTarget(self): ...
    def setAddNotificationTarget(self, f) -> None: ...
    def getDelNotificationTarget(self): ...
    def setDelNotificationTarget(self, f) -> None: ...
    def disableInbandHousekeeping(self) -> None:
        """No longer perform inband housekeeping"""
    def enableInbandHousekeeping(self) -> None:
        """(Re)enable inband housekeeping"""
    def isInbandHousekeepingEnabled(self):
        """Report if inband housekeeping is enabled"""
    def housekeep(self) -> None:
        """Call this from a scheduler at least every
        self._period * (SPARE_BUCKETS - 1) seconds to perform out of band
        housekeeping"""
    def manage_changeTransientObjectContainer(
        self,
        title: str = "",
        timeout_mins: int = 20,
        addNotification=None,
        delNotification=None,
        limit: int = 0,
        period_secs: int = 20,
        REQUEST=None,
    ):
        """Change an existing transient object container."""

def getCurrentTimeslice(period):
    """
    Return an integer representing the 'current' timeslice.
    The current timeslice is guaranteed to be the same integer
    within a 'slice' of time based on a divisor of 'self._period'.
    'self._period' is the number of seconds in a slice.
    """

def getTimeslices(begin, n, period):
    """Get a list of future timeslice integers of 'n' size in descending
    order"""

def roll(low, high, reason): ...

class Increaser(Persistent):
    """
    A persistent object representing a typically increasing integer that
    has conflict resolution which uses the greatest integer out of the three
    available states.
    """

    value: Incomplete
    def __init__(self, v) -> None: ...
    def set(self, v) -> None: ...
    def __call__(self): ...

class Length2(Persistent):
    """
    A persistent object responsible for maintaining a repesention of
    the number of current transient objects.

    Conflict resolution is sensitive to which methods are used to
    change the length.
    """
    def __init__(self, value: int = 0) -> None: ...
    value: Incomplete
    floor: int
    ceiling: Incomplete
    def set(self, value) -> None: ...
    def increment(self, delta) -> None:
        """Increase the length by delta.

        Conflict resolution will take the sum of all the increments."""
    def decrement(self, delta) -> None:
        """Decrease the length by delta.

        Conflict resolution will take the highest decrement."""
    def __call__(self): ...
