from _typeshed import Incomplete
from plone.app.content.browser.contents import ContentsBaseAction

class WorkflowAction:
    template: Incomplete
    order: int
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_options(self): ...

class WorkflowActionView(ContentsBaseAction):
    required_obj_permission: str
    success_msg: Incomplete
    failure_msg: Incomplete
    pworkflow: Incomplete
    transition_id: Incomplete
    comments: Incomplete
    recurse: Incomplete
    def __call__(self): ...
    def action(self, obj, bypass_recurse: bool = False) -> None: ...
