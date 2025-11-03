from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.actions import ActionAddForm
from plone.app.contentrules.actions import ActionEditForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from zope.interface import Interface

class INotifyAction(Interface):
    """Interface for the configurable aspects of a notify action.

    This is also used to create add and edit forms, below.
    """

    message: Incomplete
    message_type: Incomplete

class NotifyAction(SimpleItem):
    """The actual persistent implementation of the notify action element."""

    message: str
    message_type: str
    element: str
    @property
    def summary(self): ...

class NotifyActionExecutor:
    """The executor for this action.

    This is registered as an adapter in configure.zcml
    """

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class NotifyAddForm(ActionAddForm):
    """An add form for notify rule actions."""

    schema = INotifyAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    Type = NotifyAction

class NotifyAddFormView(ContentRuleFormWrapper):
    form = NotifyAddForm

class NotifyEditForm(ActionEditForm):
    """An edit form for notify rule actions.

    z3c.form does all the magic here.
    """

    schema = INotifyAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class NotifyEditFormView(ContentRuleFormWrapper):
    form = NotifyEditForm
