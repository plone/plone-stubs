from _typeshed import Incomplete
from Acquisition import Explicit

class TreeNode(Explicit):
    __allow_access_to_unprotected_subobjects__: int
    state: int
    height: int
    size: int
    def __init__(self) -> None: ...
    def flat(self):
        """Return a flattened preorder list of tree nodes"""
    def walk(self, f, data=None) -> None:
        """Preorder walk this tree, passing each node to a function"""
    depth: Incomplete
    def __getitem__(self, index): ...
    def __len__(self) -> int: ...

class TreeMaker:
    """Class for mapping a hierarchy of objects into a tree of nodes."""

    __allow_access_to_unprotected_subobjects__: int
    def setIdAttr(self, id) -> None:
        """Set the attribute or method name called to get a unique Id.

        The id attribute or method is used to get a unique id for every
        node in the tree, so that the state of the tree can be encoded
        as a string using Tree.encodeExpansion(). The returned id should
        be unique and stable across Zope requests.

        If the attribute or method isn't found on an object, either
        the objects persistence Id or the result of id() on the object
        is used instead.
        """
    def setExpandRoot(self, expand) -> None:
        """Set wether or not to expand the root node by default.

        When no expanded flag or mapping is passed to .tree(), assume the root
        node is expanded, and leave all subnodes closed.

        The default is to expand the root node.
        """
    def setAssumeChildren(self, assume) -> None:
        """Set wether or not to assume nodes have children.

        When a node is not expanded, when assume children is set, don't
        determine if it is a leaf node, but assume it can be opened. Use this
        when determining the children for a node is expensive.

        The default is to not assume there are children.
        """
    def setChildAccess(self, attrname=..., filter=..., function=...) -> None:
        """Set the criteria for fetching child nodes.

        Child nodes can be accessed through either an attribute name
        or callback function.  Children fetched by attribute name can
        be filtered through a callback function.
        """
    def setStateFunction(self, function) -> None:
        """Set the expansion state function.

        This function will be called to determine if a node should be open or
        collapsed, or should be treated as a leaf node. The function is passed
        the current object, and the intended state for that object. It should
        return the actual state the object should be in. State is encoded as an
        integer, meaning:

            -1: Node closed. Children will not be processed.
             0: Leaf node, cannot be opened or closed, no children are
                processed.
             1: Node opened. Children will be processed as part of the tree.
        """
    def getId(self, object): ...
    def node(self, object): ...
    def hasChildren(self, object): ...
    def filterChildren(self, children): ...
    def getChildren(self, object): ...
    def tree(self, root, expanded=None, subtree: int = 0):
        """Create a tree from root, with specified nodes expanded.

        "expanded" must be false, true, or a mapping.
        Each key of the mapping is the id of a top-level expanded
        node, and each value is the "expanded" value for the
        children of that node.
        """

def simple_type(ob): ...
def b2a(s):
    """Encode a bytes/string as a cookie- and url-safe string.

    Encoded string use only alphanumeric characters, and "._-".
    """

def a2b(s):
    """Decode a b2a-encoded value to bytes."""

def encodeExpansion(nodes, compress: int = 1):
    """Encode the expanded node ids of a tree into bytes.

    Accepts a list of nodes, such as that produced by root.flat().
    Marks each expanded node with an expansion_number attribute.
    Since node ids are encoded, the resulting string is safe for
    use in cookies and URLs.
    """

def decodeExpansion(s, nth=None, maxsize: int = 8192):
    """Decode an expanded node map from bytes.

    If nth is an integer, also return the (map, key) pair for the nth entry.
    """
