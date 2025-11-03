from _typeshed import Incomplete
from plone.app.content.browser.contents import ContentsBaseAction

logger: Incomplete

class RenameAction:
    template: Incomplete
    order: int
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_options(self): ...

class RenameActionView(ContentsBaseAction):
    success_msg: Incomplete
    failure_msg: Incomplete
    errors: Incomplete
    def __call__(self): ...
