from _typeshed import Incomplete
from z3c.form import form

logger: Incomplete

class SendToForm(form.Form):
    label: Incomplete
    description: Incomplete
    fields: Incomplete
    ignoreContext: bool
    mail_template: Incomplete
    def handle_send(self, action) -> None: ...

send_to_form: Incomplete
