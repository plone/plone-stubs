from Products.Five import BrowserView
from zope.cachedescriptors.property import Lazy as lazy_property

class CaptionedImageView(BrowserView):
    """Captioned image template."""
    @lazy_property
    def template(self): ...
    def __call__(self, **options): ...
