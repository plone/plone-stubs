from _typeshed import Incomplete

WIN32: bool

class MissingBinary(Exception): ...

envPath: Incomplete
bin_search_path: Incomplete
cygwin: str
extensions: Incomplete

def bin_search(binary):
    """search the bin_search_path for a given binary returning its fullname or
    raises MissingBinary"""

def getShortPathName(binary): ...
def sansext(path): ...
def bodyfinder(text):
    """Return body or unchanged text if no body tags found.

    Always use html_headcheck() first.
    Accepts bytes or text. Returns text.
    """

def scrubHTMLNoRaise(html):
    """Strip illegal HTML tags from string text."""

scrubHTML = scrubHTMLNoRaise
