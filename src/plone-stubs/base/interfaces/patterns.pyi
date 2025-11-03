from zope.interface import Interface

class IPatternsSettings(Interface):
    """Interface to register global pattern settings adapters"""
    def __call__(self) -> None:
        """
        Return a dict of pattern options
        """
