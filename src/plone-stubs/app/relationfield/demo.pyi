from _typeshed import Incomplete
from z3c.form import form
from z3c.form.interfaces import IFormLayer

class ITestForm(IFormLayer):
    multiple: Incomplete
    single: Incomplete

class TestForm(form.EditForm):
    fields: Incomplete

TestView: Incomplete
