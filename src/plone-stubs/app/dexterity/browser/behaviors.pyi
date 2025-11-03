from _typeshed import Incomplete
from plone.app.dexterity.browser.layout import TypeFormLayout
from z3c.form import form

TTW_BEHAVIOR_BLACKLIST: Incomplete

def behaviorConfigurationModified(object, event) -> None: ...

class BehaviorConfigurationAdapter:
    def __init__(self, context) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def __iter__(self): ...

class TypeBehaviorsForm(form.EditForm):
    template: Incomplete
    label: Incomplete
    description: Incomplete
    successMessage: Incomplete
    noChangesMessage: Incomplete
    buttons: Incomplete
    def getContent(self): ...
    @property
    def behaviors(self):
        """Return dict of (behavior name, reg)"""
    @property
    def fields(self): ...

class TypeBehaviorsPage(TypeFormLayout):
    form = TypeBehaviorsForm
    label: Incomplete
