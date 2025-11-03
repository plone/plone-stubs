from ..portlets import base
from _typeshed import Incomplete
from plone.portlets.interfaces import IPortletDataProvider

class ILanguagePortlet(IPortletDataProvider):
    """A portlet which shows the available portal languages."""

class Assignment(base.Assignment):
    title: Incomplete

class Renderer(base.Renderer):
    selector: Incomplete
    languages: Incomplete
    navigation_root_url: Incomplete
    def __init__(self, context, request, view, manager, data) -> None: ...
    def show(self): ...
    @property
    def available(self): ...
    def showFlags(self): ...
    def update(self) -> None: ...
    render: Incomplete

class AddForm(base.NullAddForm):
    def create(self): ...
