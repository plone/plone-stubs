from ..portlets import base
from _typeshed import Incomplete
from plone.portlets.interfaces import IPortletDataProvider

class INewsPortlet(IPortletDataProvider):
    count: Incomplete
    state: Incomplete
    thumb_scale: Incomplete
    no_thumbs: Incomplete

class Assignment(base.Assignment):
    thumb_scale: Incomplete
    no_thumbs: bool
    count: Incomplete
    state: Incomplete
    def __init__(
        self,
        count: int = 5,
        state=("published",),
        thumb_scale=None,
        no_thumbs: bool = False,
    ) -> None: ...
    @property
    def title(self): ...

class Renderer(base.Renderer):
    def __init__(self, *args) -> None: ...
    def render(self): ...
    @property
    def available(self): ...
    def published_news_items(self): ...
    def all_news_link(self): ...
    def thumb_scale(self):
        """Use override value or read thumb_scale from registry.
        Image sizes must fit to value in allowed image sizes.
        None will suppress thumb.
        """

class AddForm(base.AddForm):
    schema = INewsPortlet
    label: Incomplete
    description: Incomplete
    def create(self, data): ...

class EditForm(base.EditForm):
    schema = INewsPortlet
    label: Incomplete
    description: Incomplete
