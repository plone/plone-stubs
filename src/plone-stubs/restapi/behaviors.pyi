from _typeshed import Incomplete
from plone.app.dexterity.textindexer.behavior import IDexterityTextIndexer
from plone.supermodel import model
from zope.interface import Interface

IDexterityTextIndexer = Interface
BLOCKS_SCHEMA: Incomplete
LAYOUT_SCHEMA: Incomplete

class IBlocks(model.Schema, IDexterityTextIndexer):
    blocks: Incomplete
    blocks_layout: Incomplete

class IBlocksEditableLayout(IBlocks):
    """Volto Blocks Editable Layout marker interface"""
