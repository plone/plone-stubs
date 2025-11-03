from _typeshed import Incomplete
from z3c.form import form

class TypeCloneForm(form.AddForm):
    label: Incomplete
    fields: Incomplete
    id: str
    def create(self, data): ...
    status: Incomplete
    def add(self, fti) -> None: ...
    def nextURL(self): ...

TypeCloneFormPage: Incomplete
