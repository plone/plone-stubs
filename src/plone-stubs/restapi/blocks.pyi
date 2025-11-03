from _typeshed import Incomplete
from collections.abc import Generator

def visit_blocks(context, blocks) -> Generator[Incomplete, Incomplete]:
    """Generator yielding all blocks, including nested blocks.

    context: Content item where these blocks are stored.
    blocks: A dict mapping block ids to a dict of block data.
    """

def visit_subblocks(context, block) -> Generator[Incomplete, Incomplete]:
    """Generator yielding the immediate subblocks of a block.

    context: Context item where this block is stored
    block: A dict of block data
    """

def iter_block_transform_handlers(
    context, block_value, interface
) -> Generator[Incomplete, None, Incomplete]:
    """Find valid handlers for a particular block transformation.

    Looks for adapters of the context and request to this interface.
    Then skips any that are disabled or don't match the block type,
    and returns the remaining handlers sorted by `order`.
    """

class NestedBlocksVisitor:
    """Visit nested blocks."""
    def __init__(self, context, request) -> None: ...
    def __call__(self, block_value) -> Generator[Incomplete, Incomplete]:
        """Visit nested blocks in ["data"]["blocks"] or ["blocks"]"""
