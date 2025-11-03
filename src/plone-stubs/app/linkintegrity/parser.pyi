from _typeshed import Incomplete
from html.parser import HTMLParser

TAG_ATTRS_TO_TRACK: Incomplete

class LinkParser(HTMLParser):
    """A simple html parser for link and image urls."""

    links: Incomplete
    def __init__(self) -> None: ...
    def getLinks(self):
        """Return all links found during parsing."""
    def handle_starttag(self, tag, attrs) -> None:
        """Override the method to remember all links."""

def links_in_srcset(attrval): ...
def search_attr(name, attrs):
    """Search named attribute in a list of attributes."""

def extractLinks(data, encoding: str = "utf-8"):
    """Parse the given html and return all links."""
