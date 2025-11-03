from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.actions import ActionAddForm
from plone.app.contentrules.actions import ActionEditForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from zope.interface import Interface

logger: Incomplete
handler: Incomplete
formatter: Incomplete

class ILoggerAction(Interface):
    """Interface for the configurable aspects of a logger action.

    This is also used to create add and edit forms, below.
    """

    targetLogger: Incomplete
    loggingLevel: Incomplete
    message: Incomplete

class LoggerAction(SimpleItem):
    """The actual persistent implementation of the logger action element.

    Note that we must mix in Explicit to keep Zope 2 security happy.
    """

    targetLogger: str
    loggingLevel: str
    message: str
    element: str
    @property
    def summary(self): ...

class LoggerActionExecutor:
    """The executor for this action.

    This is registered as an adapter in configure.zcml
    """

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def processedMessage(self): ...
    def __call__(self): ...

class LoggerAddForm(ActionAddForm):
    """An add form for logger rule actions."""

    schema = ILoggerAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    Type = LoggerAction

class LoggerAddFormView(ContentRuleFormWrapper):
    form = LoggerAddForm

class LoggerEditForm(ActionEditForm):
    """An edit form for logger rule actions.

    z3c.form does all the magic here.
    """

    schema = ILoggerAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class LoggerEditFormView(ContentRuleFormWrapper):
    form = LoggerEditForm
