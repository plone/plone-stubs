from zope.interface import Interface

class IVersionPolicy(Interface):
    """A version policy object, which describes and sets up a versioning
    policy
    """
    def Title() -> None:
        """Returns a nice name for the policy"""
