class LanguageIndependentFieldMetadataHandler:
    """Define the ``lingua`` namespace.

    This lets you write lingua:independent="true" on a field to mark it as
    a language independent field.
    """

    namespace: str
    prefix: str
    def read(self, fieldNode, schema, field) -> None: ...
    def write(self, fieldNode, schema, field) -> None: ...
