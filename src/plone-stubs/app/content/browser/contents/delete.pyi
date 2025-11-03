from _typeshed import Incomplete
from AccessControl.Permissions import delete_objects
from plone.app.content.browser.contents import ContentsBaseAction

class DeleteAction:
    template: Incomplete
    order: int
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_options(self): ...

class DeleteActionView(ContentsBaseAction):
    required_obj_permission = delete_objects
    success_msg: Incomplete
    failure_msg: Incomplete
    def __call__(self): ...
    def action(self, obj) -> None: ...
