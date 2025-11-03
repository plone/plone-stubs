from _typeshed import Incomplete
from collections.abc import Generator
from plone.restapi.services import Service

WC_LOCATION_MODE: str

class CreateWorkingCopy(Service):
    def reply(self): ...
    def containers(self) -> Generator[Incomplete]:
        """Get a list of potential containers (copied over from p.a.iterate)"""
