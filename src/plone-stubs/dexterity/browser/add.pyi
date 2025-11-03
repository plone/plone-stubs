from _typeshed import Incomplete
from plone.dexterity.browser.base import DexterityExtensibleForm
from plone.z3cform import layout
from z3c.form import form
from zope.publisher.browser import BrowserPage

class DefaultAddForm(DexterityExtensibleForm, form.AddForm):
    """Standard add form, which is wrapped by DefaultAddView (see below).

    This form is capable of rendering the fields of any Dexterity schema,
    including behaviours. To do that, needs to know the portal_type, which
    can be set as a class variable (in a subclass), or on a created instance.

    By default, the DefaultAddView (see below) will set the portal_type based
    on the FTI.
    """

    portal_type: Incomplete
    immediate_view: Incomplete
    success_message: Incomplete
    ti: Incomplete
    def __init__(self, context, request, ti=None) -> None: ...
    @property
    def additionalSchemata(self): ...
    @property
    def container(self):
        """find container

        return container object.

        In subclasses this could be used to point to a different container.
        """
    def create(self, data): ...
    def add(self, object) -> None: ...
    def nextURL(self): ...
    status: Incomplete
    def handleAdd(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...
    def update(self) -> None: ...
    def updateActions(self) -> None: ...
    @property
    def label(self): ...

class DefaultAddView(layout.FormWrapper, BrowserPage):
    """This is the default add view as looked up by the ++add++ traversal
    namespace adapter in CMF. It is an unnamed adapter on
    (context, request, fti).

    Note that this is registered in ZCML as a simple <adapter />, but we
    also use the <class /> directive to set up security.
    """

    form = DefaultAddForm
    ti: Incomplete
    def __init__(self, context, request, ti) -> None: ...
