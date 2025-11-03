from _typeshed import Incomplete
from webresource import ScriptResource
from webresource import StyleResource

class PloneBaseResource:
    """Mixin to override certain aspects of a webresource for Plone needs."""

    context: Incomplete
    expression: Incomplete
    def __init__(self, context, **kw) -> None:
        """Initialize with Plone context"""
    @property
    def file_data(self):
        """Fetch data from using a resource via traversal"""
    @property
    def include(self): ...
    @include.setter
    def include(self, include) -> None: ...
    def eval_expression(self): ...

class PloneScriptResource(PloneBaseResource, ScriptResource):
    """Webresource based ScriptResource for Plone"""

class PloneStyleResource(PloneBaseResource, StyleResource):
    """Webresource based StyleResource for Plone"""
