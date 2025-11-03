from _typeshed import Incomplete

logger: Incomplete

class AutoFields:
    """Mixin class for the WidgetsView and AutoExtensibleForm classes.
    Takes care of actually processing field updates
    """

    schema: Incomplete
    additionalSchemata: Incomplete
    fields: Incomplete
    groups: Incomplete
    ignorePrefix: bool
    autoGroups: bool
    def updateFieldsFromSchemata(self) -> None: ...
    def getPrefix(self, schema):
        """Get the preferred prefix for the given schema"""
