from zope.interface import Interface

class ICacheChooser(Interface):
    def __call__(fun_name) -> None: ...

class IXHTMLCompressor(Interface):
    def compress(string) -> None: ...
