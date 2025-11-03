from _typeshed import Incomplete
from plone.supermodel import model

VOCAB: str

class IPreviewLink(model.Schema):
    preview_image_link: Incomplete
    preview_caption_link: Incomplete

class PreviewImageScalesFieldAdapter:
    """Get the image_scales for the preview_image_link field"""

    field: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, field, context, request) -> None: ...
    def __call__(self): ...

def update_preview_image_scales(obj, event) -> None:
    """When an image is modified, update the image_scales metadata
    on other items that use it as a preview image.
    """
