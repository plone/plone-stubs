from _typeshed import Incomplete
from plone.protect.utils import safeWrite as safeWrite

logger: Incomplete
X_FRAME_OPTIONS: Incomplete
CSRF_DISABLED: Incomplete
ANNOTATION_KEYS: Incomplete
SAFE_TYPES: Incomplete

class ProtectTransform:
    """
    XXX Need to be extremely careful with everything we do in here
    since an error here would mean the transform is skipped
    and no CSRF protection...
    """

    order: int
    key_manager: Incomplete
    site: Incomplete
    safe_views: Incomplete
    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def parseTree(self, result, encoding): ...
    def transformBytes(self, result, encoding): ...
    def transformString(self, result, encoding): ...
    def transformUnicode(self, result, encoding): ...
    def transformIterable(self, result, encoding):
        """Apply the transform if required"""
    def getContext(self): ...
    def getViewName(self): ...
    def check(self):
        """
        just being very careful here about our check so we don't
        cause errors that prevent this check from happening
        """
    def isActionInSite(self, action, current_url): ...
    def transform(self, result, encoding): ...
