from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.browser.formhelper import AddForm
from plone.app.contentrules.browser.formhelper import ContentRuleFormWrapper
from plone.app.contentrules.browser.formhelper import EditForm
from zope.interface import Interface

class IFileExtensionCondition(Interface):
    """Interface for the configurable aspects of a portal type condition.

    This is also used to create add and edit forms, below.
    """

    file_extension: Incomplete

class FileExtensionCondition(SimpleItem):
    """The actual persistent implementation of the file extension condition.

    Note that we must mix in Explicit to keep Zope 2 security happy.
    """

    file_extension: str
    element: str
    @property
    def summary(self): ...

class FileExtensionConditionExecutor:
    """The executor for this condition.

    This is registered as an adapter in configure.zcml
    """

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...

class FileExtensionAddForm(AddForm):
    """An add form for file extension rule conditions."""

    schema = IFileExtensionCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete
    def create(self, data): ...

class FileExtensionAddFormView(ContentRuleFormWrapper):
    form = FileExtensionAddForm

class FileExtensionEditForm(EditForm):
    """An edit form for portal type conditions

    z3c.form does all the magic here.
    """

    schema = IFileExtensionCondition
    label: Incomplete
    description: Incomplete
    form_name: Incomplete

class FileExtensionEditFormView(ContentRuleFormWrapper):
    form = FileExtensionEditForm
