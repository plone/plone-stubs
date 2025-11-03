from _typeshed import Incomplete
from plone.autoform.base import AutoFields
from z3c.form.form import DisplayForm
from z3c.form.interfaces import IFormLayer

class WidgetsView(AutoFields, DisplayForm):
    """Mix-in to allow widgets (in view mode) to be accessed from browser
    views.
    """

    schema: Incomplete
    additionalSchemata: Incomplete
    request_layer = IFormLayer
    w: Incomplete
    fieldsets: Incomplete
    def update(self) -> None: ...
    def render(self): ...
    def __call__(self): ...
