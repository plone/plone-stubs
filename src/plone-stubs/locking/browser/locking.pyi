from _typeshed import Incomplete
from Products.Five import BrowserView

_: Incomplete

class LockingOperations(BrowserView):
    """Lock acquisition and stealing operations"""
    def redirect(self) -> None:
        """Redirect to the context view if needed"""
    def force_unlock(self, redirect: bool = True) -> None:
        """Steal the lock.

        If redirect is True, redirect back to the context URL, i.e. reload
        the page.
        """
    def create_lock(self, redirect: bool = True) -> None:
        """Lock the object if it is unlocked"""
    def safe_unlock(self, redirect: bool = True) -> None:
        """Unlock the object if the current user has the lock"""
    def refresh_lock(self, redirect: bool = True) -> None:
        """Reset the lock start time"""

class LockingInformation(BrowserView):
    """Lock information"""
    def is_locked(self): ...
    def is_locked_for_current_user(self):
        """True if this object is locked for the current user (i.e. the
        current user is not the lock owner)
        """
    def lock_is_stealable(self):
        """Find out if the lock is stealable"""
    def lock_info(self):
        """Get information about the current lock, a dict containing:

        creator - the id of the user who created the lock
        fullname - the full name of the lock creator
        author_page - a link to the home page of the author
        time - the creation time of the lock
        time_difference - a string representing the time since the lock was
        acquired.
        """

class LockingInformationFallback(BrowserView):
    """Fallback view for Lock information.

    This view exists to return sensible defaults if a content type does
    not have the plone.locking behavior active.
    """
    def is_locked(self): ...
    def is_locked_for_current_user(self): ...
    def lock_is_stealable(self): ...
    def lock_info(self) -> None: ...
