from _typeshed import Incomplete

logger: Incomplete

def safe_native_string(value, encoding: str = "utf8"):
    """Try to convert value into a native string"""

def constructMessageFromSchema(context, schema, charset: str = "utf-8"): ...
def constructMessageFromSchemata(context, schemata, charset: str = "utf-8"): ...
def constructMessage(context, fields, charset: str = "utf-8"): ...
def initializeObjectFromSchema(
    context, schema, message, defaultCharset: str = "utf-8"
) -> None: ...
def initializeObjectFromSchemata(
    context, schemata, message, defaultCharset: str = "utf-8"
):
    """Convenience method which calls ``initializeObject()`` with all the
    fields in order, of all the given schemata (a sequence of schema
    interfaces).
    """

def initializeObject(
    context, fields, message, defaultCharset: str = "utf-8"
) -> None: ...
