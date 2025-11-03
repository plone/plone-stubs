from zope.interface import Interface

class IContentish(Interface):
    """General interface for "contentish" items.

    o These methods need to be implemented by any class that wants to be a
      first-class citizen in the CMF world.

    o CMFCore.PortalContent implements this interface.
    """

    __module__: str
    def SearchableText() -> None:
        """Return a string containing textual information about the content.

        o This string may be the content of a file, or may be synthesized
          by concatenating the string attributes of the instance.

        o Permissions:  View
        """

class IDiscussable(Interface):
    """Interface for things which can have responses."""

    __module__: str
    def createReply(title, text, Creator=None) -> None:
        """Create a reply in the proper place.

        o Returns: HTML (directly or via redirect) # XXX

        o Permission: Reply to item
        """
    def getReplies() -> None:
        """Return a sequence of IDiscussionResponse objects which are
            replies to this IDiscussable

        o Permission: View
        """
    def quotedContents() -> None:
        """Return this object's contents in a form suitable for inclusion
            as a quote in a response.

        o The default implementation returns an empty string.  It might be
           overridden to return a '>' quoted version of the item.

        o Permission: Reply to item
        """

class IOldstyleDiscussable(Interface):
    """Oldstyle discussable interface."""

    __module__: str
    def createReply(title, text, REQUEST, RESPONSE) -> None:
        """Create a reply in the proper place.

        o Returns: HTML (directly or via redirect) # XXX

        o Permission: Reply to item
        """
    def getReplyLocationAndID(REQUEST) -> None:
        """
        This method determines where a user's reply should be stored, and
        what it's ID should be.

        You don't really want to force users to have to select a
        unique ID each time they want to reply to something.  The
        present implementation selects a folder in the Member's home
        folder called 'Correspondence' (creating it if it is missing)
        and finds a free ID in that folder.

        createReply should use this method to determine what the reply
        it creates should be called, and where it should be placed.

        This method (and createReply, I expect) do not really belong in
        this interface.  There should be a DiscussionManager singleton
        (probably the portal object itself) which handles this.

        Permissions: None assigned
        Returns: 2-tuple, containing the container object, and a string ID.
        """
    def getReplyResults() -> None:
        """
        Return the ZCatalog results that represent this object's replies.

        Often, the actual objects are not needed.  This is less expensive
        than fetching the objects.

        Permissions: View
        Returns: sequence of ZCatalog results representing DiscussionResponses
        """
    def getReplies() -> None:
        """
        Return a sequence of the DiscussionResponse objects which are
        associated with this Discussable

        Permissions: View
        Returns: sequence of DiscussionResponses
        """
    def quotedContents() -> None:
        """
        Return this object's contents in a form suitable for inclusion
        as a quote in a response.  The default implementation returns
        an empty string.  It might be overridden to return a '>' quoted
        version of the item.
        """

class IDiscussionResponse(Interface):
    """Interface for objects which are replies to IDiscussable objects."""

    __module__: str
    def inReplyTo(REQUEST=None) -> None:
        """Return the IDiscussable object to which this item is a reply.

        o Permission: None assigned
        """
    def setReplyTo(reply_to) -> None:
        """Make this object a response to the passed object.

        o 'reply_to' is an IDiscussable, or a path (as a string) to one.

        o Raise ValueError if 'reply_to' is not an IDiscussable (or doesn't
          resolve to one as a path).

        o XXX This does not seem like the right exception.

        o Permission: None assigned
        """
    def parentsInThread(size: int = 0) -> None:
        """Return a sequence of IDiscussables which are this object's parents,
            from the point of view of the threaded discussion.

        o Parents are ordered oldest to newest.

        o If 'size' is not zero, only the closest 'size' parents will be
          returned.
        """

class IMinimalDublinCore(Interface):
    """Minimal set of Dublin Core metadata elements."""

    __module__: str
    def Title() -> None:
        """Return a single string, the DCMI Title element (resource name).

        o Permission:  View
        """
    def Description() -> None:
        """Return the DCMI Description element (resource summary).

        o Result is a natural language description of this object.

        o Permission:  View
        """
    def Type() -> None:
        """Return the DCMI Type element (resource type).

        o Result a human-readable type name for the resource (typically
          the Title of its type info object).

        o Permission:  View
        """

