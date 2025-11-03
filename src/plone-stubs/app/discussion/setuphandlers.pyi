from _typeshed import Incomplete

DEFAULT_TYPES: Incomplete
BEHAVIOR: str

class HiddenProfiles:
    def getNonInstallableProfiles(self): ...

def add_discussion_behavior_to_default_types(context) -> None:
    """Add the discussion behavior to all default types, if they exist."""

def remove_discussion_behavior_to_default_types(context) -> None:
    """Remove the discussion behavior from all default types, if they exist."""

def post_install(context) -> None:
    """Post install script"""

def post_uninstall(context) -> None:
    """Post uninstall script"""
