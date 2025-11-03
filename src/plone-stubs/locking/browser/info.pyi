from _typeshed import Incomplete
from Products.Five.browser import BrowserView

class LockInfoViewlet(BrowserView):
    """This is a viewlet which is not hooked up anywhere. It is referenced
    from plone.app.layout. We do it this way to avoid having the  lower-level
    plone.locking depend on these packages, whilst still providing
    an implementation of the info box in a single place.
    """

    template: Incomplete
    __parent__: Incomplete
    context: Incomplete
    request: Incomplete
    view: Incomplete
    manager: Incomplete
    info: Incomplete
    def __init__(self, context, request, view, manager) -> None: ...
    def update(self) -> None: ...
    def render(self): ...
    def lock_is_stealable(self): ...
    def lock_info(self): ...
