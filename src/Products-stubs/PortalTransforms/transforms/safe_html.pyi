from _typeshed import Incomplete

CSS_COMMENT: Incomplete

def hasScript(s):
    """Dig out evil Java/VB script inside an HTML attribute.
    >>> hasScript(
    ...     'data:text/html;'
    ...     'base64,PHNjcmlwdD5hbGVydCgidGVzdCIpOzwvc2NyaXB0Pg==')
    True
    >>> hasScript('script:evil(1);')
    True
    >>> hasScript('expression:evil(1);')
    True
    >>> hasScript('expression/**/:evil(1);')
    True
    >>> hasScript('http://foo.com/ExpressionOfInterest.doc')
    False
    """

def unescape_chr(matchobj): ...
def decode_charref(s): ...
def decode_entityref(s): ...

CHR_RE: Incomplete
CHARREF_RE: Incomplete
ENTITYREF_RE: Incomplete

def decode_htmlentities(s): ...

class SafeHTML:
    """Simple transform which uses lxml to
    clean potentially bad tags.

    We only want security related filtering here, all the rest has to be done
    in TinyMCE & co.

    Tags must explicit be allowed in valid_tags to pass. Only
    the tags themself are removed, not their contents. If tags
    are removed and in nasty_tags, they are removed with
    all of their contents.

    Settings are in plone.registry.

    Objects will not be transformed again with changed settings.
    You need to clear the cache by e.g.
    1.) restarting your zope or
    2.) empty the zodb-cache via ZMI -> Control_Panel
        -> Database Management -> main || other_used_database
        -> Flush Cache.
    """

    inputs: Incomplete
    output: str
    config: Incomplete
    config_metadata: Incomplete
    def __init__(self, name=None, **kwargs) -> None: ...
    def name(self): ...
    def __getattr__(self, attr): ...
    settings: Incomplete
    def convert(self, orig, data, **kwargs): ...
    def cleaner_options(self): ...
    def scrub_html(self, orig): ...

def register(): ...
