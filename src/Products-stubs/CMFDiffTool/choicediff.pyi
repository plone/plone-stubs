from Products.CMFDiffTool.TextDiff import AsTextDiff

def title_or_value(vocabulary, value):
    """
    Given a `vocabulary` and a `value` in that vocabulary, return the
    corresponding title or `value` if there is no title.
    """

def get_schemas(obj):
    """Return a tuple (schema, additional_schemata)."""

def get_field_object(obj, field_name):
    """
    Return the `zope.schema.Field` object corresponding to `field_name` in
    `obj`. Return `None` if not found.
    """

class ChoiceDiff(AsTextDiff):
    """
    Diff for choice fields.

    It's implemented as an specialization of `AsTextDiff`. The difference is
    that this class tries to obtain the title corresponding to the value from
    the vocabulary associated with the field in order to provide an
    user-friendlier inline diff to the user.
    """
    def __init__(
        self,
        obj1,
        obj2,
        field,
        id1=None,
        id2=None,
        field_name=None,
        field_label=None,
        schemata=None,
    ) -> None: ...
