from .mixins import OrderingMixin
from _typeshed import Incomplete

class DeserializeFromJson(OrderingMixin):
    context: Incomplete
    request: Incomplete
    sm: Incomplete
    permission_cache: Incomplete
    modified: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(
        self,
        validate_all: bool = False,
        data=None,
        create: bool = False,
        mask_validation_errors: bool = True,
    ): ...
    def get_schema_data(self, data, validate_all, create: bool = False): ...
    def mark_field_as_changed(self, schema, fieldname) -> None:
        """Collect the names of the modified fields. Use prefixed name because
        z3c.form does so.
        """
    def check_permission(self, permission_name): ...
