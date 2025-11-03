from _typeshed import Incomplete

SERVICE_ID: str

class ControlpanelSummarySerializeToJson:
    controlpanel: Incomplete
    def __init__(self, controlpanel) -> None: ...
    def __call__(self): ...

def get_jsonschema_for_controlpanel(controlpanel, context, request, form=None):
    """Build a complete JSON schema for the given controlpanel."""

class ControlpanelSerializeToJson:
    controlpanel: Incomplete
    schema: Incomplete
    schema_prefix: Incomplete
    registry: Incomplete
    def __init__(self, controlpanel) -> None: ...
    def __call__(self): ...
