from _typeshed import Incomplete

LOG: Incomplete
imguid_re: Incomplete

class PortalTransformsTransformer:
    """Invoke portal_transforms to perform a conversion"""

    context: Incomplete
    catalog: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self, value, mimeType): ...
    def check_referenced_images(self, value, target_mimetype, cache_obj) -> None: ...
