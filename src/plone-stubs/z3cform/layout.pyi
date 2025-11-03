from _typeshed import Incomplete
from Products.Five import BrowserView

class FormWrapper(BrowserView):
    """Use this as a base class for your Five view and override the
    'form' attribute with your z3c.form form class.  Your form will
    then be rendered in the contents area of a layout template, the
    'index' attribute.

    Use the 'wrap' function in this module if you don't like defining
    classes.
    """

    form: Incomplete
    index: Incomplete
    request_layer: Incomplete
    form_instance: Incomplete
    def __init__(self, context, request) -> None: ...
    contents: str
    def update(self) -> None:
        """On update, we switch on the zope3 request, needed to work with
        our z3c form. We update here the wrapped form.

        Override this method if you have more than one form.
        """
    def __call__(self):
        """We use the update/render pattern. If a redirect happens in the
        meantime, we simply skip the rendering.
        """
    def render(self):
        """This method renders the outer skeleton template, which in
        turn calls the 'contents' method below.

        We use an indirection to 'self.index' here to allow users to
        override the skeleton template through the 'browser' zcml
        directive. If no index template is set, we look up a an adapter from
        (self, request) to IPageTemplate and use that instead.
        """
    def label(self):
        """Override this method to use a different way of acquiring a
        label or title for your page.  Overriding this with a simple
        attribute works as well.
        """
    @property
    def description(self):
        """Override this property to use a different way of acquiring a
        description for your page.  Overriding this with a simple
        attribute works as well.
        """

def wrap_form(form, /, __wrapper_class=..., **kwargs): ...
