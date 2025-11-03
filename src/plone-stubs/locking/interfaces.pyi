from _typeshed import Incomplete
from zope.annotation.interfaces import IAttributeAnnotatable
from zope.interface import Interface

DEFAULT_TIMEOUT: int
MAX_TIMEOUT: Incomplete

class ILockType(Interface):
    """Representation of a type of lock"""

    stealable: Incomplete
    user_unlockable: Incomplete
    timeout: Incomplete

class LockType:
    stealable: Incomplete
    user_unlockable: Incomplete
    timeout: Incomplete
    def __init__(self, name, stealable, user_unlockable, timeout=...) -> None: ...

STEALABLE_LOCK: Incomplete

class ITTWLockable(IAttributeAnnotatable):
    """Marker interface for objects that are lockable through-the-web"""

class INonStealableLock(Interface):
    """Mark an object with this interface to make locks be non-stealable."""

class ILockable(Interface):
    """A component that is lockable.

    Lock tokens are remembered (in annotations). Multiple locks can exist,
    based on lock types. The default lock type, STEALABLE_LOCK, is a lock
    that can be stolen (unless the object is marked with INonStealableLock).

    Most operations take the type as a parameter and operate on the lock token
    associated with a particular type.
    """
    def lock(lock_type=..., children: bool = False) -> None:
        """Lock the object using the given key.

        If children is True, child objects will be locked as well.
        """
    def unlock(lock_type=..., stealable_only: bool = True) -> None:
        """Unlock the object using the given key.

        If stealable_only is true, the operation will only have an effect on
        objects that are stealable(). Thus, non-stealable locks will need
        to pass stealable_only=False to actually get unlocked.
        """
    def clear_locks() -> None:
        """Clear all locks on the object"""
    def locked() -> None:
        """True if the object is locked with any lock."""
    def can_safely_unlock(lock_type=...) -> None:
        """Determine if the current user can safely attempt to unlock the
        object.

        That means:

         - lock_type.user_unlockable is True; and

         - the object is not locked; or
         - the object is only locked with the given lock_type, for the
           current user;
        """
    def stealable(lock_type=...) -> None:
        """Find out if the lock can be stolen.

        This means:

         - the lock type is stealable; and

         - the object is not marked with INonStealableLock; or
         - can_safely_unlock() is true.

        """
    def lock_info() -> None:
        """Get information about locks on object.

        Returns a list containing the following dict for each valid lock:

         - creator : the username of the lock creator
         - time    : the time at which the lock was acquired
         - token   : the underlying lock token
         - type    : the type of lock
        """

class IRefreshableLockable(ILockable):
    """A component that is lockable and whose locks can be refreshed."""
    def refresh_lock(lock_type=...) -> None:
        """Refresh the lock so it expires later."""

class ILockSettings(Interface):
    """A component that looks up configuration settings for lock behavior."""

    lock_on_ttw_edit: Incomplete
