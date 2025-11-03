from _typeshed import Incomplete

ACQUIRE: int
DISABLED: int
ENABLED: int

class ConstrainTypesBehavior:
    context: Incomplete
    def __init__(self, context) -> None: ...
    def getConstrainTypesMode(self):
        """
        If value is set, use it.
        Default value is ACQUIRED, IF the parent is of the same portal type
        and can be adapted to ISelectableConstrainTypes.
        Else it is DISABLED
        """
    def setConstrainTypesMode(self, mode) -> None: ...
    def canSetConstrainTypes(self): ...
    def getDefaultAddableTypes(self, context=None): ...
    def allowedContentTypes(self, context=None):
        """
        If constraints are enabled, return the locally allowed types.
        If the setting is ACQUIRE, acquire the locally allowed types according
        to the ACQUIRE rules, described in the interface.
        If constraints are disabled, use the default addable types

        This method returns the FTI, NOT the FTI id, like most other methods.
        """
    def getLocallyAllowedTypes(self, context=None):
        """
        If constraints are enabled, return the locally allowed types.
        If the setting is ACQUIRE, acquire the locally allowed types according
        to the ACQUIRE rules, described in the interface.
        If constraints are disabled, use the default addable types
        """
    def setLocallyAllowedTypes(self, types) -> None: ...
    def getImmediatelyAddableTypes(self, context=None):
        """
        If constraints are enabled, return the locally immediately
        addable tpes.
        If the setting is ACQUIRE, acquire the immediately addable types from
        the parent, according to the rules described in the interface.
        If constraints are disabled, use the default addable types
        """
    def setImmediatelyAddableTypes(self, types) -> None: ...
