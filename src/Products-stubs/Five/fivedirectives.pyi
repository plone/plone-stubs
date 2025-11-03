from _typeshed import Incomplete
from zope.browserresource.metadirectives import IBasicResourceInformation
from zope.interface import Interface

class ISizableDirective(Interface):
    """Attach sizable adapters to classes."""

    class_: Incomplete

class IPagesFromDirectoryDirective(IBasicResourceInformation):
    """Register each file in a skin directory as a page resource"""

    for_: Incomplete
    module: Incomplete
    directory: Incomplete