class IDublinCore(IMinimalDublinCore):
    """Dublin Core metadata elements supported by CMF and their semantics."""

    __module__: str
    def listCreators() -> None:
        """Return a sequence of DCMI Creator elements (resource authors).

        o Depending on the implementation, this returns the full name(s) of the
          author(s) of the content object or their ids.

        o Permission:  View
        """
    def Creator() -> None:
        """Return the first DCMI Creator element, or an empty string.

        o Permission:  View
        """
    def Subject() -> None:
        """Return a sequence of DCMI Subject elements (resource keywords).

        o Result is zero or more keywords associated with the content object.

        o Permission:  View
        """
    def Publisher() -> None:
        """Return the DCMI Publisher element (resource publisher).

        o Result is the full formal name of the entity or person responsible
          for publishing the resource.

        o Permission:  View
        """
    def listContributors() -> None:
        """Return a sequence of DCMI Contributor elements (resource
            collaborators).

        o Return zero or more collaborators (beyond thos returned by
          'listCreators').

        o Permission:  View
        """
    def Contributors() -> None:
        """Deprecated alias for 'listContributors'.

        o 'initial caps' names are reserved for strings.
        """
    def Date(zone=None) -> None:
        """Return the DCMI Date element (default resource date).

        o Result is a string, formatted 'YYYY-MM-DD H24:MN:SS TZ'.

        o If 'zone' is 'None', return the time in the system default
          timezone.

        o Permission:  View
        """
    def CreationDate(zone=None) -> None:
        """Return the DCMI Date element (date resource created).

        o Result is a string, formatted 'YYYY-MM-DD H24:MN:SS TZ'.

        o If 'zone' is 'None', return the time in the system default
          timezone.

        o Permission:  View
        """
    def EffectiveDate(zone=None) -> None:
        """Return the DCMI Date element (date resource becomes effective).

        o Result is a string, formatted 'YYYY-MM-DD H24:MN:SS TZ', or
          None.

        o If 'zone' is 'None', return the time in the system default
          timezone.

        o Permission:  View
        """
    def ExpirationDate(zone=None) -> None:
        """Return the DCMI Date element (date resource expires).

        o Result is a string, formatted 'YYYY-MM-DD H24:MN:SS TZ', or
          None.

        o If 'zone' is 'None', return the time in the system default
          timezone.

        o Permission:  View
        """
    def ModificationDate(zone=None) -> None:
        """DCMI Date element - date resource last modified.

        o Result is a string, formatted 'YYYY-MM-DD H24:MN:SS TZ'.

        o If 'zone' is 'None', return the time in the system default
          timezone.

        o Permission:  View
        """
    def Format() -> None:
        """Return the DCMI Format element (resource format).

        o Result is the resource's MIME type (e.g. 'text/html',
          'image/png', etc.).

        o Permission:  View
        """
    def Identifier() -> None:
        """Return the DCMI Identifier element (resource ID).

        o Result is a unique ID (a URL) for the resource.

        o Permission:  View
        """
    def Language() -> None:
        """DCMI Language element (resource language).

        o Result it the RFC language code (e.g. 'en-US', 'pt-BR') for the
          resource.

        o Permission:  View
        """
    def Rights() -> None:
        """Return the DCMI Rights element (resource copyright).

        o Return a string describing the intellectual property status, if
          any, of the resource.

        o Permission:  View
        """

class ICatalogableDublinCore(Interface):
    """Provide Zope-internal date attributes for cataloging purposes."""

    __module__: str
    def created() -> None:
        """Return the DateTime form of CreationDate.

        o Permission:  View
        """
    def effective() -> None:
        """Return the DateTime form of EffectiveDate.

        o Permission:  View
        """
    def expires() -> None:
        """Return the DateTime form of ExpirationDate.

        o Permission:  View
        """
    def modified() -> None:
        """Return the DateTime form of ModificationDate

        o Permission:  View
        """

class IMutableMinimalDublinCore(IMinimalDublinCore):
    """Update interface for minimal set of mutable metadata."""

    __module__: str
    def setTitle(title) -> None:
        """Set DCMI Title element - resource name.

        o Permission:  Modify portal content
        """
    def setDescription(description) -> None:
        """Set DCMI Description element - resource summary.

        o Permission:  Modify portal content
        """

class IMutableDublinCore(IMutableMinimalDublinCore, IDublinCore):
    """Update interface for mutable metadata."""

    __module__: str
    def setCreators(creators) -> None:
        """Set DCMI Creator elements - resource authors.

        o Permission:  Modify portal content
        """
    def setSubject(subject) -> None:
        """Set DCMI Subject element - resource keywords.

        o Permission:  Modify portal content
        """
    def setContributors(contributors) -> None:
        """Set DCMI Contributor elements - resource collaborators.

        o Permission:  Modify portal content
        """
    def setEffectiveDate(effective_date) -> None:
        """Set DCMI Date element - date resource becomes effective.

        o Permission:  Modify portal content
        """
    def setExpirationDate(expiration_date) -> None:
        """Set DCMI Date element - date resource expires.

        o Permission:  Modify portal content
        """
    def setFormat(format) -> None:
        """Set DCMI Format element - resource format.

        o Permission:  Modify portal content
        """
    def setLanguage(language) -> None:
        """Set DCMI Language element - resource language.

        o Permission:  Modify portal content
        """
    def setRights(rights) -> None:
        """Set DCMI Rights element - resource copyright.

        o Permission:  Modify portal content
        """

