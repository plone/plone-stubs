from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.browser.formhelper import AddForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from plone.app.contentrules.browser.formhelper import EditForm
from zope.interface import Interface

class IGroupCondition(Interface):
    """Interface for the configurable aspects of a group condition.

    This is also used to create add and edit forms, below.
    """

    group_names: Incomplete

class GroupCondition(SimpleItem):
    """The actual persistent implementation of the group condition element.

    Note that we must mix in SimpleItem to keep Zope 2 security happy.
    """

    group_names: Incomplete
    element: str
    @property
    def summary(self): ...

class GroupConditionExecutor:
    """The executor for this condition.

    This is registered as an adapter in configure.zcml
    """

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class GroupAddForm(AddForm):
    """An add form for group rule conditions."""

    schema = IGroupCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    def create(self, data): ...

class GroupAddFormView(ContentRuleFormWrapper):
    form = GroupAddForm

class GroupEditForm(EditForm):
    """An edit form for group conditions"""

    schema = IGroupCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class GroupEditFormView(ContentRuleFormWrapper):
    form = GroupAddForm
