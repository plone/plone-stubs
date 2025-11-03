from _typeshed import Incomplete

def safe_decode(s, encoding: str = "utf-8", errors: str = "strict"): ...

class WebIntelligentToHtmlConverter:
    urlRegexp: Incomplete
    emailRegexp: Incomplete
    indentRegexp: Incomplete
    orig: Incomplete
    tab_width: Incomplete
    def __init__(self, orig, tab_width: int = 4) -> None: ...
    def __call__(self): ...
    @staticmethod
    def abbreviateUrl(url, max: int = 60, ellipsis: str = "[&hellip;]"):
        """very long urls are abbreviated to allow nicer layout"""
    @classmethod
    def replaceURL(cls, match):
        """Replace hyperlinks with clickable <a> tags"""
    @staticmethod
    def replaceEmail(match):
        """Replace email strings with mailto: links"""
    def indentWhitespace(self, match):
        """Make leading whitespace on a line into &nbsp; to preserve indents"""

def convertWebIntelligentPlainTextToHtml(orig, tab_width: int = 4):
    """Converts text/x-web-intelligent to text/html"""

def convertHtmlToWebIntelligentPlainText(orig):
    """Converts text/html to text/x-web-intelligent."""
