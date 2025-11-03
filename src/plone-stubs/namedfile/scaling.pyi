from _typeshed import Incomplete
from plone.namedfile.browser import ALLOWED_INLINE_MIMETYPES
from plone.namedfile.browser import DISALLOWED_INLINE_MIMETYPES
from plone.namedfile.browser import USE_DENYLIST
from Products.Five import BrowserView

logger: Incomplete

class ImageScale(BrowserView):
    """view used for rendering image scales"""

    __roles__: Incomplete
    __allow_access_to_unprotected_subobjects__: int
    data: Incomplete
    allowed_inline_mimetypes = ALLOWED_INLINE_MIMETYPES
    disallowed_inline_mimetypes = DISALLOWED_INLINE_MIMETYPES
    use_denylist = USE_DENYLIST
    context: Incomplete
    request: Incomplete
    url: Incomplete
    srcset: Incomplete
    def __init__(self, context, request, **info) -> None: ...
    def absolute_url(self): ...
    def srcset_attribute(self): ...
    @property
    def title(self):
        """Get the title from the context.

        Let's not fail when we cannot find a title.
        """
    def tag(self, height=..., width=..., alt=..., css_class=None, title=..., **kwargs):
        """Create a tag including scale"""
    def validate_access(self) -> None: ...
    def set_headers(self, response=None) -> None: ...
    def index_html(self):
        """download the image"""
    def manage_DAVget(self):
        """Get scale via webdav."""
    def manage_FTPget(self):
        """Get scale via ftp."""
    def __call__(self): ...
    def HEAD(self, REQUEST, RESPONSE=None):
        """Obtain metainformation about the image implied by the request
        without transfer of the image itself
        """

class ImmutableTraverser:
    scale: Incomplete
    def __init__(self, scale) -> None: ...
    def traverse(self, name, furtherPath): ...

class DefaultImageScalingFactory:
    context: Incomplete
    fieldname: Incomplete
    def __init__(self, context) -> None: ...
    def get_original_value(self, fieldname=None):
        """Get the image value.

        In most cases this will be a NamedBlobImage field.
        """
    def get_raw_data(self, orig_value):
        """Get the raw image data.

        The result may be an open file, in which case it is the responsibility
        of the caller to close it.  Or it may be a string.
        """
    def url(self): ...
    def get_quality(self):
        """Get scaled image quality setting from imaging control panel."""
    def update_parameters(self, **parameters): ...
    def create_scale(self, data, mode, height, width, **parameters): ...
    def handle_image(self, orig_value, orig_data, mode, height, width, **parameters):
        """Return a scaled image, its mimetype format, and width and height."""
    def __call__(
        self,
        fieldname=None,
        mode: str = "scale",
        height=None,
        width=None,
        scale=None,
        **parameters,
    ):
        """Factory for image scales`.

        Note: the 'scale' keyword argument is ignored.
        You should pass a height and width.
        """

class ImageScaling(BrowserView):
    """view used for generating (and storing) image scales"""
    def publishTraverse(self, request, name):
        """used for traversal via publisher, i.e. when using as a url"""
    def browserDefault(self, request) -> None: ...
    def traverse(self, name, furtherPath):
        """used for path traversal, i.e. in zope page templates"""
    def getAvailableSizes(self, fieldname=None): ...
    @property
    def available_sizes(self): ...
    @available_sizes.setter
    def available_sizes(self, value) -> None: ...
    def getImageSize(self, fieldname=None): ...
    def guarded_orig_image(self, fieldname): ...
    def get_orig_image(self, fieldname): ...
    def getRetinaScales(self): ...
    def getHighPixelDensityScales(self): ...
    def modified(self, fieldname=None):
        """Provide a callable to return the modification time of content
        items, so stored image scales can be invalidated.
        """
    def scale(
        self,
        fieldname=None,
        scale=None,
        height=None,
        width=None,
        mode: str = "scale",
        pre: bool = False,
        include_srcset=None,
        **parameters,
    ): ...
    def calculate_srcset(
        self,
        fieldname=None,
        scale=None,
        height=None,
        width=None,
        mode: str = "scale",
        storage=None,
        **parameters,
    ): ...
    def tag(
        self,
        fieldname=None,
        scale=None,
        height=None,
        width=None,
        mode: str = "scale",
        **kwargs,
    ): ...
    def picture(
        self,
        fieldname=None,
        picture_variant=None,
        alt=None,
        css_class=None,
        title=...,
        **kwargs,
    ): ...
    def srcset(
        self,
        fieldname=None,
        scale_in_src: str = "huge",
        sizes: str = "",
        alt=...,
        css_class=None,
        title=...,
        **kwargs,
    ): ...

class NavigationRootScaling(ImageScaling):
    def tag(self, brain, fieldname, **kwargs): ...

class ImagesTest(BrowserView):
    """View for Editors to check how images look and what scales are stored."""
    @property
    def storage(self): ...
    def stored_scales(self): ...
    def clear(self):
        """Clear the scales."""
