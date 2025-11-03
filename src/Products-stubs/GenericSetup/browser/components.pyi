from _typeshed import Incomplete
from Products.Five import BrowserView
from zope.interface import Interface

class IComponentsSetupSchema(Interface):
    """Schema for components setup views."""

    body: Incomplete

class ComponentsSetupSchemaAdapter:
    context: Incomplete
    def __init__(self, context) -> None: ...
    body: Incomplete

class ComponentsSetupView(BrowserView):
    """Components setup view for IObjectManagerSite."""

    template: Incomplete
    form_template: Incomplete
    status: str
    adapter: Incomplete
    def update(self) -> None: ...
    def __call__(self): ...

class ComponentsSetupTab(ComponentsSetupView):
    """Components setup ZMI tab for IObjectManagerSite."""

    template: Incomplete
