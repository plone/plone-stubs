from _typeshed import Incomplete
from plone.dexterity.browser.add import DefaultAddForm
from plone.dexterity.browser.add import DefaultAddView
from plone.z3cform.fieldsets.group import Group

logger: Incomplete

class AddViewTraverser:
    """Add view traverser."""

    context: Incomplete
    request: Incomplete
    info: Incomplete
    def __init__(self, context, request) -> None: ...
    def traverse(self, name, ignored): ...

class MultilingualAddFormGroup(Group):
    """Multilingual marked group"""

class MultilingualAddForm(DefaultAddForm):
    babel: Incomplete
    group_class = MultilingualAddFormGroup
    def portal_url(self): ...
    babel_content: Incomplete
    def render(self): ...
    def add(self, object) -> None: ...
    @property
    def max_nr_of_buttons(self): ...
    def update(self) -> None: ...

class DefaultMultilingualAddView(DefaultAddView):
    """This is the default add view as looked up by the ++add++ traversal
    namespace adapter in CMF. It is an unnamed adapter on
    (context, request, fti).

    Note that this is registered in ZCML as a simple <adapter />, but we
    also use the <class /> directive to set up security.
    """

    form = MultilingualAddForm
