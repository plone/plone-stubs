from _typeshed import Incomplete
from z3c.form import form

class FieldsetAddForm(form.AddForm):
    fields: Incomplete
    label: Incomplete
    id: str
    def create(self, data): ...
    def add(self, new_fieldset) -> None: ...
    def nextURL(self): ...

FieldsetAddFormPage: Incomplete
