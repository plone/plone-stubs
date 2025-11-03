from _typeshed import Incomplete
from plone.app.users.browser.account import AccountPanelForm
from plone.app.users.browser.account import AccountPanelSchemaAdapter
from zope.interface import Interface

HAS_PAE: bool
HAS_DT_VOCAB: bool

class IPersonalPreferences(Interface):
    """Provide schema for personalize form."""

    wysiwyg_editor: Incomplete
    language: Incomplete
    timezone: Incomplete

class PersonalPreferencesPanelAdapter(AccountPanelSchemaAdapter):
    schema = IPersonalPreferences

class PersonalPreferencesPanel(AccountPanelForm):
    """Implementation of personalize form that uses z3c.form."""

    form_name: Incomplete
    schema = IPersonalPreferences
    @property
    def description(self): ...
    def updateWidgets(self) -> None: ...
    def __call__(self): ...

class PersonalPreferencesConfiglet(PersonalPreferencesPanel):
    """Control panel version of the personal preferences panel"""

    template: Incomplete
    tab: str
