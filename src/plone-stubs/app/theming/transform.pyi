from _typeshed import Incomplete

LOGGER: Incomplete

class ThemeTransform:
    """Late stage in the 8000's transform chain. When plone.app.blocks is
    used, we can benefit from lxml parsing having taken place already.
    """

    order: int
    published: Incomplete
    request: Incomplete
    def __init__(self, published, request) -> None: ...
    def debug_theme(self):
        """Check if the theme should be debugged
        We will debug the theme
        when we have a truish diazo.debug parameter in the request
        """
    def develop_theme(self):
        """Check if the theme should be recompiled
        every time the transform is applied
        """
    def setupTransform(self, runtrace: bool = False): ...
    def getSettings(self): ...
    def parseTree(self, result): ...
    def transformBytes(self, result, encoding): ...
    def transformString(self, result, encoding): ...
    def transformUnicode(self, result, encoding): ...
    def transformIterable(self, result, encoding):
        """Apply the transform if required"""
