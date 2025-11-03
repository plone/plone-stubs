from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.actions import ActionAddForm
from plone.app.contentrules.actions import ActionEditForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from zope.interface import Interface

logger: Incomplete

class IMailAction(Interface):
    """Definition of the configuration available for a mail action"""

    subject: Incomplete
    source: Incomplete
    recipients: Incomplete
    exclude_actor: Incomplete
    message: Incomplete

class MailAction(SimpleItem):
    """
    The implementation of the action defined before
    """

    subject: str
    source: str
    recipients: str
    message: str
    exclude_actor: bool
    element: str
    @property
    def summary(self): ...

class MailActionExecutor:
    """The executor for this action."""

    context: Incomplete
    element: Incomplete
    event: Incomplete
    mail_settings: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class MailAddForm(ActionAddForm):
    """
    An add form for the mail action
    """

    schema = IMailAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    Type = MailAction
    template: Incomplete

class MailAddFormView(ContentRuleFormWrapper):
    form = MailAddForm

class MailEditForm(ActionEditForm):
    """
    An edit form for the mail action
    """

    schema = IMailAction
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    template: Incomplete

class MailEditFormView(ContentRuleFormWrapper):
    form = MailEditForm
