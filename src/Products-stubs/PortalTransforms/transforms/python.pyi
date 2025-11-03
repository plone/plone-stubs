from _typeshed import Incomplete

class Parser:
    """Send colored python source."""

    raw: Incomplete
    out: Incomplete
    tags: Incomplete
    def __init__(self, raw, tags) -> None:
        """Store the source text."""
    lines: Incomplete
    pos: int
    def __call__(self):
        """Parse and send the colored source."""
    def format_tokenizer(self, toktype, toktext, sx, ex, line) -> None:
        """Token handler."""

class PythonTransform:
    """Colorize Python source files"""

    inputs: Incomplete
    output: str
    config: Incomplete
    def name(self): ...
    def convert(self, orig, data, **kwargs): ...

def register(): ...
