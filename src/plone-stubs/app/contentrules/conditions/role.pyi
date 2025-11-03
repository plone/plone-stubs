from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.browser.formhelper import AddForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from plone.app.contentrules.browser.formhelper import EditForm
from zope.interface import Interface

class IRoleCondition(Interface):
    """Interface for the configurable aspects of a role condition.

    This is also used to create add and edit forms, below.
    """

    role_names: Incomplete

class RoleCondition(SimpleItem):
    """The actual persistent implementation of the role condition element.

    Note that we must mix in SimpleItem to keep Zope 2 security happy.
    """

    role_names: Incomplete
    element: str
    @property
    def summary(self): ...

class RoleConditionExecutor:
    """The executor for this condition.

    This is registered as an adapter in configure.zcml
    """

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class RoleAddForm(AddForm):
    """An add form for role rule conditions."""

    schema = IRoleCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    def create(self, data): ...

class RoleAddFormView(ContentRuleFormWrapper):
    form = RoleAddForm

class RoleEditForm(EditForm):
    """An edit form for role conditions"""

    schema = IRoleCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class RoleEditFormView(ContentRuleFormWrapper):
    form = RoleEditForm
