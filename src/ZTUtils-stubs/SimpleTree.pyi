from .Tree import TreeMaker
from .Tree import TreeNode
from _typeshed import Incomplete

class SimpleTreeNode(TreeNode):
    def branch(self): ...

class SimpleTreeMaker(TreeMaker):
    """Generate Simple Trees"""

    tree_pre: Incomplete
    def __init__(self, tree_pre: str = "tree") -> None: ...
    def node(self, object): ...
    def tree(self, root, expanded=None, subtree: int = 0): ...
