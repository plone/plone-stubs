from _typeshed import Incomplete
from zope.interface import Interface

class IFormWrapper(Interface):
    """Form wrapper class.

    This class allows "two-step" rendering, with an outer view rendering
    part of the page and the form class rendering the form area.

    In Zope < 2.12, this is the only way to get z3c.form support, because
    the view class takes care of the acquisition requirement.

    In Zope 2.12 and later, this approach is optional: you may register the
    form class directly as a browser view.
    """
    def update() -> None:
        """We use the content provider update/render couple."""
    def render() -> None:
        """We use the content provider update/render couple."""
    form: Incomplete
    form_instance: Incomplete
    index: Incomplete

class IWrappedForm(Interface):
    """Marker interface applied to wrapped forms during rendering.

    This allows different handling of templates, for example.
    """

class IDeferSecurityCheck(Interface):
    """Marker interface applied to the request during traversal.

    This can be used by other code that wants to skip security
    checks during traversal.
    """

class ISubformFactory(Interface):
    """Factory that will instantiate our subforms for ObjectWidget.
    BBB: backported from z3c.form 3.6.x
    """
    def __call__() -> None:
        """Return a default object created to be populated."""
