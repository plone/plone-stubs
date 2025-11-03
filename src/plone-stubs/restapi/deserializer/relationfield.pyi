from plone.restapi.deserializer.dxfields import DefaultFieldDeserializer

class RelationChoiceFieldDeserializer(DefaultFieldDeserializer):
    def __call__(self, value): ...
