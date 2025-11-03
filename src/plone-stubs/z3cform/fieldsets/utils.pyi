def add(form, *args, **kwargs) -> None:
    """Add one or more fields. Keyword argument 'index' can be used to
    specify an index to insert at. Keyword argument 'group' can be used
    to specify the label of a group, which will be found and used or
    created if it doesn't exist.
    """

def remove(form, field_name, prefix=None):
    """Get rid of a field. The omitted field will be returned."""

def move(
    form, field_name, before=None, after=None, prefix=None, relative_prefix=None
) -> None:
    """Move the field with the given name before or after another field."""

def find_source(form, group=None): ...
