from plone.autoform.base import AutoFields
from plone.z3cform.fieldsets.extensible import ExtensibleForm

class AutoExtensibleForm(AutoFields, ExtensibleForm):
    """Mixin class for z3c.form forms that support fields extracted from
    a schema
    """

    showEmptyGroups: bool
    @property
    def schema(self) -> None: ...
    @property
    def additionalSchemata(self):
        """Default to there being no additional schemata"""
    def updateFields(self) -> None: ...

class AutoObjectSubForm(AutoFields):
    """A Mixin class for plone.z3cform.subform.ObjectSubForm forms that
    supports fields being updated from hints in a schema.
    """
    @property
    def schema(self): ...
    def setupFields(self) -> None: ...
