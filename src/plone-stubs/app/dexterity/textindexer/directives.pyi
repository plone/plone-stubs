from plone.supermodel.directives import MetadataListDirective

SEARCHABLE_KEY: str

class searchable(MetadataListDirective):
    """Directive used to mark a field as searchable."""

    key = SEARCHABLE_KEY
    value: str
    def factory(self, *args):
        """The searchable directive accepts as arguments one or more
        fieldnames (string) of fields which should be searchable.
        """
