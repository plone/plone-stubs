from _typeshed import Incomplete
from Products.Five import BrowserView

class ImportStepsView(BrowserView):
    global_registry: Incomplete
    tool_registry: Incomplete
    def __init__(self, context, request) -> None: ...
    def invalidSteps(self): ...
    def doubleSteps(self): ...

class ExportStepsView(ImportStepsView):
    global_registry: Incomplete
    tool_registry: Incomplete
    def __init__(self, context, request) -> None: ...
