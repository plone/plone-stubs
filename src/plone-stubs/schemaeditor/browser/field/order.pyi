from _typeshed import Incomplete
from Products.Five import BrowserView

class FieldOrderView(BrowserView):
    context: Incomplete
    request: Incomplete
    field: Incomplete
    schema: Incomplete
    def __init__(self, context, request) -> None: ...
    def move(self, pos, fieldset_index) -> None:
        """AJAX method to change field position within its schema.
        The position is relative to the fieldset.
        """
    def delete(self) -> None:
        """
        AJAX method to delete a field
        """
