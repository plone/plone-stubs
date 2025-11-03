from _typeshed import Incomplete
from z3c.form import form

class TypeAddForm(form.AddForm):
    label: Incomplete
    fields: Incomplete
    id: str
    fti_id: Incomplete
    def create(self, data): ...
    status: Incomplete
    def add(self, fti) -> None: ...
    def nextURL(self): ...

TypeAddFormPage: Incomplete
