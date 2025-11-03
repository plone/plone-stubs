from _typeshed import Incomplete
from plone.restapi.services import Service

class UserSchemaGet(Service):
    params: Incomplete
    def __init__(self, context, request) -> None: ...
    def publishTraverse(self, request, name): ...
    def build_userschema_as_jsonschema(self, user_schema):
        """function to build a jsonschema from user schema information"""
    def reply(self): ...
