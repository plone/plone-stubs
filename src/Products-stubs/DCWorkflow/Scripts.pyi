from .ContainerTab import ContainerTab
from _typeshed import Incomplete

class Scripts(ContainerTab):
    """A container for workflow scripts"""

    meta_type: str
    security: Incomplete
    def manage_main(self, client=None, REQUEST=None, **kw):
        """ """
