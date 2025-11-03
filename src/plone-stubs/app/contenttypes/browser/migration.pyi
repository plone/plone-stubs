from _typeshed import Incomplete
from z3c.form import form
from zope.interface import Interface

logger: Incomplete

class ChangedBaseClasses:
    def __call__(self, context):
        """Return a vocabulary with all changed base classes."""

class IBaseClassMigratorForm(Interface):
    changed_base_classes: Incomplete

class BaseClassMigratorForm(form.Form):
    label: Incomplete
    fields: Incomplete
    ignoreContext: bool
    enableCSRFProtection: bool
    def updateWidgets(self) -> None: ...
    def handle_migrate(self, action) -> None: ...

BaseClassMigrator: Incomplete
