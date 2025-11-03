from _typeshed import Incomplete
from plone.app.dexterity.browser.layout import TypeFormLayout
from z3c.form import form

class TypeOverviewForm(form.EditForm):
    enableCSRFProtection: bool
    template: Incomplete
    @property
    def fields(self): ...
    def getContent(self): ...

class TypeOverviewPage(TypeFormLayout):
    form = TypeOverviewForm
    label: Incomplete
