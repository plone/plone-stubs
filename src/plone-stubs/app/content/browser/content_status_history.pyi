from _typeshed import Incomplete
from z3c.form import form
from zope.interface import Interface
from zope.publisher.browser import BrowserView

class IContentStatusHistoryDates(Interface):
    """Interface for the two dates on content status history view"""

    effective_date: Incomplete
    expiration_date: Incomplete

class ContentStatusHistoryDatesForm(form.Form):
    fields: Incomplete
    ignoreContext: bool
    label: str
    effective_date: Incomplete
    expiration_date: Incomplete

class ContentStatusHistoryView(BrowserView):
    template: Incomplete
    dates_form: Incomplete
    errors: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(
        self,
        workflow_action=None,
        paths=[],
        comment: str = "",
        effective_date=None,
        expiration_date=None,
        include_children: bool = False,
        *args,
    ): ...
    def validate(self, workflow_action=None, paths=[]) -> None: ...
    def get_objects_from_path_list(self, paths=[]): ...
    def redirect_to_referrer(self): ...
    def isExpired(self, content): ...
    def human_readable_size(self, size): ...
