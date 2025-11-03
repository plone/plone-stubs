from plone.rfc822.defaultfields import BaseFieldMarshaler

class RelationFieldMarshaler(BaseFieldMarshaler):
    """Field marshaler for z3c.relationfield IRelation and IRelationChoice
    fields
    """

    ascii: bool
    def encode(self, value, charset: str = "utf-8", primary: bool = False): ...
    def decode(
        self,
        value,
        message=None,
        charset: str = "utf-8",
        contentType=None,
        primary: bool = False,
    ): ...
