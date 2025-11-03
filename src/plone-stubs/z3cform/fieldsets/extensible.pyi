from _typeshed import Incomplete
from z3c.form.group import GroupForm

def order_key(adapter_tuple): ...

class FormExtender:
    """Base class for IFormExtender adapters with convenience APIs"""

    order: int
    context: Incomplete
    request: Incomplete
    form: Incomplete
    def __init__(self, context, request, form) -> None: ...
    def add(self, *args, **kwargs) -> None:
        """Add one or more fields. Keyword argument 'index' can be used to
        specify an index to insert at. Keyword argument 'group' can be used
        to specify the label of a group, which will be found and used or
        created if it doesn't exist.
        """
    def remove(self, field_name, prefix=None):
        """Get rid of a field. The omitted field will be returned."""
    def move(
        self, field_name, before=None, after=None, prefix=None, relative_prefix=None
    ) -> None:
        """Move the field with the given name before or after another field."""

class ExtensibleForm(GroupForm):
    groups: Incomplete
    default_fieldset_label: Incomplete
    def update(self) -> None: ...
    def updateFields(self) -> None: ...
