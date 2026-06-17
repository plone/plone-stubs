from _typeshed import Incomplete
from zope.interface import Interface

class ISyndicatable(Interface): ...

class IFeedData(Interface):
    def link(self) -> None:
        """
        Link to item
        """
    def base_url(self) -> None:
        """
        base url to item
        """
    def title(self) -> None:
        """
        title of item
        """
    def description(self) -> None:
        """ """
    def categories(self) -> None:
        """
        List of tags
        """
    def published(self) -> None:
        """
        publishing date
        """
    def modified(self) -> None:
        """
        modification date
        """
    def uid(self) -> None:
        """ """
    def rights(self) -> None:
        """ """
    def publisher(self) -> None:
        """ """
    def author(self) -> None:
        """ """
    def author_name(self) -> None:
        """ """
    def author_email(self) -> None:
        """ """

class IFeed(IFeedData):
    """
    An adapter on the context and request
    to get feed information
    """
    def show_about(self) -> None:
        """ """
    def logo(self) -> None:
        """ """
    def icon(self) -> None:
        """ """
    def items(self) -> None:
        """
        adapted items
        """
    def limit(self) -> None:
        """ """
    def language(self) -> None:
        """ """

class ISearchFeed(IFeed): ...

class IFeedItem(IFeedData):
    """
    An adapter on the feed item and IFeed instance
    """
    def body(self) -> None:
        """ """
    def guid(self) -> None:
        """ """
    def has_enclosure(self) -> None:
        """ """
    def file(self) -> None:
        """ """
    def file_url(self) -> None:
        """ """
    def file_length(self) -> None:
        """ """
    def file_type(self) -> None:
        """ """

class ISiteSyndicationSettings(Interface):
    allowed: Incomplete
    default_enabled: Incomplete
    search_rss_enabled: Incomplete
    show_author_info: Incomplete
    render_body: Incomplete
    max_items: Incomplete
    allowed_feed_types: Incomplete
    site_rss_items: Incomplete
    show_syndication_button: Incomplete
    show_syndication_link: Incomplete

class IFeedSettings(Interface):
    enabled: Incomplete
    feed_types: Incomplete
    render_body: Incomplete
    max_items: Incomplete

class ISyndicationUtil(Interface):
    def allowed_feed_types(self) -> None:
        """
        get a list of allow feed types
        """
    def context_allowed(self) -> None:
        """
        If syndication is allowed on the context
        """
    def context_enabled(self, raise404: bool = False) -> None:
        """
        If syndication is enabled on the context
        """
    def site_enabled(self) -> None:
        """
        If syndication is enabled on the site
        """
    def search_rss_enabled(self, raise404: bool = False) -> None:
        """
        If search_rss is enabled
        """
    def show_author_info(self) -> None:
        """
        If author information should show on feeds
        """
    def max_items(self) -> None:
        """
        Default max items to show on the site
        """
    def rss_url(self) -> None:
        """
        Default rss url. Mainly to be used for the
        rss portal_action link
        """
