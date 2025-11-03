from ..browser.formhelper import AddForm as AddForm
from ..browser.formhelper import EditForm as EditForm
from ..browser.formhelper import NullAddForm as NullAddForm
from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem
from zope.container.contained import Contained

class Assignment(SimpleItem, Contained):
    """Base class for assignments.

    Your type may override the 'title', 'available' and 'data' properties, and
    may
    """
    @property
    def id(self): ...
    @property
    def title(self): ...
    def available(self, context, request):
        """By default, this portlet is always available"""
    @property
    def data(self):
        """Make the assignment itself represent the data object that is being rendered."""

class Renderer:
    """Base class for portlet renderers.

    You must override render() to return a string to render. One way of
    doing this is to write:

        from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
        ...
        render = ViewPageTemplateFile('mytemplate.pt')

    This will render the template mytemplate.pt, found in the same directory
    as your source code file.
    """

    context: Incomplete
    request: Incomplete
    view: Incomplete
    __parent__: Incomplete
    manager: Incomplete
    data: Incomplete
    def __init__(self, context, request, view, manager, data) -> None: ...
    def update(self) -> None: ...
    def render(self) -> None: ...
    @property
    def available(self):
        """By default, portlets are available"""

class DeferredRenderer(Renderer):
    """provide defer functionality via KSS

    in here don't override render() but instead override render_full

    """

    render_preload: Incomplete
    def render_full(self) -> None: ...
    def render(self):
        """render the portlet

        the template gets chosen depending on the initialize state
        """
