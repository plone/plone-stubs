from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from Products.CMFPlone.browser.interfaces import IContactForm
from z3c.form import form

log: Incomplete

class ContactForm(AutoExtensibleForm, form.Form):
    template: Incomplete
    template_mailview: str
    schema = IContactForm
    ignoreContext: bool
    success: bool
    def mailhost_is_configured(self): ...
    def handle_send(self, action) -> None: ...
    def generate_mail(self, variables, encoding=None): ...
    def send_message(self, data) -> None: ...
    def send_feedback(self) -> None: ...
