from _typeshed import Incomplete
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

class IEventsPortlet(IPortletDataProvider):
    count: Incomplete
    state: Incomplete
    search_base_uid: Incomplete
    thumb_scale: Incomplete
    no_thumbs: Incomplete

class Assignment(base.Assignment):
    thumb_scale: Incomplete
    no_thumbs: bool
    count: Incomplete
    state: Incomplete
    search_base_uid: Incomplete
    def __init__(
        self,
        count: int = 5,
        state=None,
        search_base_uid=None,
        thumb_scale=None,
        no_thumbs: bool = False,
    ) -> None: ...
    @property
    def title(self): ...

class Renderer(base.Renderer):
    @property
    def search_base(self): ...
    @property
    def search_base_path(self): ...
    next_url: Incomplete
    prev_url: Incomplete
    def update(self) -> None: ...
    def render(self): ...
    @property
    def available(self): ...
    @property
    def events(self): ...
    def formatted_date(self, event): ...
    def thumb_scale(self):
        """Use override value or read thumb_scale from registry.
        Image sizes must fit to value in allowed image sizes.
        None will suppress thumb.
        """

class AddForm(base.AddForm):
    schema = IEventsPortlet
    label: Incomplete
    description: Incomplete
    def create(self, data): ...

class EditForm(base.EditForm):
    schema = IEventsPortlet
    label: Incomplete
    description: Incomplete
