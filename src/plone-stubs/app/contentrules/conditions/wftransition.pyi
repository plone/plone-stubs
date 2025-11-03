from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.browser.formhelper import AddForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from plone.app.contentrules.browser.formhelper import EditForm
from zope.interface import Interface

class IWorkflowTransitionCondition(Interface):
    """Interface for the configurable aspects of a workflow transition condition.

    This is also used to create add and edit forms, below.
    """

    wf_transitions: Incomplete

class WorkflowTransitionCondition(SimpleItem):
    """The actual persistent implementation of the workflow transition
    condition element.
    """

    wf_transitions: Incomplete
    element: str
    @property
    def summary(self): ...

class WorkflowTransitionConditionExecutor:
    """The executor for this condition."""

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class WorkflowTransitionAddForm(AddForm):
    """An add form for workflow transition conditions."""

    schema = IWorkflowTransitionCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    def create(self, data): ...

class WorkflowTransitionAddFormView(ContentRuleFormWrapper):
    form = WorkflowTransitionAddForm

class WorkflowTransitionEditForm(EditForm):
    """An edit form for portal type conditions

    z3c.form does all the magic here.
    """

    schema = IWorkflowTransitionCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class WorkflowTransitionEditFormView(ContentRuleFormWrapper):
    form = WorkflowTransitionEditForm
