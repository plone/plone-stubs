from _typeshed import Incomplete
from plone.namedfile.browser import DisplayFile

class SiteFavicon(DisplayFile):
    use_denylist: bool
    data: Incomplete
    filename: Incomplete
    def __init__(self, context, request) -> None: ...
