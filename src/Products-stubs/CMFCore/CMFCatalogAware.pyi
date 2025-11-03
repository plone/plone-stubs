from _typeshed import Incomplete
from ExtensionClass import Base

logger: Incomplete

class CatalogAware(Base):
    """Mix-in for notifying the catalog tool."""

    security: Incomplete
    def indexObject(self) -> None:
        """Index the object in the portal catalog."""
    def unindexObject(self) -> None:
        """Unindex the object from the portal catalog."""
    def reindexObject(self, idxs=[], update_metadata: int = 1, uid=None) -> None:
        """Reindex the object in the portal catalog."""
    def reindexObjectSecurity(self, skip_self: bool = False) -> None:
        """Reindex security-related indexes on the object."""

class WorkflowAware(Base):
    """Mix-in for notifying the workflow tool."""

    security: Incomplete
    manage_options: Incomplete
    def manage_workflowsTab(self, REQUEST, manage_tabs_message=None):
        """Tab displaying the current workflows for the content object."""
    @security.private
    def notifyWorkflowCreated(self) -> None:
        """Notify the workflow that the object was just created."""

class OpaqueItemManager(Base):
    """Mix-in for managing opaque items."""

    security: Incomplete
    def opaqueItems(self):
        """
        Return opaque items (subelements that are contained
        using something that is not an ObjectManager).
        """
    def opaqueIds(self):
        """
        Return opaque ids (subelements that are contained
        using something that is not an ObjectManager).
        """
    def opaqueValues(self):
        """
        Return opaque values (subelements that are contained
        using something that is not an ObjectManager).
        """

class CMFCatalogAware(CatalogAware, WorkflowAware, OpaqueItemManager):
    """Mix-in for notifying catalog and workflow and managing opaque items."""

def handleContentishEvent(ob, event) -> None:
    """Event subscriber for (IContentish, IObjectEvent) events."""

def handleDynamicTypeCopiedEvent(ob, event) -> None:
    """Event subscriber for (IDynamicType, IObjectCopiedEvent) events."""

def dispatchToOpaqueItems(ob, event) -> None:
    """Dispatch an event to opaque sub-items of a given object."""

def handleOpaqueItemEvent(ob, event) -> None:
    """Event subscriber for (ICallableOpaqueItemEvents, IObjectEvent) events."""
