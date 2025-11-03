from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from plone.z3cform import layout
from Products.Five.browser import BrowserView
from z3c.form import form

class AddForm(AutoExtensibleForm, form.AddForm):
    """A base add form for content rule.

    Use this for rule elements that require configuration before being added to
    a rule. Element types that do not should use NullAddForm instead.

    Sub-classes should define create() and set the form_fields class variable.

    Notice the subtle difference between AddForm and NullAddform in that the
    create template method for AddForm takes as a parameter a dict 'data':

        def create(self, data):
            return MyAssignment(data.get('foo'))

    whereas the NullAddForm has no data parameter:

        def create(self):
            return MyAssignment()
    """

    ignoreContext: bool
    def updateActions(self) -> None: ...
    def nextURL(self): ...
    def add(self, content) -> None: ...
    status: Incomplete
    def handle_save_action(self, action) -> None: ...
    def handle_cancel_action(self, action): ...

class NullAddForm(BrowserView):
    """An add view that will add its content immediately, without presenting
    a form.

    You should subclass this for rule elements that do not require any
    configuration before being added, and write a create() method that takes no
    parameters and returns the appropriate assignment instance.
    """
    def __call__(self): ...
    def nextURL(self): ...
    def create(self) -> None: ...

class EditForm(AutoExtensibleForm, form.EditForm):
    """An edit form for rule elements."""
    def updateActions(self) -> None: ...
    status: Incomplete
    def handle_save_action(self, action): ...
    def handle_cancel_action(self, action): ...
    def nextURL(self): ...

class ContentRuleFormWrapper(layout.FormWrapper):
    index: Incomplete
