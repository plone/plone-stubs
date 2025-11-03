from _typeshed import Incomplete
from plone.batching.browser import BatchView
from z3c.form import form
from zope import interface

class ICrudForm(interface.Interface):
    update_schema: Incomplete
    view_schema: Incomplete
    add_schema: Incomplete
    editform_factory: Incomplete
    addform_factory: Incomplete
    batch_size: Incomplete
    def get_items() -> None:
        """Subclasses must a list of all items to edit.

        This list contains tuples of the form ``(id, item)``, where
        the id is a unique identifiers to the items.  The items must
        be adaptable to the schema returned by ``update_schema`` and
        ``view_schema`` methods.
        """
    def add(data) -> None:
        """Subclasses must implement this method to create an item for
        the given `data` *and* add it to a container, and return it.

        The `data` mapping corresponds to the schema returned by
        `add_schema`.

        May raise zope.schema.ValidationError to indicate that there's
        a problem with the add form data.
        """
    def remove(id_item) -> None:
        """Subclasses must implement this method to remove the given
        item from the site.

        It's left to the implementing class to notify of
        ``zope.app.container.contained.ObjectRemovedEvent``.
        """
    def before_update(item, data) -> None:
        """A hook that gets called before an item is updated."""
    def link(item, field) -> None:
        """Return a URL for this item's field or None."""

class AbstractCrudForm:
    """The AbstractCrudForm is not a form but implements methods
    necessary to comply with the ``ICrudForm`` interface:

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ICrudForm, AbstractCrudForm)
      True
    """

    update_schema: Incomplete
    view_schema: Incomplete
    batch_size: int
    @property
    def add_schema(self): ...
    def get_items(self) -> None: ...
    def add(self, data) -> None: ...
    def remove(self, id_item) -> None: ...
    def before_update(self, item, data) -> None: ...
    def link(self, item, field) -> None: ...

class CrudBatchView(BatchView):
    prefix: str
    def make_link(self, pagenumber): ...

class EditSubForm(form.EditForm):
    template: Incomplete
    @property
    def prefix(self): ...
    content: Incomplete
    content_id: Incomplete
    @property
    def fields(self): ...
    def getContent(self): ...
    def getCombinedWidgets(self):
        """Returns pairs of widgets to improve layout"""
    def getTitleWidgets(self): ...
    def getNiceTitles(self): ...

class EditForm(form.Form):
    label: Incomplete
    template: Incomplete
    editsubform_factory = EditSubForm
    @property
    def prefix(self): ...
    def update(self) -> None: ...
    @property
    def batch(self): ...
    def render_batch_navigation(self): ...
    status: Incomplete
    def handle_edit(self, action) -> None: ...
    def handle_delete(self, action) -> None: ...
    def selected_items(self): ...
    def getURL(self):
        """Return url of the current page including parameters.

        Equivalent to plone_context_state/current_page_url, not using plone
        to not need plone stack in testing-setup
        """

class AddForm(form.Form):
    template: Incomplete
    label: Incomplete
    ignoreContext: bool
    ignoreRequest: bool
    @property
    def prefix(self): ...
    @property
    def fields(self): ...
    status: Incomplete
    def handle_add(self, action) -> None: ...

class NullForm:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def update(self) -> None: ...
    def render(self): ...
    __call__ = render

class CrudForm(AbstractCrudForm, form.Form):
    template: Incomplete
    description: str
    editform_factory = EditForm
    addform_factory = AddForm
    subforms: Incomplete
    def update(self) -> None: ...
