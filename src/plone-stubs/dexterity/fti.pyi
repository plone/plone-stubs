from _typeshed import Incomplete
from Products.CMFDynamicViewFTI import fti as base

def get_suffix(fti): ...

class DexterityFTIModificationDescription:
    attribute: Incomplete
    oldValue: Incomplete
    def __init__(self, attribute, oldValue) -> None: ...

class DexterityFTI(base.DynamicViewTypeInformation):
    """A Dexterity FTI"""

    meta_type: str
    default_aliases: Incomplete
    default_actions: Incomplete
    immediate_view: str
    default_view: str
    view_methods: Incomplete
    add_permission: str
    behaviors: Incomplete
    klass: str
    model_source: str
    model_file: str
    schema: str
    schema_policy: str
    factory: Incomplete
    content_meta_type: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
    def Title(self): ...
    def Description(self): ...
    def Metatype(self): ...
    @property
    def hasDynamicSchema(self): ...
    def lookupSchema(self): ...
    def lookupModel(self): ...
    def isConstructionAllowed(self, container): ...
    def possiblePermissionIds(self):
        """Get a vocabulary of Zope 3 permission ids"""

def register(fti) -> None:
    """Helper method to:

    - register an FTI as a local utility
    - register a local factory utility
    - register an add view
    """

def unregister(fti, old_name=None) -> None:
    """Helper method to:

    - unregister the FTI local utility
    - unregister any local factory utility associated with the FTI
    - unregister any local add view associated with the FTI
    """

def unregister_factory(factory_name, site_manager) -> None:
    """Helper method to unregister factories when unused by any dexterity
    type
    """

def ftiAdded(object, event) -> None:
    """When the FTI is created, install local components"""

def ftiRemoved(object, event) -> None:
    """When the FTI is removed, uninstall local components"""

def ftiRenamed(object, event) -> None:
    """When the FTI is modified, ensure local components are still valid"""

def ftiModified(object, event) -> None:
    """When an FTI is modified, re-sync and invalidate the schema, if
    necessary.
    """
