from ..portlets import base
from _typeshed import Incomplete
from plone.portlets.interfaces import IPortletDataProvider

class IClassicPortlet(IPortletDataProvider):
    """A portlet which can render a classic Plone portlet macro"""

    template: Incomplete
    macro: Incomplete

class Assignment(base.Assignment):
    template: Incomplete
    macro: Incomplete
    def __init__(self, template: str = "", macro: str = "") -> None: ...
    @property
    def title(self): ...

class Renderer(base.Renderer):
    context: Incomplete
    request: Incomplete
    data: Incomplete
    def __init__(self, context, request, view, manager, data) -> None: ...
    render: Incomplete
    def use_macro(self): ...
    def path_expression(self): ...

class AddForm(base.AddForm):
    schema = IClassicPortlet
    label: Incomplete
    description: Incomplete
    def create(self, data): ...

class EditForm(base.EditForm):
    schema = IClassicPortlet
    label: Incomplete
    description: Incomplete
