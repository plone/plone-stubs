from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from plone.app.contentrules.browser.formhelper import NullAddForm
from zope.interface import Interface

class IDeleteAction(Interface):
    """Interface for the configurable aspects of a delete action."""

class DeleteAction(SimpleItem):
    """The actual persistent implementation of the action element."""

    element: str
    summary: Incomplete

class DeleteActionExecutor:
    """The executor for this action."""

    context: Incomplete
    element: Incomplete
    event: Incomplete
    def __init__(self, context, element, event) -> None: ...
    def __call__(self): ...
    def error(self, obj, error) -> None: ...

class DeleteAddForm(NullAddForm):
    """A degenerate "add form" for delete actions."""
    def create(self): ...
