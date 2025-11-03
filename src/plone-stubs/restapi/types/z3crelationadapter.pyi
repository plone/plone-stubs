from plone.restapi.types.adapters import ListJsonSchemaProvider

class ChoiceslessRelationListSchemaProvider(ListJsonSchemaProvider):
    def get_items(self):
        """Get items properties."""
