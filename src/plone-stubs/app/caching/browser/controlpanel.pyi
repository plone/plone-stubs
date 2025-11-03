from _typeshed import Incomplete
from plone.memoize.instance import memoize

class BaseView:
    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self): ...
    errors: Incomplete
    registry: Incomplete
    settings: Incomplete
    ploneSettings: Incomplete
    purgingSettings: Incomplete
    ramCache: Incomplete
    def update(self): ...
    def render(self): ...
    @property
    @memoize
    def purgingEnabled(self): ...

class ControlPanel(BaseView):
    """Control panel view"""

    editGlobal: bool
    editRuleset: bool
    editOperationName: Incomplete
    editRulesetName: Incomplete
    def publishTraverse(self, request, name):
        """Allow the following types of URLs:

        /
            Render the standard control panel (no publish traverse invoked)

        /edit-operation-global/${operation-name}
            Render an edit form for global operation parameters

        /edit-operation-ruleset/${operation-name}/${ruleset-name}
            Render an edit form for per-ruleset operation parameters
        """
    def update(self) -> None: ...
    def processSave(self) -> None: ...
    @property
    @memoize
    def ruleTypes(self): ...
    @property
    def operationMapping(self): ...
    @property
    def templateMapping(self): ...
    @property
    def contentTypeMapping(self): ...
    @property
    @memoize
    def operationTypesLookup(self): ...
    @property
    @memoize
    def contentTypesLookup(self): ...
    @property
    @memoize
    def operationTypes(self): ...
    @property
    @memoize
    def contentTypes(self): ...
    @property
    @memoize
    def reverseContentTypeMapping(self): ...
    @property
    @memoize
    def reverseTemplateMapping(self): ...
    def hasGlobalOptions(self, operationType): ...
    def hasRulesetOptions(self, operationType, ruleset): ...

class Import(BaseView):
    """The import control panel"""
    def update(self) -> None: ...
    def processImport(self) -> None: ...
    @property
    @memoize
    def profiles(self): ...

class Purge(BaseView):
    """The purge control panel"""

    purgeLog: Incomplete
    def update(self) -> None: ...
    def processPurge(self) -> None: ...

class RAMCache(BaseView):
    """The RAM cache control panel"""
    def update(self) -> None: ...
    def processPurge(self) -> None: ...
