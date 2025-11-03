from .ActionProviderBase import ActionProviderBase
from .utils import SimpleItemWithProperties
from .utils import UniqueObject
from _typeshed import Incomplete
from OFS.ObjectManager import IFAwareObjectManager
from OFS.OrderedFolder import OrderedFolder

logger: Incomplete

class TypeInformation(SimpleItemWithProperties, ActionProviderBase):
    """Base class for information about a content type."""

    manage_options: Incomplete
    security: Incomplete
    title: str
    description: str
    i18n_domain: str
    content_meta_type: str
    icon_expr: str
    add_view_expr: str
    immediate_view: str
    filter_content_types: bool
    allowed_content_types: Incomplete
    allow_discussion: bool
    global_allow: bool
    link_target: str
    id: Incomplete
    def __init__(self, id, **kw) -> None: ...
    manage_aliases: Incomplete
    def manage_setMethodAliases(self, REQUEST) -> None:
        """Config method aliases."""
    def Title(self):
        """
        Return the "human readable" type name (note that it
        may not map exactly to the \'portal_type\', e.g., for
        l10n/i18n or where a single content class is being
        used twice, under different names.
        """
    def Description(self):
        """
        Textual description of the class of objects (intended
        for display in a "constructor list").
        """
    def Metatype(self):
        """
        Returns the Zope 'meta_type' for this content object.
        May be used for building the list of portal content
        meta types.
        """
    def getIcon(self):
        """Returns the icon for this content object."""
    @security.private
    def getIconExprObject(self):
        """Get the expression object representing the icon for this type."""
    @security.public
    def allowType(self, contentType):
        """
        Can objects of 'contentType' be added to containers whose
        type object we are?
        """
    @security.public
    def getId(self): ...
    @security.public
    def allowDiscussion(self):
        """
        Can this type of object support discussion?
        """
    @security.public
    def globalAllow(self):
        """
        Should this type be implicitly addable anywhere?
        """
    @security.public
    def listActions(self, info=None, object=None):
        """Return a sequence of the action info objects for this type."""
    @security.public
    def constructInstance(self, container, id, *args, **kw):
        """Build an instance of the type.

        Builds the instance in 'container', using 'id' as its id.
        Returns the object.
        """
    def getMethodAliases(self):
        """Get method aliases dict."""
    def setMethodAliases(self, aliases):
        """Set method aliases dict."""
    @security.public
    def queryMethodID(self, alias, default=None, context=None):
        """Query method ID by alias."""
    @security.private
    def getInfoData(self):
        """Get the data needed to create an ActionInfo."""

class FactoryTypeInformation(TypeInformation):
    """Portal content factory."""

    security: Incomplete
    product: str
    factory: str
    @security.public
    def isConstructionAllowed(self, container):
        """
        a. Does the factory method exist?

        b. Is the factory method usable?

        c. Does the current user have the permission required in
        order to invoke the factory method?

        d. Do all workflows authorize the creation?
        """

class ScriptableTypeInformation(TypeInformation):
    """Invokes a script rather than a factory to create the content."""

    security: Incomplete
    permission: str
    constructor_path: str
    @security.public
    def isConstructionAllowed(self, container):
        """
        Does the current user have the permission required in
        order to construct an instance?
        """

allowedTypes: Incomplete

class TypesTool(UniqueObject, IFAwareObjectManager, OrderedFolder, ActionProviderBase):
    """Provides a configurable registry of portal content types."""

    id: str
    meta_type: str
    security: Incomplete
    manage_options: Incomplete
    manage_overview: Incomplete
    manage_aliases: Incomplete
    def all_meta_types(self, interfaces=None): ...
    def manage_addTypeInformation(
        self, add_meta_type, id=None, typeinfo_name=None, RESPONSE=None
    ) -> None:
        """Create a TypeInformation in self."""
    def manage_setTIMethodAliases(self, REQUEST) -> None:
        """Config method aliases."""
    def getTypeInfo(self, contentType):
        """
        Return an instance which implements the
        TypeInformation interface, corresponding to
        the specified 'contentType'.  If contentType is actually
        an object, rather than a string, attempt to look up
        the appropriate type info using its portal_type.
        """
    def listTypeInfo(self, container=None):
        """
        Return a sequence of instances which implement the
        TypeInformation interface, one for each content
        type registered in the portal.
        """
    def listContentTypes(self, container=None, by_metatype: int = 0):
        """List type info IDs.

        Passing 'by_metatype' is deprecated (type information may not
        correspond 1:1 to an underlying meta_type). This argument will be
        removed when CMFCore/dtml/catalogFind.dtml doesn't need it anymore.
        """
    @security.public
    def constructContent(self, type_name, container, id, RESPONSE=None, *args, **kw):
        """
        Build an instance of the appropriate content class in
        'container', using 'id'.
        """
    @security.private
    def listActions(self, info=None, object=None):
        """List all the actions defined by a provider."""
    def listMethodAliasKeys(self):
        """List all defined method alias names."""
