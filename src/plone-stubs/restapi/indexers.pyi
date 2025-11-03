from _typeshed import Incomplete

class TextBlockSearchableText:
    """Searchable Text indexer for Text (DraftJS) blocks."""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, value): ...

class TableBlockSearchableText:
    """Searchable Text indexer for Table blocks."""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, value): ...

class SlateTextIndexer:
    """Searchable Text indexer for Slate blocks."""

    context: Incomplete
    request: Incomplete
    def __init__(self, context, request) -> None: ...
    def __call__(self, block): ...

def extract_text(block, obj, request):
    """Extract text information from a block.

    This function tries the following methods, until it finds a result:
        1. searchableText attribute
        2. Server side adapter
        3. Subblocks

    The decision to use the server side adapter before the subblocks traversal
    allows addon developers to choose this implementation when they want a
    more granular control of the indexing.

    :param block: Dictionary with block information.
    :param obj: Context to be used to get a IBlockSearchableText.
    :param request: Current request.
    :returns: A string with text found in the block.
    """

def get_blocks_text(obj):
    """Extract text to be used by the SearchableText index in the Catalog."""

def text_strip(text_list): ...

class BlocksSearchableTextExtender:
    context: Incomplete
    def __init__(self, context) -> None: ...
    def __call__(self): ...

def SearchableText_blocks(obj): ...
