from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from Products.Five.browser import BrowserView
from z3c.form.form import Form

logger: Incomplete

class ModifyTranslationsForm(BrowserView):
    def available_languages(self): ...
    def get_translation(self, language): ...

class ConnectTranslation(AutoExtensibleForm, Form):
    schema: Incomplete
    ignoreContext: bool
    label: Incomplete
    description: Incomplete
    status: Incomplete
    def handle_add(self, action): ...

class DisconnectTranslation(BrowserView):
    tpl: Incomplete
    def __call__(self): ...
