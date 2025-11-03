from _typeshed import Incomplete
from collections.abc import Generator

LOGGER: Incomplete

class FakeView:
    """This fake view is used for enabled z3c forms z2 mode on."""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...

def dynamic_searchable_text_indexer(obj):
    """Dynamic searchable text indexer."""

def get_field_widget(obj, field, request):
    """Returns the field widget of a field in display mode without
    touching any form.
    The `field` should be a z3c form field, not a zope schema field.
    """

def get_searchable_contexts_and_fields(obj) -> Generator[Incomplete]:
    """Returns a generator of tuples, which contains a storage object for
    each schema (adapted `obj`) and a list of fields on this schema which
    are searchable.
    """
