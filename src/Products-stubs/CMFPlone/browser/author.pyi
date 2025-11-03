from _typeshed import Incomplete
from Products.Five.browser import BrowserView
from z3c.form import form

logger: Incomplete

class AuthorFeedbackForm(form.Form):
    fields: Incomplete
    ignoreContext: bool
    portal_state: Incomplete
    portal: Incomplete
    membership_tool: Incomplete
    feedback_template: Incomplete
    def handle_send(self, action) -> None: ...

class AuthorView(BrowserView):
    username: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def makeQuery(self, **kw): ...
    @property
    def is_anonymous(self): ...
    @property
    def is_owner(self): ...
    @property
    def author(self): ...
    @property
    def member_info(self): ...
    @property
    def author_content(self): ...
    def home_folder(self, username): ...
    portal_catalog: Incomplete
    membership_tool: Incomplete
    portal_state: Incomplete
    feedback_form: Incomplete
    email_from_address: Incomplete
    def __call__(self): ...
