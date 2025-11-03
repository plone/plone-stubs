from _typeshed import Incomplete
from z3c.form import form

class ObjectSubForm(form.BaseForm):
    context: Incomplete
    request: Incomplete
    __parent__: Incomplete
    parentForm: Incomplete
    ignoreContext: Incomplete
    ignoreRequest: Incomplete
    ignoreReadonly: Incomplete
    prefix: Incomplete
    def __init__(self, context, request, parentWidget) -> None: ...
    fields: Incomplete
    def setupFields(self) -> None: ...
    mode: Incomplete
    def update(self) -> None: ...
    def getContent(self): ...

class SubformAdapter:
    """Most basic-default subform factory adapter"""

    factory = ObjectSubForm
    context: Incomplete
    request: Incomplete
    widgetContext: Incomplete
    form: Incomplete
    widget: Incomplete
    field: Incomplete
    schema: Incomplete
    def __init__(
        self, context, request, widgetContext, form, widget, field, schema
    ) -> None: ...
    def __call__(self): ...