class IDynamicType(Interface):
    """General interface for dynamic items."""

    __module__: str
    def getPortalTypeName() -> None:
        """Return the name of the type information for this object.

        o If the object is uninitialized, return None.

        o Permission:  Public
        """
    def getTypeInfo() -> None:
        """Return the ITypeInformation object for this object.

        o A shortcut to 'getTypeInfo' of portal_types.

        o Permission:  Public
        """
    def getActionInfo(
        action_chain, check_visibility: int = 0, check_condition: int = 0
    ) -> None:
        """Get an Action info mapping specified by a chain of actions.

        o A shortcut to 'getActionInfo' of the related ITypeInformation
          object.

        o Permission:  Public
        """
    def getIconURL() -> None:
        """Get the absolute URL of the icon for the object.

        o This method is used in the \'folder_contents\' view to generate an
          appropriate icon for the items found in the folder.

        o If the content item does not define an attribute named "icon"
          return a "default" icon path (e.g., ``/misc_/dtmldoc.gif``, which is
          the icon used for DTML Documents).

        o Permission:  Public
        """

class ICatalogAware(Interface):
    """Interface for notifying the catalog tool."""

    __module__: str
    def indexObject() -> None:
        """Index the object in the portal catalog."""
    def unindexObject() -> None:
        """Unindex the object from the portal catalog."""
    def reindexObject(idxs=[]) -> None:
        """Reindex the object in the portal catalog.

        If idxs is present, only those indexes are reindexed. The metadata is
        always updated.

        Also update the modification date of the object, unless specific
        indexes were requested.
        """
    def reindexObjectSecurity(skip_self: bool = False) -> None:
        """Reindex security-related indexes on the object.

        Recurses in the children to reindex them too.

        If skip_self is True, only the children will be reindexed. This is a
        useful optimization if the object itself has just been fully
        reindexed, as there's no need to reindex its security twice.
        """

class IWorkflowAware(Interface):
    """Interface for notifying the workflow tool."""

    __module__: str
    def notifyWorkflowCreated() -> None:
        """Notify the workflow that the object was just created."""

class IOpaqueItemManager(Interface):
    """Interface for managing opaque items."""

    __module__: str

class IFolderish(Interface):
    """General interface for "folderish" content items."""

    __module__: str
    def contentItems(filter=None) -> None:
        """Return a sequence of (object ID, object) tuples for
            IContentish and IFolderish sub-objects.

        o Provide a filtered view onto \'objectItems\', allowing only
          "content space" objects to show through.

        o Permission:  Public (not publishable)
        """
    def contentIds(filter=None) -> None:
        """Return a sequence of IDs of IContentish and IFolderish sub-objects.

        o Provide a filtered view onto \'objectIds\', allowing only
          "content space" objects to show through.

        o Permission:  Public (not publishable)

        Returns -- List of object IDs
        """
    def contentValues(filter=None) -> None:
        """Return a sequence of IContentish and IFolderish sub-objects.

        o Provide a filtered view onto \'objectValues\', allowing only
          "content space" objects to show through.

        o Permission:  Public (not publishable)

        Returns -- List of objects
        """
    def listFolderContents(contentFilter=None) -> None:
        """Return a sequence of IContentish and IFolderish sub-objects,
            filtered by the current user's possession of the View permission.

        o Hook around 'contentValues' to let 'folder_contents' be protected.

        o Duplicates 'skip_unauthorized' behavior of 'dtml-in'.

        o Permission -- List folder contents
        """

class ISiteRoot(IFolderish):
    """Marker interface for the object which serves as the root of a site."""

    __module__: str

class ICallableOpaqueItem(Interface):
    """Interface for callable opaque items.

    o Opaque items are subelements that are contained using something that
      is not an ObjectManager.

    o On add, copy, move and delete operations, a marked opaque items
      'manage_afterAdd', 'manage_afterClone' and 'manage_beforeDelete'
      hooks get called if available. Unavailable hooks do not throw
      exceptions.
    """

    __module__: str
    def __init__(obj, id) -> None:
        """Return the opaque item and assign it to 'obj' as attr with 'id'."""
    def __call__() -> None:
        """Return the opaque items value."""
    def getId() -> None:
        """Return the id of the opaque item."""

class ICallableOpaqueItemEvents(Interface):
    """CMF specific events upon copying, renaming and deletion."""

    __module__: str
    def manage_afterClone(item) -> None:
        """After clone event hook."""
    def manage_beforeDelete(item, container) -> None:
        """Before delete event hook."""
    def manage_afterAdd(item, container) -> None:
        """After add event hook."""

class ISyndicatable(Interface):
    """Filter content for syndication."""

    __module__: str
    def synContentValues() -> None:
        """Return a list of IDublinCore objects to be syndicated.

        o For example, 'IFolderish' containers might returns a list of
          recently-created or modified subobjects.

        o Topics might return a sequence of objects from a catalog query.
        """
