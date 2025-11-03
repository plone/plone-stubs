from _typeshed import Incomplete
from Products.Five.browser import BrowserView

class Transform(BrowserView):
    """Invoke a transformation on a RichText field.

    Invoke as::
        context/@@text-transform/fieldname

    Or::
        context/@@text-transform/fieldname/major/minor

    e.g.::
        context/@@text-transform/fieldname/text/plain
    """

    fieldName: Incomplete
    major: Incomplete
    minor: Incomplete
    def __getitem__(self, name): ...
    def __call__(self, value=None, fieldName=None, mimeType=None): ...
