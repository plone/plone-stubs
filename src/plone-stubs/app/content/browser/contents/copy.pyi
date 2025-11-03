from _typeshed import Incomplete
from plone.app.content.browser.contents import ContentsBaseAction

class CopyAction:
    order: int
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_options(self): ...

class CopyActionView(ContentsBaseAction):
    success_msg: Incomplete
    failure_msg: Incomplete
    def action(self, obj) -> None: ...
    def finish(self) -> None: ...
    oblist: Incomplete
    def __call__(self): ...
