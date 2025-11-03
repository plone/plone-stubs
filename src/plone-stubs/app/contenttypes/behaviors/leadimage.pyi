from _typeshed import Incomplete
from plone.supermodel import model
from zope.interface import Interface

class ILeadImage(Interface): ...

class ILeadImageBehavior(model.Schema):
    image: Incomplete
    image_caption: Incomplete

class LeadImage:
    context: Incomplete
    def __init__(self, context) -> None: ...
    @property
    def image(self): ...
    @image.setter
    def image(self, value) -> None: ...
    @property
    def image_caption(self): ...
    @image_caption.setter
    def image_caption(self, value) -> None: ...
