from _typeshed import Incomplete
from zope.interface import Interface
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

class ILocalrolesModifiedEvent(IObjectModifiedEvent):
    """Interface for event which get fired after local roles of an object has
    been changed.
    """

class ISharingPageRole(Interface):
    """A named utility providing information about roles that are managed
    by the sharing page.

    Utility names should correspond to the role name.

    A user will be able to delegate the given role if a utility can be found
    and the user has the required_permission (or it's None).
    """

    title: Incomplete
    required_permission: Incomplete
    required_interface: Incomplete
