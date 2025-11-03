from _typeshed import Incomplete

class RegistryConfigletPanel:
    configlet: Incomplete
    configlet_id: Incomplete
    configlet_category_id: Incomplete
    schema: Incomplete
    schema_prefix: str
    context: Incomplete
    request: Incomplete
    portal_cp: Incomplete
    title: Incomplete
    group: Incomplete
    def __init__(self, context, request) -> None: ...
    def add(self, names) -> None: ...
    def get(self, names) -> None: ...
    def update(self, names) -> None: ...
    def delete(self, names) -> None: ...
