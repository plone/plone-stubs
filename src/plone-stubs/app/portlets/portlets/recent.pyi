from ..portlets import base
from _typeshed import Incomplete
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider

class IRecentPortlet(IPortletDataProvider):
    count: Incomplete
    no_icons: Incomplete
    thumb_scale: Incomplete
    no_thumbs: Incomplete

class Assignment(base.Assignment):
    no_icons: bool
    thumb_scale: Incomplete
    no_thumbs: bool
    count: Incomplete
    def __init__(
        self,
        count: int = 5,
        no_icons: bool = False,
        thumb_scale=None,
        no_thumbs: bool = False,
    ) -> None: ...
    @property
    def title(self): ...

class Renderer(base.Renderer):
    title: Incomplete
    anonymous: Incomplete
    navigation_root_url: Incomplete
    typesToShow: Incomplete
    navigation_root_path: Incomplete
    catalog: Incomplete
    def __init__(self, *args) -> None: ...
    def render(self): ...
    @property
    def available(self): ...
    def recent_items(self): ...
    def recently_modified_link(self): ...
    @memoize
    def thumb_scale(self):
        """Use override value or read thumb_scale from registry.
        Image sizes must fit to value in allowed image sizes.
        None will suppress thumb.
        """
    def getMimeTypeIcon(self, obj): ...

class AddForm(base.AddForm):
    schema = IRecentPortlet
    label: Incomplete
    description: Incomplete
    def create(self, data): ...

class EditForm(base.EditForm):
    schema = IRecentPortlet
    label: Incomplete
    description: Incomplete
