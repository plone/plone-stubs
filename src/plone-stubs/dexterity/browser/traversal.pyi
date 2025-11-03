from _typeshed import Incomplete
from ZPublisher.BaseRequest import DefaultPublishTraverse

class DexterityPublishTraverse(DefaultPublishTraverse):
    """Override the default browser publisher to make WebDAV work for
    Dexterity objects.

    In part, this works around certain problems with the ZPublisher that make
    DAV requests difficult, and in part it adds support for the '_data'
    pseudo-resource that is shown for folderish content items.
    """

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def browserDefault(self, request): ...
