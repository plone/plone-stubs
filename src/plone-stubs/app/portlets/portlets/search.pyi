from ..portlets import base
from _typeshed import Incomplete
from plone.portlets.interfaces import IPortletDataProvider

class ISearchPortlet(IPortletDataProvider):
    """A portlet displaying a (live) search box"""

    enableLivesearch: Incomplete

class Assignment(base.Assignment):
    enableLivesearch: Incomplete
    def __init__(self, enableLivesearch: bool = True) -> None: ...
    @property
    def title(self): ...

class Renderer(base.Renderer):
    render: Incomplete
    action: str
    livesearch_action: str
    def __init__(self, context, request, view, manager, data) -> None: ...
    def enable_livesearch(self): ...
    def search_action(self): ...
    def navigation_root_url(self): ...

class AddForm(base.AddForm):
    schema = ISearchPortlet
    label: Incomplete
    description: Incomplete
    def create(self, data): ...

class EditForm(base.EditForm):
    schema = ISearchPortlet
    label: Incomplete
    description: Incomplete
