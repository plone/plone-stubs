from plone.restapi.serializer.dxcontent import SerializeToJson

class SerializeCollectionToJson(SerializeToJson):
    def __call__(self, version=None, include_items: bool = True): ...
