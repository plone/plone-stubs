def safe_encode(value, encoding: str = "utf-8"):
    """Convert unicode to the specified encoding.

    copied from Products.CMFPlone.utils b/c this package does not depend on it
    """

def safe_text(value, encoding: str = "utf-8"):
    """Converts a value to text, even it is already a text string.

    copied from Products.CMFPlone.utils b/c this package does not depend on it
    """

def is_equal(val1, val2): ...
def mod_auth_tkt_digest(secret, data1, data2): ...
def createTicket(
    secret,
    userid,
    tokens=(),
    user_data: str = "",
    ip: str = "0.0.0.0",
    timestamp=None,
    encoding: str = "utf-8",
    mod_auth_tkt: bool = False,
):
    """
    By default, use a more compatible
    """

def splitTicket(ticket, encoding=None): ...
def validateTicket(
    secret,
    ticket,
    ip: str = "0.0.0.0",
    timeout: int = 0,
    now=None,
    encoding=None,
    mod_auth_tkt: bool = False,
): ...
