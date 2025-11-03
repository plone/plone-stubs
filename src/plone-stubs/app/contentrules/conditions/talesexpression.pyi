from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.browser.formhelper import AddForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from plone.app.contentrules.browser.formhelper import EditForm
from zope.interface import Interface

class ITalesExpressionCondition(Interface):
    """Interface for the configurable aspects of a TALES expression condition.

    This is also used to create add and edit forms, below.
    """

    tales_expression: Incomplete

class TalesExpressionCondition(SimpleItem):
    """The actual persistent implementation of the TALES expression condition
    element.
    """

    tales_expression: str
    element: str
    @property
    def summary(self): ...

class TalesExpressionConditionExecutor:
    """The executor for this condition.

    This is registered as an adapter in configure.zcml
    """

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class TalesExpressionAddForm(AddForm):
    """An add form for tales expression condition."""

    schema = ITalesExpressionCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    def create(self, data): ...

class TalesExpressionAddFormView(ContentRuleFormWrapper):
    form = TalesExpressionAddForm

class TalesExpressionEditForm(EditForm):
    """An edit form for TALES expression condition"""

    schema = ITalesExpressionCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class TalesExpressionEditFormView(ContentRuleFormWrapper):
    form = TalesExpressionEditForm
