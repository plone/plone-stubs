from _typeshed import Incomplete
from zope.interface import Interface

class INavigationBreadcrumbs(Interface):
    def breadcrumbs() -> None:
        """Breadcrumbs for Navigation."""

class INavigationTabs(Interface):
    def topLevelTabs(actions=None, category: str = "portal_tabs") -> None:
        """Top level tabs"""

class INavigationTree(Interface):
    def navigationTreeRootPath() -> None:
        """Get the path to the root of the navigation tree"""
    def navigationTree() -> None:
        """Navigation tree"""

class ISiteMap(Interface):
    def siteMap() -> None:
        """Site map"""

class INavigationPortlet(Interface):
    """Interface for portlet to display navigation tree"""
    def title() -> None:
        """The title of the navigation portlet (may be '' to fall back on default)"""
    def display() -> None:
        """Whether or not the navtree should be displayed"""
    def includeTop() -> None:
        """Whether or not to include the root element in the tree"""
    def navigationRoot() -> None:
        """Get the root object"""
    def rootTypeName() -> None:
        """Get a normalized content type name for the root object"""
    def createNavTree() -> None:
        """Build the actual tree"""
    def isPortalOrDefaultChild() -> None:
        """Determine if the context is the portal or a default-document"""

class INewsPortlet(Interface):
    """Interface for portlet to display recent news items"""
    def published_news_items() -> None:
        """Returns 5 most recently published News Items in reverse
        chronological order
        """
    def all_news_link() -> None:
        """Returns URL, relative to the portal, of a page that display all
        published News Items
        """

class IEventsPortlet(Interface):
    """Interface for portlet to display recent news items"""
    def published_events() -> None:
        """Returns 5 most recently published News Items in reverse
        chronological order
        """
    def all_events_link() -> None:
        """Returns URL, relative to the portal, of a page that display all
        published News Items
        """
    def prev_events_link() -> None:
        """Returns URL, relative to the portal, of a page that display all
        past events.
        """

class IRecentPortlet(Interface):
    """Interface for portlet to display recently modified items"""
    def results() -> None:
        """Get the list of recently modified items"""

class ICalendarPortlet(Interface):
    def DateTime() -> None:
        """ """
    def current() -> None:
        """ """
    def current_day() -> None:
        """ """
    def nextYearMax() -> None:
        """ """
    def prevYearMin() -> None:
        """ """
    def year() -> None:
        """ """
    def month() -> None:
        """ """
    def prevMonthTime() -> None:
        """ """
    def nextMonthTime() -> None:
        """ """
    def weeks() -> None:
        """ """
    def showStates() -> None:
        """ """
    def showPrevMonth() -> None:
        """ """
    def showNextMonth() -> None:
        """ """
    def getYearAndMonthToDisplay() -> None:
        """ """
    def getPreviousMonth(month, year) -> None:
        """ """
    def getNextMonth(month, year) -> None:
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
    def createSiteMap() -> None:
        """Create the site map data structure"""

class IMainTemplate(Interface):
    """Interface to the view that generated the main_template"""

    macros: Incomplete
    template_name: Incomplete

class IGlobalStatusMessage(Interface):
    """Interface to the view that generated the main_template"""

class IPlone(Interface):
    """ """
    def getCurrentUrl() -> None:
        """Returns the actual url plus the query string."""
    def uniqueItemIndex(pos: int = 0) -> None:
        """Return an index iterator."""
    def toLocalizedTime(time, long_format=None, time_only=None) -> None:
        """The time parameter must be either a string that is suitable for
        initializing a DateTime or a DateTime object. Returns a localized
        string.
        """
    def toLocalizedSize(size) -> None:
        """Convert an integer to a localized size string
        3322 -> 3KB in english, 3Ko in french
        """
    def normalizeString(text) -> None:
        """Normalizes a title to an id."""
    def isDefaultPageInFolder() -> None:
        """Returns a boolean indicating whether the current context is the
        default page of its parent folder.
        """
    def isStructuralFolder() -> None:
        """Checks if a given object is a "structural folder".

        That is, a folderish item which does not explicitly implement
        INonStructuralFolder to declare that it doesn\'t wish to be treated
        as a folder by the navtree, the tab generation etc.
        """
    def navigationRootPath() -> None:
        """Get the current navigation root path"""
    def navigationRootUrl() -> None:
        """Get the url to the current navigation root"""
    def getParentObject() -> None:
        """Returns the parent of the current object, equivalent to
        aq_inner(aq_parent(context)), or context.aq_inner.getParentNode()
        """
    def getCurrentFolder() -> None:
        """If the context is the default page of a folder or is not itself a
        folder, the parent is returned, otherwise the object itself is
        returned.  This is useful for providing a context for methods
        which wish to act on what is considered the current folder in the
        ui.
        """
    def getCurrentFolderUrl() -> None:
        """Returns the URL of the current folder as determined by
        self.getCurrentFolder(), used heavily in actions.
        """
    def getCurrentObjectUrl() -> None:
        """Returns the URL of the current object unless that object is a
        folder default page, in which case it returns the parent.
        """
    def isFolderOrFolderDefaultPage() -> None:
        """Returns true only if the current object is either a folder (as
        determined by isStructuralFolder) or the default page in context.
        """
    def isPortalOrPortalDefaultPage() -> None:
        """Returns true only if the current object is either the portal object
        or the default page of the portal.
        """
    def getViewTemplateId() -> None:
        """Returns the template Id corresponding to the default view method of
        the context object.
        """
    def showToolbar() -> None:
        """Returns true if the editable border should be shown"""
    def cropText(text, length, ellipsis) -> None:
        """Crop text on a word boundary"""
    def site_encoding() -> None:
        """returns site encoding"""
    def patterns_settings() -> None:
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
