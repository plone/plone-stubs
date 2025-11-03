from _typeshed import Incomplete

PRODUCTION_RESOURCE_DIRECTORY: str
logger: Incomplete

def get_production_resource_directory(): ...
def get_resource(context, path): ...
def get_override_directory(context): ...
def evaluateExpression(expression, context):
    """Evaluate an object's TALES condition to see if it should be
    displayed."""
