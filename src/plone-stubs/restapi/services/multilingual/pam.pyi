from _typeshed import Incomplete
from plone.restapi.services import Service

class Translations:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, expand: bool = False): ...

class TranslationInfo(Service):
    """Get translation information"""
    def reply(self): ...

class LinkTranslations(Service):
    """Link two content objects as translations of each other"""

    portal: Incomplete
    portal_url: Incomplete
    catalog: Incomplete
    def __init__(self, context, request) -> None: ...
    def reply(self): ...
    def get_object(self, key): ...

class UnlinkTranslations(Service):
    """Unlink the translations for a content object"""
    def reply(self): ...
