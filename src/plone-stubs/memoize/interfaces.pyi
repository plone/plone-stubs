from zope.interface import Interface

class ICacheChooser(Interface):
    def __call__(self, fun_name) -> None: ...

class IXHTMLCompressor(Interface):
    def compress(self, string) -> None: ...
