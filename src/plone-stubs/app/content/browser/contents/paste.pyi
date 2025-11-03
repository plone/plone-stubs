from _typeshed import Incomplete
from plone.app.content.browser.contents import ContentsBaseAction

class PasteAction:
    order: int
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_options(self): ...

class PasteActionView(ContentsBaseAction):
    required_obj_permission: str
    success_msg: Incomplete
    failure_msg: Incomplete
    errors: Incomplete
    dest: Incomplete
    def __call__(self): ...
