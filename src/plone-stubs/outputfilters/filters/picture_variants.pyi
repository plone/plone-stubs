from _typeshed import Incomplete

logger: Incomplete

class PictureVariantsFilter:
    """Converts img tags with a data-picturevariant attribute into picture/source tag's with srcset definitions."""

    order: int
    def is_enabled(self): ...
    current_status: Incomplete
    context: Incomplete
    request: Incomplete
    img2picturetag: Incomplete
    all_picture_variants: Incomplete
    def __init__(self, context=None, request=None) -> None: ...
    def __call__(self, data): ...
