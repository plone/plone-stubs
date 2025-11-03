from _typeshed import Incomplete
from plone.memoize.instance import memoize
from z3c.form import form

class EditForm(form.Form):
    """General edit form for operations.

    This is not registered as a view directly. Instead, we parameterise it
    manually and return it from the ``publishTraverse()`` method in
    ``controlpanel.py``

    This form can be used in two slightly different ways: to edit "global"
    settings for an operation, or to edit "ruleset-specific" overrides. The
    latter mode is invoked when ``rulesetName`` and ``ruleset`` are set.

    The form fields are built from the records in registry corresponding to
    the operation\'s ``options`` list, taking the ``prefix`` into account.
    See ``plone.caching`` for a detailed explanation of how the naming scheme
    works.

    If a global record cannot be found, the option is ignored, i.e. no field
    is rendered for it.

    If we are editing ruleset-specific options and a particular ruleset-
    specific option does not exist, we take the global option field as a
    basis, and create a new record on the fly in ``applyChanges()``.

    The only other complication comes from the fact that we need to clone
    the persistent fields for two purposes:

    * Every record\'s field has the same name -- "value". We need to give it
      a different name in the form, so we clone the field and set a new name.
    * When we create a new ruleset-specific record, we also need a clone of
      the field.

    The ``cloneField()`` method takes care of this for us.

    Once the fields have been set up, the form operations on a dictionary
    context (as returned by ``getContent()``), where the keys are the record
    names.
    """

    template: Incomplete
    context: Incomplete
    request: Incomplete
    operationName: Incomplete
    operation: Incomplete
    rulesetName: Incomplete
    ruleset: Incomplete
    def __init__(
        self, context, request, operationName, operation, rulesetName=None, ruleset=None
    ) -> None: ...
    registry: Incomplete
    fields: Incomplete
    def update(self) -> None: ...
    @memoize
    def getContent(self):
        """Operate on a dictionary context that contains the values for
        all options for which we actually have records.
        """
    def applyChanges(self, data) -> None:
        """Save changes in the given data dictionary to the registry."""
    def cloneField(self, field): ...
    @property
    def title(self): ...
    @property
    def description(self): ...
    status: Incomplete
    def save(self, action): ...
    def cancel(self, action): ...
    def clear(self, action): ...
