from _typeshed import Incomplete
from plone.app.z3cform.widgets.base import HTMLInputWidget
from z3c.form.widget import Widget

def get_contentbrowser_options(
    context,
    value,
    separator,
    vocabulary_name,
    vocabulary_view,
    field_name=None,
    include_recently_added: bool = True,
): ...

class ContentBrowserWidget(HTMLInputWidget, Widget):
    """ContentBrowser widget for z3c.form."""

    pattern: str
    separator: str
    vocabulary: Incomplete
    vocabulary_override: bool
    vocabulary_view: str
    orderable: bool
    def update(self) -> None: ...
    def get_pattern_options(self): ...
    def items(self):
        """Return item for the widget values for the display template

        Query the catalog for the widget-value (uuids) to only display items
        that the user is allowed to see. Accessing the value with e.g.
        getattr(self.context, self.__name__) would yield the items unfiltered.
        Uses IContentListing for easy access to MimeTypeIcon and more.
        """

def ContentBrowserFieldWidget(field, request, extra=None): ...
