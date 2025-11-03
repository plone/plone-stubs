from _typeshed import Incomplete
from zope.browserpage.metadirectives import IViewDirective

import zope.browserpage.metaconfigure
import zope.browserpage.simpleviewclass

def is_method(func): ...
def page(
    _context,
    name,
    permission,
    for_=...,
    layer=...,
    template=None,
    class_=None,
    allowed_interface=None,
    allowed_attributes=None,
    attribute: str = "__call__",
    menu=None,
    title=None,
) -> None: ...

class pages(zope.browserpage.metaconfigure.pages):
    def page(
        self,
        _context,
        name,
        attribute: str = "__call__",
        template=None,
        menu=None,
        title=None,
    ): ...

class IFiveViewDirective(IViewDirective):
    permission: Incomplete

class view(zope.browserpage.metaconfigure.view):
    def __call__(self): ...

def resource(
    _context,
    name,
    layer=...,
    permission: str = "zope.Public",
    file=None,
    image=None,
    template=None,
) -> None: ...
def resourceDirectory(
    _context, name, directory, layer=..., permission: str = "zope.Public"
) -> None: ...

class ViewNotCallableError(AttributeError, NotImplementedError): ...

class simple(zope.browserpage.metaconfigure.simple):
    @property
    def __call__(self): ...

class ViewMixinForTemplates(zope.browserpage.simpleviewclass.simple):
    def __getitem__(self, name): ...

def SimpleViewClass(src, offering=None, used_for=None, bases=(), name: str = ""): ...
