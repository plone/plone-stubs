from _typeshed import Incomplete
from Products.Five.browser import BrowserView

UNWANTED_TAGS: Incomplete

class AnalyticsViewlet(BrowserView):
    render: Incomplete
    record_name: str
    __parent__: Incomplete
    view: Incomplete
    manager: Incomplete
    def __init__(self, context, request, view, manager) -> None: ...
    @property
    def webstats_js(self): ...
    def update(self) -> None:
        """The viewlet manager _updateViewlets requires this method"""

class AnalyticsHeadViewlet(AnalyticsViewlet):
    render: Incomplete
    record_name: str
