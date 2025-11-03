from _typeshed import Incomplete
from z3c.form import group

class Group(group.Group):
    label: str
    description: str
    order: int
    def getContent(self): ...

class GroupFactory:
    fields: Incomplete
    label: Incomplete
    description: Incomplete
    order: Incomplete
    def __init__(
        self, __name__, fields, label=None, description=None, order=None
    ) -> None: ...
    def __call__(self, context, request, parentForm): ...
