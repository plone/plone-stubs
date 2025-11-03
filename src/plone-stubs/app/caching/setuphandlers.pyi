class NonInstallable:
    def getNonInstallableProfiles(self): ...

def enableExplicitMode() -> None:
    """ZCML startup hook to put the ruleset registry into explicit mode.
    This means we require people to declare ruleset types before using them.
    """

def post_handler(context) -> None: ...
