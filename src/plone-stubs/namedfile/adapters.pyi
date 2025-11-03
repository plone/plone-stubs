from _typeshed import Incomplete
from zope.interface import Interface

IImageScalesFieldAdapter = Interface

class ImageFieldScales:
    context: Incomplete
    request: Incomplete
    field: Incomplete
    def __init__(self, field, context, request) -> None: ...
    images_view: Incomplete
    def __call__(self): ...
    def get_scales(self, field, width, height):
        """Get a dictionary of available scales for a particular image field,
        with the actual dimensions (aspect ratio of the original image).
        """
    def get_original_image_url(self, fieldname, width, height): ...
