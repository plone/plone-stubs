from _typeshed import Incomplete
from ZTUtils.Batch import Batch
from ZTUtils.Lazy import Lazy
from ZTUtils.SimpleTree import SimpleTreeMaker
from ZTUtils.Tree import TreeMaker

class LazyFilter(Lazy):
    def __init__(self, seq, test=None, skip=None) -> None: ...
    def __getitem__(self, index): ...

class TreeSkipMixin:
    """Mixin class to make trees test security, and allow
    skipping of unauthorized objects."""

    skip: Incomplete
    def setSkip(self, skip): ...
    def getChildren(self, object): ...
    def filterChildren(self, children): ...

class TreeMaker(TreeSkipMixin, TreeMaker): ...

class SimpleTreeMaker(TreeSkipMixin, SimpleTreeMaker):
    def cookieTree(self, root_object, default_state=None):
        """Make a tree with state stored in a cookie."""

class Batch(Batch):
    def __init__(
        self,
        sequence,
        size,
        start: int = 0,
        end: int = 0,
        orphan: int = 0,
        overlap: int = 0,
        skip_unauthorized=None,
    ) -> None: ...

def make_query(*args, **kwargs):
    """Construct a URL query string, with marshalling markup.

    If there are positional arguments, they must be dictionaries.
    They are combined with the dictionary of keyword arguments to form
    a dictionary of query names and values.

    Query names (the keys) must be strings.  Values may be strings,
    integers, floats, or DateTimes, and they may also be lists or
    namespaces containing these types.  Names and string values
    should not be URL-quoted.  All arguments are marshalled with
    complex_marshal().
    """

def make_hidden_input(*args, **kwargs):
    """Construct a set of hidden input elements, with marshalling markup.

    If there are positional arguments, they must be dictionaries.
    They are combined with the dictionary of keyword arguments to form
    a dictionary of query names and values.

    Query names (the keys) must be strings.  Values may be strings,
    integers, floats, or DateTimes, and they may also be lists or
    namespaces containing these types.  All arguments are marshalled with
    complex_marshal().
    """

def complex_marshal(pairs):
    """Add request marshalling information to a list of name-value pairs.

    Names must be strings.  Values may be strings,
    integers, floats, or DateTimes, and they may also be lists or
    namespaces containing these types.

    The list is edited in place so that each (name, value) pair
    becomes a (name, marshal, value) triple.  The middle value is the
    request marshalling string.  Integer, float, and DateTime values
    will have ":int", ":float", or ":date" as their marshal string.
    Lists will be flattened, and the elements given ":list" in
    addition to their simple marshal string.  Dictionaries will be
    flattened and marshalled using ":record".
    """

def simple_marshal(v): ...
def url_query(request, req_name: str = "URL", omit=None):
    """Construct a URL with a query string, using the current request.

    request: the request object
    req_name: the name, such as "URL1" or "BASEPATH1", to get from request
    omit: sequence of name of query arguments to omit.  If a name
    contains a colon, it is treated literally.  Otherwise, it will
    match each argument name that starts with the name and a period or colon.
    """
