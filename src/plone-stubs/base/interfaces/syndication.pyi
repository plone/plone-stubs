from _typeshed import Incomplete
from zope.interface import Interface

class ISyndicatable(Interface): ...

class IFeedData(Interface):
    def link() -> None:
        """
        Link to item
        """
    def base_url() -> None:
        """
        base url to item
        """
    def title() -> None:
        """
        title of item
        """
    def description() -> None:
        """ """
    def categories() -> None:
        """
        List of tags
        """
    def published() -> None:
        """
        publishing date
        """
    def modified() -> None:
        """
        modification date
        """
    def uid() -> None:
        """ """
    def rights() -> None:
        """ """
    def publisher() -> None:
        """ """
    def author() -> None:
        """ """
    def author_name() -> None:
        """ """
    def author_email() -> None:
        """ """

class IFeed(IFeedData):
    """
    An adapter on the context and request
    to get feed information
    """
    def show_about() -> None:
        """ """
    def logo() -> None:
        """ """
    def icon() -> None:
        """ """
    def items() -> None:
        """
        adapted items
        """
    def limit() -> None:
        """ """
    def language() -> None:
        """ """

class ISearchFeed(IFeed): ...

class IFeedItem(IFeedData):
    """
    An adapter on the feed item and IFeed instance
    """
    def body() -> None:
        """ """
    def guid() -> None:
        """ """
    def has_enclosure() -> None:
        """ """
    def file() -> None:
        """ """
    def file_url() -> None:
        """ """
    def file_length() -> None:
        """ """
    def file_type() -> None:
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
    def allowed_feed_types() -> None:
        """
        get a list of allow feed types
        """
    def context_allowed() -> None:
        """
        If syndication is allowed on the context
        """
    def context_enabled(raise404: bool = False) -> None:
        """
        If syndication is enabled on the context
        """
    def site_enabled() -> None:
        """
        If syndication is enabled on the site
        """
    def search_rss_enabled(raise404: bool = False) -> None:
        """
        If search_rss is enabled
        """
    def show_author_info() -> None:
        """
        If author information should show on feeds
        """
    def max_items() -> None:
        """
        Default max items to show on the site
        """
    def rss_url() -> None:
        """
        Default rss url. Mainly to be used for the
        rss portal_action link
        """
