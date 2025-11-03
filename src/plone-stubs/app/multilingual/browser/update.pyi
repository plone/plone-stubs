from _typeshed import Incomplete
from z3c.form import form

class UpdateLanguageForm(form.Form):
    """A form to change language"""

    fields: Incomplete
    ignoreContext: bool
    output: Incomplete
    status: Incomplete
    def handle_update(self, action): ...

update_language_form: Incomplete
