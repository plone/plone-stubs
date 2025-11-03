from _typeshed import Incomplete
from zope.cachedescriptors.property import Lazy as lazy_property
from zope.interface import Interface

appendix_re: Incomplete
resolveuid_re: Incomplete

class IImageCaptioningEnabler(Interface):
    available: Incomplete

class IResolveUidsEnabler(Interface):
    available: Incomplete

class ImageCaptioningEnabler:
    @property
    def available(self): ...

class ResolveUidsAlwaysEnabled:
    available: bool

def tag(img, **attributes): ...

class ResolveUIDAndCaptionFilter:
    """Parser to convert UUID links and captioned images"""

    singleton_tags: Incomplete
    current_status: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, context=None, request=None) -> None: ...
    order: int
    @lazy_property
    def captioned_image_template(self): ...
    @lazy_property
    def captioned_images(self): ...
    @lazy_property
    def resolve_uids(self): ...
    def is_enabled(self): ...
    def __call__(self, data): ...
    def resolve_scale_data(self, url):
        """return scale url, width and height"""
    def resolve_link(self, href): ...
    def resolve_image(self, src): ...
