from _typeshed import Incomplete
from OFS.OrderedFolder import OrderedFolder
from Products.CMFCore.utils import UniqueObject

class ModifierRegistryTool(UniqueObject, OrderedFolder):
    __doc__ = __doc__
    id: str
    alternative_id: str
    meta_type: str
    interfaces: Incomplete
    exceptions: Incomplete
    classes: Incomplete
    modules: Incomplete
    security: Incomplete
    def all_meta_types(self, interfaces=None):
        """Allow adding of objects implementing 'IConditionalModifier' only."""
    orderedFolderSetObject: Incomplete
    def getReferencedAttributes(self, obj):
        """See IModifier"""
    def reattachReferencedAttributes(self, obj, referenced_data) -> None:
        """ """
    def getOnCloneModifiers(self, obj):
        """See IModifier"""
    def beforeSaveModifier(self, obj, obj_clone):
        """See IModifier"""
    def afterRetrieveModifier(self, obj, repo_clone, preserve=None):
        """See IModifier"""
    def register(self, id, modifier, pos: int = -1) -> None:
        """See IModifierRegistrySet"""
    def unregister(self, id) -> None:
        """See IModifierRegistrySet"""
    def edit(self, id, enabled=None, condition=None) -> None:
        """See IModifierRegistrySet"""
    def get(self, id):
        """See IModifierRegistryQuery"""
    def query(self, id, default=None):
        """See IModifierRegistryQuery"""
