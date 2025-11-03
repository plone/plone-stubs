def serializeSchemaContext(schema_context, event=None) -> None:
    """Serializes the schema associated with a schema context.

    The serialized schema is saved to the model_source property of the FTI
    associated with the schema context.
    """

def serializeSchema(schema) -> None:
    """Finds the FTI and model associated with a schema, and synchronizes
    the schema to the FTI model_source attribute.

    This method only works for schemas that were created from an FTI's
    model_source property

    BBB - deprecated
    """
