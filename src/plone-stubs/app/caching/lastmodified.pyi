from _typeshed import Incomplete
from zope.interface import Interface

class IDCTimes(Interface): ...

def PageTemplateDelegateLastModified(template):
    """When looking up an ILastModified for a page template, look up an
    ILastModified for its context. May return None, in which case adaptation
    will fail.
    """

def FSPageTemplateDelegateLastModified(template):
    """When looking up an ILastModified for a page template, look up an
    ILastModified for its context. Must register separately or the FSObject
    adapter would otherwise take precedence.
    """

class PersistentLastModified:
    """General ILastModified adapter for persistent objects that have a
    _p_mtime. Note that we don't register this for IPersistent, because
    that interface is mixed into too many things and may end up taking
    precedence over other adapters. Instead, this can be registered on an
    as-needed basis with ZCML.
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...

class OFSFileLastModified(PersistentLastModified):
    """ILastModified adapter for OFS.Image.File"""

class FSObjectLastModified:
    """ILastModified adapter for FSFile and FSImage"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...

class CatalogableDublinCoreLastModified:
    """ILastModified adapter for ICatalogableDublinCore, which includes
    most CMF, Archetypes and Dexterity content
    """

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...

class DCTimesLastModified:
    """ILastModified adapter for zope.dublincore IDCTimes"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...

class ResourceLastModified:
    """ILastModified for Zope 3 style browser resources"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...
