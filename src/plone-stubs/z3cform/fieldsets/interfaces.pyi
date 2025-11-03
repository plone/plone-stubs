from _typeshed import Incomplete
from z3c.form.interfaces import IGroup
from zope.interface import Interface

class IFormExtender(Interface):
    """A component that can add, modify, sort and group fields in a form.

    This should be a named multi adapter from (context, request, form).
    """

    order: Incomplete
    def update() -> None:
        """Modify the form in place. Supported operations include:

        - modify the 'fields' object to change the default fieldset
        - modify the 'groups' list to add, remove or reorder fieldsets
        - modify the 'fields' property of a given group
        """

class IDescriptiveGroup(IGroup):
    """Extension to z3c.form's Group class that can separate out a name,
    a label and a description.
    """

    label: Incomplete
    description: Incomplete

class IGroupFactory(Interface):
    """An object that can be used to create a z3c.form.group.Group."""

    label: Incomplete
    description: Incomplete
    fields: Incomplete

class IExtensibleForm(Interface):
    """A special version of the IGroupForm that is extensible via
    IFormExtender adapters.
    """

    groups: Incomplete
    default_fieldset_label: Incomplete
    def updateFields() -> None:
        """Called during form update to allow updating of self.fields
        and self.groups.
        """
