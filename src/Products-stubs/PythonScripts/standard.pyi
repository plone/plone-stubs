from _typeshed import Incomplete
from App.special_dtml import HTML
from DocumentTemplate.DT_Var import dollars_and_cents as dollars_and_cents
from DocumentTemplate.DT_Var import html_quote as html_quote
from DocumentTemplate.DT_Var import newline_to_br as newline_to_br
from DocumentTemplate.DT_Var import restructured_text as restructured_text
from DocumentTemplate.DT_Var import special_formats as special_formats
from DocumentTemplate.DT_Var import sql_quote as sql_quote
from DocumentTemplate.DT_Var import structured_text as structured_text
from DocumentTemplate.DT_Var import thousands_commas as thousands_commas
from DocumentTemplate.DT_Var import url_quote as url_quote
from DocumentTemplate.DT_Var import url_quote_plus as url_quote_plus
from DocumentTemplate.DT_Var import url_unquote as url_unquote
from DocumentTemplate.DT_Var import url_unquote_plus as url_unquote_plus
from DocumentTemplate.DT_Var import whole_dollars as whole_dollars
from DocumentTemplate.security import RestrictedDTML
from urllib.parse import urlencode as urlencode
from ZPublisher.HTTPRequest import record

security: Incomplete

class DTML(RestrictedDTML, HTML):
    """DTML objects are DocumentTemplate.HTML objects that allow
    dynamic, temporary creation of restricted DTML."""
    def __call__(self, client=None, REQUEST={}, RESPONSE=None, **kw):
        """Render the DTML given a client object, REQUEST mapping,
        Response, and key word arguments."""

class _Object(record):
    def __init__(self, **kw) -> None: ...
    def __setitem__(self, key, value) -> None: ...
    def update(self, d) -> None: ...
    def __hash__(self): ...

def Object(**kw): ...
