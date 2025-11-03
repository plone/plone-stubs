from _typeshed import Incomplete
from plone.dexterity.browser.edit import DefaultEditForm

class MultilingualEditForm(DefaultEditForm):
    babel: Incomplete
    def languages(self):
        """Deprecated"""
    def portal_url(self): ...
    babel_content: Incomplete
    def render(self): ...
    @property
    def max_nr_of_buttons(self): ...

DefaultMultilingualEditView: Incomplete
