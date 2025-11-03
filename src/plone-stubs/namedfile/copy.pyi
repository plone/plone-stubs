from _typeshed import Incomplete

class BlobFileCopyHook:
    """A copy hook that fixes the blob after copying"""

    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self, toplevel, register) -> None: ...
