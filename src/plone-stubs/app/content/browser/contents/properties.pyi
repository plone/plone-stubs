from _typeshed import Incomplete
from plone.app.content.browser.contents import ContentsBaseAction

class PropertiesAction:
    template: Incomplete
    order: int
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def get_options(self): ...

class PropertiesActionView(ContentsBaseAction):
    success_msg: Incomplete
    failure_msg: Incomplete
    required_obj_permission: str
    effectiveDate: Incomplete
    expirationDate: Incomplete
    copyright: Incomplete
    contributors: Incomplete
    creators: Incomplete
    exclude: Incomplete
    language: Incomplete
    recurse: Incomplete
    def __call__(self): ...
    def action(self, obj, bypass_recurse: bool = False) -> None: ...
