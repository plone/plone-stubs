from zope.interface import Interface

class INameFromFileName(Interface):
    """Marker interface to enable name from filename behavior"""

class NameFromFileName:
    def __new__(cls, context): ...
    def __init__(self, context) -> None: ...
