from ..browser import formhelper
from ..portlets import base
from _typeshed import Incomplete
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider

class IReviewPortlet(IPortletDataProvider):
    no_icons: Incomplete
    thumb_scale: Incomplete
    no_thumbs: Incomplete

class Assignment(base.Assignment):
    no_icons: bool
    thumb_scale: Incomplete
    no_thumbs: bool
    def __init__(
        self, no_icons: bool = False, thumb_scale=None, no_thumbs: bool = False
    ) -> None: ...
    @property
    def title(self): ...

class Renderer(base.Renderer):
    render: Incomplete
    title: Incomplete
    def __init__(self, *args) -> None: ...
    @property
    def anonymous(self): ...
    @property
    def available(self): ...
    def review_items(self): ...
    def full_review_link(self): ...
    @memoize
    def thumb_scale(self):
        """Use override value or read thumb_scale from registry.
        Image sizes must fit to value in allowed image sizes.
        None will suppress thumb.
        """

class AddForm(formhelper.AddForm):
    schema = IReviewPortlet
    label: Incomplete
    description: Incomplete
    def create(self, data): ...

class EditForm(formhelper.EditForm):
    schema = IReviewPortlet
    label: Incomplete
    description: Incomplete
