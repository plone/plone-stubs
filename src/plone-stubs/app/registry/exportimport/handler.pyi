from _typeshed import Incomplete

def evaluateCondition(expression):
    """Evaluate import condition.

    ``expression`` is a string of the form "verb arguments".

    Currently the supported verbs are \'have\', \'not-have\',
    \'installed\' and \'not-installed\'.

    The \'have\' verb takes one argument: the name of a feature.
    """

def shouldPurgeList(value_node, key): ...
def importRegistry(context) -> None: ...
def exportRegistry(context) -> None: ...

class RegistryImporter:
    """Helper classt to import a registry file"""

    LOGGER_ID: str
    context: Incomplete
    environ: Incomplete
    logger: Incomplete
    def __init__(self, context, environ) -> None: ...
    def importDocument(self, document) -> None: ...
    def importRecord(self, node) -> None: ...
    def importRecords(self, node) -> None: ...

class RegistryExporter:
    LOGGER_ID: str
    context: Incomplete
    environ: Incomplete
    logger: Incomplete
    def __init__(self, context, environ) -> None: ...
    def exportDocument(self): ...
    def exportRecord(self, record): ...
