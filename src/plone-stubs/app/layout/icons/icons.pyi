from _typeshed import Incomplete
from plone.memoize import view
from plone.memoize.instance import memoize

class BaseIcon:
    """Helper base class for html rendering"""

    __allow_access_to_unprotected_subobjects__: bool
    def __call__(self): ...
    @memoize
    def html_tag(self): ...

class CatalogBrainContentIcon(BaseIcon):
    context: Incomplete
    request: Incomplete
    brain: Incomplete
    def __init__(self, context, request, brain) -> None: ...
    width: int
    height: int
    title: Incomplete
    @property
    def url(self): ...
    @property
    def description(self): ...
    @view.memoize_contextless
    def extensions_mimetype(self):
        """Return a dict {'.pdf': 'PDF Document', '.ods': '"""

class CMFContentIcon(BaseIcon):
    context: Incomplete
    request: Incomplete
    obj: Incomplete
    def __init__(self, context, request, obj) -> None: ...
    width: int
    height: int
    title: Incomplete
    @property
    def url(self): ...
    @property
    def description(self): ...

class FTIContentIcon(BaseIcon):
    context: Incomplete
    request: Incomplete
    obj: Incomplete
    def __init__(self, context, request, obj) -> None: ...
    width: int
    height: int
    title: Incomplete
    @property
    def url(self): ...
    @property
    def description(self): ...

class PloneSiteContentIcon(BaseIcon):
    context: Incomplete
    request: Incomplete
    obj: Incomplete
    def __init__(self, context, request, obj) -> None: ...
    width: int
    height: int
    title: Incomplete
    @property
    def url(self): ...
    @property
    def description(self): ...

class DefaultContentIcon(BaseIcon):
    context: Incomplete
    request: Incomplete
    obj: Incomplete
    def __init__(self, context, request, obj) -> None: ...
    width: int
    height: int
    title: Incomplete
    @property
    def url(self): ...
    @property
    def description(self): ...
