from _typeshed import Incomplete

class FieldRef:
    """Default field reference."""

    recordName: Incomplete
    originalField: Incomplete
    def __init__(self, name, originalField) -> None: ...
    @property
    def __providedBy__(self): ...
    def __getattr__(self, name): ...
