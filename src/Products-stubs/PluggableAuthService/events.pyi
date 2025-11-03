from _typeshed import Incomplete

class PASEvent:
    principal: Incomplete
    object: Incomplete
    def __init__(self, principal) -> None: ...

class PrincipalAddedToGroup(PASEvent):
    group_id: Incomplete
    def __init__(self, principal, group_id) -> None: ...

class PrincipalRemovedFromGroup(PASEvent):
    group_id: Incomplete
    def __init__(self, principal, group_id) -> None: ...

class PrincipalCreated(PASEvent): ...
class PrincipalDeleted(PASEvent): ...

class GroupCreated(PASEvent):
    plugin: Incomplete
    def __init__(self, group, plugin) -> None: ...

class GroupDeleted(PASEvent): ...

class CredentialsUpdated(PASEvent):
    password: Incomplete
    def __init__(self, principal, password) -> None: ...

class PropertiesUpdated(PASEvent):
    properties: Incomplete
    def __init__(self, principal, properties) -> None: ...

def userCredentialsUpdatedHandler(principal, event) -> None: ...
def PASEventNotify(event) -> None:
    """Event subscriber to dispatch PASEvent to interested adapters."""
