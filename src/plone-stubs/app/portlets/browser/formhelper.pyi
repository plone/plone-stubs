from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from Products.Five.browser import BrowserView
from z3c.form import form

class AddForm(AutoExtensibleForm, form.AddForm):
    """A base add form for portlets.

    Use this for portlet assignments that require configuration before being
    added. Assignment types that do not should use NullAddForm instead.

    Sub-classes should define create() and set the form_fields class variable.

    Notice the subtle difference between AddForm and NullAddform in that the
    create template method for AddForm takes as a parameter a dict 'data':

        def create(self, data):
            return MyAssignment(data.get('foo'))

    whereas the NullAddForm has no data parameter:

        def create(self):
            return MyAssignment()
    """

    template: Incomplete
    label: Incomplete
    def add(self, object): ...
    def __call__(self): ...
    def createAndAdd(self, data): ...
    @property
    def referer(self): ...
    def nextURL(self): ...
    status: Incomplete
    def handleAdd(self, action) -> None: ...
    def handleCancel(self, action): ...

class NullAddForm(BrowserView):
    """An add view that will add its content immediately, without presenting
    a form.

    You should subclass this for portlets that do not require any configuration
    before being added, and write a create() method that takes no parameters
    and returns the appropriate assignment instance.
    """
    def __call__(self): ...
    @property
    def referer(self): ...
    def nextURL(self): ...
    def create(self) -> None: ...

class EditForm(AutoExtensibleForm, form.EditForm):
    """An edit form for portlets."""

    template: Incomplete
    label: Incomplete
    def __call__(self): ...
    @property
    def referer(self): ...
    def nextURL(self): ...
    status: Incomplete
    def handleSave(self, action): ...
    def handleCancel(self, action): ...
