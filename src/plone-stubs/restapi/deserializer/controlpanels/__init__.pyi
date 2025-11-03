from _typeshed import Incomplete

class FakeDXContext:
    """Fake DX content class, so we can reuse the DX field deserializers"""

class ControlpanelDeserializeFromJson:
    controlpanel: Incomplete
    schema: Incomplete
    schema_prefix: Incomplete
    registry: Incomplete
    context: Incomplete
    request: Incomplete
    def __init__(self, controlpanel) -> None: ...
    def __call__(self, mask_validation_errors: bool = True) -> None: ...
