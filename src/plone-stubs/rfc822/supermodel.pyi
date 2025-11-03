HAVE_SUPERMODEL: bool

class PrimaryFieldMetadataHandler:
    """Define the ``marshal`` namespace.

    This lets you write marshal:primary="true" on a field to mark it as
    a primary field.
    """

    namespace: str
    prefix: str
    def read(self, fieldNode, schema, field) -> None: ...
    def write(self, fieldNode, schema, field) -> None: ...
