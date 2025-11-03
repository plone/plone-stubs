from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.actions import ActionAddForm
from plone.app.contentrules.actions import ActionEditForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from zope.interface import Interface

class IWorkflowAction(Interface):
    """Interface for the configurable aspects of a workflow action.

    This is also used to create add and edit forms, below.
    """

    transition: Incomplete

class WorkflowAction(SimpleItem):
    """The actual persistent implementation of the action element."""

    transition: str
    element: str
    @property
    def summary(self): ...

class WorkflowActionExecutor:
    """The executor for this action."""

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...
    def error(self, obj, error) -> None: ...

class WorkflowAddForm(ActionAddForm):
    """An add form for workflow actions."""

    schema = IWorkflowAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    Type = WorkflowAction

class WorkflowAddFormView(ContentRuleFormWrapper):
    form = WorkflowAddForm

class WorkflowEditForm(ActionEditForm):
    """An edit form for workflow rule actions."""

    schema = IWorkflowAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class WorkflowEditFormView(ContentRuleFormWrapper):
    form = WorkflowEditForm
