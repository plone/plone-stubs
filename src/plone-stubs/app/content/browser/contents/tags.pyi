from _typeshed import Incomplete
from plone.app.content.browser.contents import ContentsBaseAction

class TagsAction:
    template: Incomplete
    order: int
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_options(self): ...

class TagsActionView(ContentsBaseAction):
    required_obj_permission: str
    success_msg: Incomplete
    failure_msg: Incomplete
    def action(self, obj) -> None: ...
