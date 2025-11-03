from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.actions import ActionAddForm
from plone.app.contentrules.actions import ActionEditForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from zope.interface import Interface

class IVersioningAction(Interface):
    """Interface for the configurable aspects of a versioning action.

    This is also used to create add and edit forms, below.
    """

    comment: Incomplete

class VersioningAction(SimpleItem):
    """The actual persistent implementation of the versioning action element."""

    comment: str
    element: str
    @property
    def summary(self): ...

class VersioningActionExecutor:
    """The executor for this action.

    This is registered as an adapter in configure.zcml
    """

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class VersioningAddForm(ActionAddForm):
    """An add form for versioning rule actions."""

    schema = IVersioningAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    Type = VersioningAction

class VersioningAddFormView(ContentRuleFormWrapper):
    form = VersioningAddForm

class VersioningEditForm(ActionEditForm):
    """An edit form for versioning rule actions.

    z3c.form does all the magic here.
    """

    schema = IVersioningAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class VersioningEditFormView(ContentRuleFormWrapper):
    form = VersioningEditForm
