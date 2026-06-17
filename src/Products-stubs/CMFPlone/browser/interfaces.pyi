from _typeshed import Incomplete
from zope.interface import Interface

class INavigationBreadcrumbs(Interface):
    def breadcrumbs(self) -> None:
        """Breadcrumbs for Navigation."""

class INavigationTabs(Interface):
    def topLevelTabs(self, actions=None, category: str = "portal_tabs") -> None:
        """Top level tabs"""

class INavigationTree(Interface):
    def navigationTreeRootPath(self) -> None:
        """Get the path to the root of the navigation tree"""
    def navigationTree(self) -> None:
        """Navigation tree"""

class ISiteMap(Interface):
    def siteMap(self) -> None:
        """Site map"""

class INavigationPortlet(Interface):
    """Interface for portlet to display navigation tree"""
    def title(self) -> None:
        """The title of the navigation portlet (may be '' to fall back on default)"""
    def display(self) -> None:
        """Whether or not the navtree should be displayed"""
    def includeTop(self) -> None:
        """Whether or not to include the root element in the tree"""
    def navigationRoot(self) -> None:
        """Get the root object"""
    def rootTypeName(self) -> None:
        """Get a normalized content type name for the root object"""
    def createNavTree(self) -> None:
        """Build the actual tree"""
    def isPortalOrDefaultChild(self) -> None:
        """Determine if the context is the portal or a default-document"""

class INewsPortlet(Interface):
    """Interface for portlet to display recent news items"""
    def published_news_items(self) -> None:
        """Returns 5 most recently published News Items in reverse
        chronological order
        """
    def all_news_link(self) -> None:
        """Returns URL, relative to the portal, of a page that display all
        published News Items
        """

class IEventsPortlet(Interface):
    """Interface for portlet to display recent news items"""
    def published_events(self) -> None:
        """Returns 5 most recently published News Items in reverse
        chronological order
        """
    def all_events_link(self) -> None:
        """Returns URL, relative to the portal, of a page that display all
        published News Items
        """
    def prev_events_link(self) -> None:
        """Returns URL, relative to the portal, of a page that display all
        past events.
        """

class IRecentPortlet(Interface):
    """Interface for portlet to display recently modified items"""
    def results(self) -> None:
        """Get the list of recently modified items"""

class ICalendarPortlet(Interface):
    def DateTime(self) -> None:
        """ """
    def current(self) -> None:
        """ """
    def current_day(self) -> None:
        """ """
    def nextYearMax(self) -> None:
        """ """
    def prevYearMin(self) -> None:
        """ """
    def year(self) -> None:
        """ """
    def month(self) -> None:
        """ """
    def prevMonthTime(self) -> None:
        """ """
    def nextMonthTime(self) -> None:
        """ """
    def weeks(self) -> None:
        """ """
    def showStates(self) -> None:
        """ """
    def showPrevMonth(self) -> None:
        """ """
    def showNextMonth(self) -> None:
        """ """
    def getYearAndMonthToDisplay(self) -> None:
        """ """
    def getPreviousMonth(self, month, year) -> None:
        """ """
    def getNextMonth(self, month, year) -> None:
        """ """
    def getWeekdays(self) -> None:
        """Returns a list of Messages for the weekday names."""
    def getEnglishMonthName(self, month) -> None:
        """Returns the English month name."""
    def getMonthName(self, month) -> None:
        """Returns the month name as a Message."""
    def isToday(self, day) -> None:
        """Returns True if the given day and the current month and year equals
        today, otherwise False.
        """

class ISitemapView(Interface):
    """Interface to the view that creates a site map"""
    def createSiteMap(self) -> None:
        """Create the site map data structure"""

class IMainTemplate(Interface):
    """Interface to the view that generated the main_template"""

    macros: Incomplete
    template_name: Incomplete

class IGlobalStatusMessage(Interface):
    """Interface to the view that generated the main_template"""

class IPlone(Interface):
    """ """
    def getCurrentUrl(self) -> None:
        """Returns the actual url plus the query string."""
    def uniqueItemIndex(self, pos: int = 0) -> None:
        """Return an index iterator."""
    def toLocalizedTime(self, time, long_format=None, time_only=None) -> None:
        """The time parameter must be either a string that is suitable for
        initializing a DateTime or a DateTime object. Returns a localized
        string.
        """
    def toLocalizedSize(self, size) -> None:
        """Convert an integer to a localized size string
        3322 -> 3KB in english, 3Ko in french
        """
    def normalizeString(self, text) -> None:
        """Normalizes a title to an id."""
    def isDefaultPageInFolder(self) -> None:
        """Returns a boolean indicating whether the current context is the
        default page of its parent folder.
        """
    def isStructuralFolder(self) -> None:
        """Checks if a given object is a "structural folder".

        That is, a folderish item which does not explicitly implement
        INonStructuralFolder to declare that it doesn\'t wish to be treated
        as a folder by the navtree, the tab generation etc.
        """
    def navigationRootPath(self) -> None:
        """Get the current navigation root path"""
    def navigationRootUrl(self) -> None:
        """Get the url to the current navigation root"""
    def getParentObject(self) -> None:
        """Returns the parent of the current object, equivalent to
        aq_inner(aq_parent(context)), or context.aq_inner.getParentNode()
        """
    def getCurrentFolder(self) -> None:
        """If the context is the default page of a folder or is not itself a
        folder, the parent is returned, otherwise the object itself is
        returned.  This is useful for providing a context for methods
        which wish to act on what is considered the current folder in the
        ui.
        """
    def getCurrentFolderUrl(self) -> None:
        """Returns the URL of the current folder as determined by
        self.getCurrentFolder(), used heavily in actions.
        """
    def getCurrentObjectUrl(self) -> None:
        """Returns the URL of the current object unless that object is a
        folder default page, in which case it returns the parent.
        """
    def isFolderOrFolderDefaultPage(self) -> None:
        """Returns true only if the current object is either a folder (as
        determined by isStructuralFolder) or the default page in context.
        """
    def isPortalOrPortalDefaultPage(self) -> None:
        """Returns true only if the current object is either the portal object
        or the default page of the portal.
        """
    def getViewTemplateId(self) -> None:
        """Returns the template Id corresponding to the default view method of
        the context object.
        """
    def showToolbar(self) -> None:
        """Returns true if the editable border should be shown"""
    def cropText(self, text, length, ellipsis) -> None:
        """Crop text on a word boundary"""
    def site_encoding(self) -> None:
        """returns site encoding"""
    def patterns_settings(self) -> None:
        """returns mockup pattern settings"""

class ISendToForm(Interface):
    """Interface for describing the 'sendto' form"""

    send_to_address: Incomplete
    send_from_address: Incomplete
    comment: Incomplete

class IContactForm(Interface):
    """Interface for describing the contact info form"""

    sender_fullname: Incomplete
    sender_from_address: Incomplete
    subject: Incomplete
    message: Incomplete

class IAuthorFeedbackForm(Interface):
    """Interface describing the author feedback form"""

    subject: Incomplete
    message: Incomplete
    author: Incomplete
    referer: Incomplete
