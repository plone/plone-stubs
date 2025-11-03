from _typeshed import Incomplete
from zope.interface import Interface
from zope.interface.interfaces import IObjectEvent

class IReference(Interface): ...

class IIterateAware(Interface):
    """An object that can be used for check-in/check-out operations."""

ITERATE_LOCK: Incomplete

class CociException(Exception): ...
class CheckinException(CociException): ...
class CheckoutException(CociException): ...
class ConflictError(CheckinException): ...

annotation_key: str

class keys:
    checkout_user: str
    checkout_time: str

class ICheckinEvent(IObjectEvent):
    """a working copy is being checked in, event.object is the working copy, this
    message is sent before any mutation/merge has been done on the objects
    """

    baseline: Incomplete
    relation: Incomplete
    checkin_message: Incomplete

class IAfterCheckinEvent(IObjectEvent):
    """sent out after an object is checked in"""

    checkin_message: Incomplete

class IBeforeCheckoutEvent(IObjectEvent):
    """sent out before a working copy is created"""

class ICheckoutEvent(IObjectEvent):
    """an object is being checked out, event.object is the baseline"""

    working_copy: Incomplete
    relation: Incomplete

class ICancelCheckoutEvent(IObjectEvent):
    """a working copy is being cancelled"""

    baseline: Incomplete

class IWorkingCopyDeletedEvent(IObjectEvent):
    """a working copy is being deleted, this gets called multiple times at
    different states.
    So on cancel checkout and checkin operations, its mostly designed to
    broadcast an event when the user deletes a working copy using the standard
    container paradigms.
    """

    baseline: Incomplete
    relation: Incomplete

class IIterateManagedContent(Interface):
    """Any content managed by iterate - normally a sub-interface is
    applied as a marker to an instance.
    """

class IWorkingCopy(IIterateManagedContent):
    """A working copy/check-out"""

class IBaseline(IIterateManagedContent):
    """A baseline"""

class IWorkingCopyRelation(IReference):
    """A relationship to a working copy"""

class IWCContainerLocator(Interface):
    """A named adapter capable of discovering containers where working
    copies can be created.
    """

    available: Incomplete
    title: Incomplete
    def __call__() -> None:
        """Return a container object, or None if available() is False"""

class ICheckinCheckoutTool(Interface):
    def allowCheckin(content) -> None:
        """
        denotes whether a checkin operation can be performed on the content.
        """
    def allowCheckout(content) -> None:
        """
        denotes whether a checkout operation can be performed on the content.
        """
    def allowCancelCheckout(content) -> None:
        """denotes whether a cancel checkout operation can be performed on the
        content.
        """
    def checkin(content, checkin_messsage) -> None:
        """check the working copy in, this will merge the working copy with
        the baseline
        """
    def checkout(container, content) -> None: ...
    def cancelCheckout(content) -> None: ...

class IObjectCopier(Interface):
    """copies and merges the object state"""
    def copyTo(container) -> None:
        """copy the context to the given container, must also create an AT
        relation using the WorkingCopyRelation.relation name between the
        source and the copy.
        returns the copy.
        """
    def merge() -> None:
        """merge/replace the source with the copy, context is the copy."""

class IObjectArchiver(Interface):
    """iterate needs minimal versioning support"""
    def save(checkin_message) -> None:
        """save a new version of the object"""
    def isVersioned(self) -> None:
        """is this content already versioned"""
    def isVersionable(self) -> None:
        """is versionable check."""
    def isModified(self) -> None:
        """is the resource current state, different than its last saved state."""

class ICheckinCheckoutPolicy(Interface):
    """Checkin / Checkout Policy"""
    def checkin(checkin_message) -> None:
        """checkin the context, if the target has been deleted then raises a
         checkin exception.

        if the object version has changed since the checkout begin (due to
        another checkin) raises a conflict error.
        """
    def checkout(container) -> None:
        """
        checkout the content object into the container, iff another object with
        the same id exists the id is amended, the working copy object is
        returned.

        the content object is locked during checkout.

        raises a CheckoutError if the object is already checked out.
        """
    def cancelCheckout() -> None:
        """coxtent is a checkout (working copy), this method will go ahead and
        delete
        the working copy.
        """
    def getWorkingCopies() -> None: ...
    def getBaseline() -> None: ...
    def getWorkingCopy() -> None: ...

class ICheckinCheckoutReference(Interface):
    def checkout(baseline, wc, references, storage) -> None:
        """
        handle processing of the given references from the baseline
        into the working copy, storage is an annotation for bookkeeping
        information.
        """
    def checkoutBackReferences(baseline, wc, references, storage) -> None: ...
    def checkin(baseline, wc, references, storage) -> None: ...
    def checkinBackReferences(baseline, wc, references, storage) -> None: ...

class IIterateSettings(Interface):
    enable_checkout_workflow: Incomplete
    checkout_workflow_policy: Incomplete
