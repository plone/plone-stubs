from _typeshed import Incomplete

class BaseProfileImportEvent:
    tool: Incomplete
    profile_id: Incomplete
    steps: Incomplete
    full_import: Incomplete
    def __init__(self, tool, profile_id, steps, full_import) -> None: ...

class BeforeProfileImportEvent(BaseProfileImportEvent): ...
class ProfileImportedEvent(BaseProfileImportEvent): ...

def handleProfileImportedEvent(event) -> None:
    """Update 'last version for profile' after a full import."""
