from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.browser.formhelper import AddForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from plone.app.contentrules.browser.formhelper import EditForm
from zope.interface import Interface

class IWorkflowStateCondition(Interface):
    """Interface for the configurable aspects of a workflow state condition.

    This is also used to create add and edit forms, below.
    """

    wf_states: Incomplete

class WorkflowStateCondition(SimpleItem):
    """The actual persistent implementation of the workflow state condition
    element.py.
    """

    wf_states: Incomplete
    element: str
    @property
    def summary(self): ...

class WorkflowStateConditionExecutor:
    """The executor for this condition."""

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class WorkflowStateAddForm(AddForm):
    """An add form for workflow state conditions."""

    schema = IWorkflowStateCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    def create(self, data): ...

class WorkflowStateAddFormView(ContentRuleFormWrapper):
    form = WorkflowStateAddForm

class WorkflowStateEditForm(EditForm):
    """An edit form for portal type conditions

    z3c.form does all the magic here.
    """

    schema = IWorkflowStateCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class WorkflowStateEditFormView(ContentRuleFormWrapper):
    form = WorkflowStateEditForm
