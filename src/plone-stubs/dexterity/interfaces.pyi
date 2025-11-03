from _typeshed import Incomplete
from Products.CMFCore.interfaces import ITypeInformation
from zope.component.interfaces import IFactory
from zope.interface import Interface
from zope.interface.interfaces import IObjectEvent
from zope.lifecycleevent.interfaces import IModificationDescription

class IContentType(Interface): ...

DAV_FOLDER_DATA_ID: str

class IDexterityFTI(ITypeInformation):
    """The Factory Type Information for Dexterity content objects"""
    def lookupSchema() -> None:
        """Return an InterfaceClass that represents the schema of this type.
        Raises a ValueError if it cannot be found.

        If a schema interface is specified, return this. Otherwise, look up
        the model from either the TTW model source string or a specified
        model XML file, and build a schema from the unnamed schema
        specified in this model.
        """
    def lookupModel() -> None:
        """Return the IModel specified in either the model_source or
        model_file (the former takes precedence). See plone.supermodel for
        more information about this type.

        If neither a model_source or a model_file is given, but a schema is
        given, return a faux model that contains just this schema.

        Note that model.schema is not necessarily going to be the same as
        the schema returned by lookupSchema().
        """
    add_permission: Incomplete
    behaviors: Incomplete
    schema: Incomplete
    model_source: Incomplete
    model_file: Incomplete
    hasDynamicSchema: Incomplete

class IDexterityFTIModificationDescription(IModificationDescription):
    """Descriptor passed with an IObjectModifiedEvent for a Dexterity FTI."""

    attribute: Incomplete
    oldValue: Incomplete

class IDexterityFactory(IFactory):
    """A factory that can create Dexterity objects.

    This factory will create an object by looking up the klass property of
    the FTI with the given portal type. It will also set the portal_type
    on the instance and mark the instance as providing the schema interface
    if it does not do so already.
    """

    portal_type: Incomplete

class IDexteritySchema(Interface):
    """Base class for Dexterity schemata"""

class ISchemaInvalidatedEvent(Interface):
    """Event fired when the schema cache should be invalidated.

    If the portal_type is not given, all schemata will be cleared from the
    cache.
    """

    portal_type: Incomplete

class IDexterityContent(Interface):
    """Marker interface for dexterity-managed content objects"""

class IDexterityItem(IDexterityContent):
    """Marker interface applied to dexterity-managed non-folderish objects"""

class IDexterityContainer(IDexterityContent):
    """Marker interface applied to dexterity-managed folderish objects"""

class IBegunEvent(IObjectEvent):
    """Base begun event"""

class IEditBegunEvent(IBegunEvent):
    """An edit operation was begun"""

class IAddBegunEvent(IBegunEvent):
    """An add operation was begun. The event context is the folder,
    since the object does not exist yet.
    """

class ICancelledEvent(IObjectEvent):
    """Base cancel event"""

class IEditCancelledEvent(ICancelledEvent):
    """An edit operation was cancelled"""

class IAddCancelledEvent(ICancelledEvent):
    """An add operation was cancelled. The event context is the folder,
    since the object does not exist yet.
    """

class IEditFinishedEvent(IObjectEvent):
    """Edit was finished and contents are saved. This event is fired
    even when no changes happen (and no modified event is fired.)
    """

class IDexterityEditForm(Interface):
    """The edit form for a Dexterity content type."""
