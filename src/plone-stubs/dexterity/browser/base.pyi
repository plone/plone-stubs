from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm

class DexterityExtensibleForm(AutoExtensibleForm):
    """Mixin class for Dexterity forms that support updatable fields"""

    default_fieldset_label: Incomplete
    @property
    def description(self): ...
    @property
    def schema(self): ...
    @property
    def additionalSchemata(self): ...
