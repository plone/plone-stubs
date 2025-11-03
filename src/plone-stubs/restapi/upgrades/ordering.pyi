from _typeshed import Incomplete
from Products.Five.browser import BrowserView

ORDER_KEY: Incomplete
QUERY: Incomplete

def safe_utf8(to_utf8): ...
def ensure_child_ordering_object_ids_are_native_strings(container) -> None:
    """Make sure the ordering stored on parent contains only native_string
    object ids.

    This function can be used to fix ordering object ids stored on a parent
    object in a `DefaultOrdering` ordering adapter. When changing object
    ordering via PATCH request we used to incorrectly store ids of reordered
    resources as unicode instead of a bytestring (on python 2). This
    lead to mixed types being stored in the ordering annotations and
    subsequently mixed types being returned when calling `objectIds` of a
    container.

    The problem only exists with python 2 so we do nothing when we are
    called on python 3 by mistake.
    """

class FixOrderingView(BrowserView):
    """Attempt to fix ordering for all potentially affected objects.

    By default will fix ordering object ids for every object that considers
    itself folderish.

    The problem only exists with python 2 so we do nothing when we are
    called on python 3 by mistake.
    """
    def __call__(self): ...
