from _typeshed import Incomplete
from Products.Five import BrowserView

class RegistryExporterView(BrowserView):
    """this view make sane exports of the registry.

    Main goal is to export in a way, that the output can be reused as
    best practive settings
    """

    template: Incomplete
    def __call__(self): ...
    def interfaces(self): ...
    def prefixes(self): ...
    def export(self, sinterface=None, sname=None): ...
