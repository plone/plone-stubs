from _typeshed import Incomplete
from plone.restapi.services import Service

class Site:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, expand: bool = False): ...
    def plone_timezone(self):
        """Returns the portal timezone"""
    def features(self):
        """Indicates which features are supported by this site.

        This can be used by a client to check for version-dependent features.
        """

class SiteGet(Service):
    def reply(self): ...
