from _typeshed import Incomplete
from Acquisition import Explicit
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import PathReprProvider
from plone.dexterity.filerepresentation import DAVCollectionMixin
from plone.dexterity.filerepresentation import DAVResourceMixin
from plone.folder.ordered import CMFOrderedBTreeFolderBase
from Products.CMFCore.CMFCatalogAware import CMFCatalogAware
from Products.CMFCore.PortalContent import PortalContent
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from zope.container.contained import Contained
from zope.interface.declarations import ObjectSpecificationDescriptor

FLOOR_DATE: Incomplete
CEILING_DATE: Incomplete
ATTRIBUTE_NAMES_TO_IGNORE: Incomplete
ASSIGNABLE_CACHE_KEY: str

def get_assignable(context):
    """get the BehaviorAssignable for the context.

    Read from cache on request if needed (twice as fast as lookup)

    returns IBehaviorAssignable providing instance or None
    """

class FTIAwareSpecification(ObjectSpecificationDescriptor):
    """A __providedBy__ decorator that returns the interfaces provided by
    the object, plus the schema interface set in the FTI.
    """
    def __get__(self, inst, cls=None): ...

class AttributeValidator(Explicit):
    """Decide whether attributes should be accessible. This is set as the
    __allow_access_to_unprotected_subobjects__ variable in Dexterity's content
    classes.
    """
    def __call__(self, name, value): ...

class PasteBehaviourMixin: ...

class DexterityContent(DAVResourceMixin, PortalContent, PropertyManager, Contained):
    """Base class for Dexterity content"""

    __providedBy__: Incomplete
    __allow_access_to_unprotected_subobjects__: Incomplete
    security: Incomplete
    portal_type: Incomplete
    title: str
    description: str
    subject: Incomplete
    creators: Incomplete
    contributors: Incomplete
    effective_date: Incomplete
    expiration_date: Incomplete
    format: str
    language: str
    rights: str
    id: Incomplete
    creation_date: Incomplete
    modification_date: Incomplete
    def __init__(
        self,
        id=None,
        title=...,
        subject=...,
        description=...,
        contributors=...,
        effective_date=...,
        expiration_date=...,
        format=...,
        language=...,
        rights=...,
        **kwargs,
    ) -> None: ...
    def __getattr__(self, name): ...
    def UID(self): ...
    @security.private
    def notifyModified(self) -> None: ...
    def addCreator(self, creator=None) -> None: ...
    def setModificationDate(self, modification_date=None) -> None: ...
    def Title(self): ...
    def Description(self): ...
    def Type(self): ...
    def listCreators(self): ...
    def Creator(self): ...
    def Subject(self): ...
    def Publisher(self): ...
    def listContributors(self): ...
    def Contributors(self): ...
    def Date(self, zone=None): ...
    def CreationDate(self, zone=None): ...
    def EffectiveDate(self, zone=None): ...
    def ExpirationDate(self, zone=None): ...
    def ModificationDate(self, zone=None): ...
    def Identifier(self): ...
    def Language(self): ...
    def Rights(self): ...
    def created(self): ...
    def effective(self): ...
    def expires(self): ...
    def modified(self): ...
    def isEffective(self, date): ...
    def setTitle(self, title) -> None: ...
    def setDescription(self, description) -> None: ...
    def setCreators(self, creators) -> None: ...
    def setSubject(self, subject) -> None: ...
    def setContributors(self, contributors) -> None: ...
    def setEffectiveDate(self, effective_date) -> None: ...
    def setExpirationDate(self, expiration_date) -> None: ...
    def setFormat(self, format) -> None: ...
    def setLanguage(self, language) -> None: ...
    def setRights(self, rights) -> None: ...

class Item(PasteBehaviourMixin, BrowserDefaultMixin, DexterityContent):
    """A non-containerish, CMFish item"""

    __providedBy__: Incomplete
    __allow_access_to_unprotected_subobjects__: Incomplete
    isPrincipiaFolderish: int
    manage_options: Incomplete
    __getattr__: Incomplete

class Container(
    PathReprProvider,
    PasteBehaviourMixin,
    DAVCollectionMixin,
    BrowserDefaultMixin,
    CMFCatalogAware,
    CMFOrderedBTreeFolderBase,
    DexterityContent,
):
    """Base class for folderish items"""

    __providedBy__: Incomplete
    __allow_access_to_unprotected_subobjects__: Incomplete
    security: Incomplete
    isPrincipiaFolderish: int
    manage_options: Incomplete
    Title: Incomplete
    setTitle: Incomplete
    Description: Incomplete
    setDescription: Incomplete
    def __init__(self, id=None, **kwargs) -> None: ...
    def __getattr__(self, name): ...
    def manage_delObjects(self, ids=None, REQUEST=None):
        """Delete the contained objects with the specified ids.

        If the current user does not have permission to delete one of the
        objects, an Unauthorized exception will be raised.
        """
    def allowedContentTypes(self, context=None): ...
    def invokeFactory(self, type_name, id, RESPONSE=None, *args, **kw): ...

def reindexOnModify(content, event) -> None:
    """When an object is modified, re-index it in the catalog"""
