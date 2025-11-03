from plone.restapi.serializer.dxfields import DefaultFieldSerializer

def relationvalue_converter(value): ...

class RelationChoiceFieldSerializer(DefaultFieldSerializer): ...

class RelationListFieldSerializer(DefaultFieldSerializer):
    def get_value(self, default=None):
        """Return field value reduced to list of non-broken Relationvalues.

        Args:
            default (list, optional): Default field value. Defaults to empty list.

        Returns:
            list: List of RelationValues
        """
