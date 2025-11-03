from _typeshed import Incomplete
from collections.abc import Generator
from Products.Five import BrowserView

class SiteMapView(BrowserView):
    """Creates the sitemap as explained in the specifications.

    http://www.sitemaps.org/protocol.php
    """

    template: Incomplete
    context: Incomplete
    request: Incomplete
    filename: str
    def __init__(self, context, request) -> None: ...
    def objects(self) -> Generator[Incomplete]:
        """Returns the data to create the sitemap."""
    def generate(self):
        """Generates the Gzipped sitemap."""
    def __call__(self):
        """Checks if the sitemap feature is enable and returns it."""
