from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.browser.formhelper import AddForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from plone.app.contentrules.browser.formhelper import EditForm
from zope.interface import Interface

class IPortalTypeCondition(Interface):
    """Interface for the configurable aspects of a portal type condition.

    This is also used to create add and edit forms, below.
    """

    check_types: Incomplete

class PortalTypeCondition(SimpleItem):
    """The actual persistent implementation of the portal type condition element.

    Note that we must mix in SimpleItem to keep Zope 2 security happy.
    """

    check_types: Incomplete
    element: str
    @property
    def summary(self): ...

class PortalTypeConditionExecutor:
    """The executor for this condition.

    This is registered as an adapter in configure.zcml
    """

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class PortalTypeAddForm(AddForm):
    """An add form for portal type conditions."""

    schema = IPortalTypeCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    def create(self, data): ...

class PortalTypeAddFormView(ContentRuleFormWrapper):
    form = PortalTypeAddForm

class PortalTypeEditForm(EditForm):
    """An edit form for portal type conditions"""

    schema = IPortalTypeCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class PortalTypeEditFormView(ContentRuleFormWrapper):
    form = PortalTypeEditForm
