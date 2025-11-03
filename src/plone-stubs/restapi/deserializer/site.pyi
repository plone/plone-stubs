from _typeshed import Incomplete
from plone.restapi.deserializer.dxcontent import DeserializeFromJson

HAS_PLONE_6: Incomplete

class DeserializeSiteRootFromJson(DeserializeFromJson):
    """JSON deserializer for the Plone site root"""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, validate_all: bool = False): ...
