from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.actions import ActionAddForm
from plone.app.contentrules.actions import ActionEditForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from zope.interface import Interface

class IMoveAction(Interface):
    """Interface for the configurable aspects of a move action.

    This is also used to create add and edit forms, below.
    """

    target_folder: Incomplete

class MoveAction(SimpleItem):
    """The actual persistent implementation of the action element."""

    target_folder: str
    element: str
    @property
    def summary(self): ...

class MoveActionExecutor:
    """The executor for this action."""

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...
    def error(self, obj, error) -> None: ...
    def generate_id(self, target, old_id): ...

class MoveAddForm(ActionAddForm):
    """An add form for move-to-folder actions."""

    schema = IMoveAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    Type = MoveAction

class MoveAddFormView(ContentRuleFormWrapper):
    form = MoveAddForm

class MoveEditForm(ActionEditForm):
    """An edit form for move rule actions.

    z3c.form does all the magic here.
    """

    schema = IMoveAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class MoveEditFormView(ContentRuleFormWrapper):
    form = MoveEditForm
