from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.actions import ActionAddForm
from plone.app.contentrules.actions import ActionEditForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from zope.interface import Interface

class ICopyAction(Interface):
    """Interface for the configurable aspects of a move action.

    This is also used to create add and edit forms, below.
    """

    target_folder: Incomplete

class CopyAction(SimpleItem):
    """The actual persistent implementation of the action element."""

    target_folder: str
    element: str
    @property
    def summary(self): ...

class CopyActionExecutor:
    """The executor for this action."""

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...
    def error(self, obj, error) -> None: ...
    def generate_id(self, target, old_id): ...

class CopyAddForm(ActionAddForm):
    """An add form for move-to-folder actions."""

    schema = ICopyAction
    label: Incomplete
    description: Incomplete
    Type = CopyAction

class CopyAddFormView(ContentRuleFormWrapper):
    form = CopyAddForm

class CopyEditForm(ActionEditForm):
    """An edit form for copy rule actions.

    z3c.form does all the magic here.
    """

    schema = ICopyAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class CopyEditFormView(ContentRuleFormWrapper):
    form = CopyEditForm
