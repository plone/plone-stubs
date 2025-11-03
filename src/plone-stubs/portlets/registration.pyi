from _typeshed import Incomplete
from persistent import Persistent

class PortletType(Persistent):
    """A portlet registration.

    This is persistent so that it can be stored as a local utility.
    """

    title: str
    description: str
    addview: str
    editview: Incomplete
    for_: Incomplete
