from _typeshed import Incomplete
from zope.interface import Interface

class INavigationQueryBuilder(Interface):
    """An object which returns a catalog query when called, used to
    construct a navigation tree.
    """
    def __call__() -> None:
        """Returns a mapping describing a catalog query used to build a
        navigation structure.
        """

class INavtreeStrategy(Interface):
    """An object that is used by buildFolderTree() to determine how to
    construct a navigation tree.
    """

    rootPath: Incomplete
    showAllParents: Incomplete
    def nodeFilter(node) -> None:
        """Return True or False to determine whether to include the given node
        in the tree. Nodes are dicts with at least one key - 'item', the
        catalog brain of the object the node represents.
        """
    def subtreeFilter(node) -> None:
        """Return True or False to determine whether to expand the given
        (folderish) node
        """
    def decoratorFactory(node) -> None:
        """Inject any additional keys in the node that are needed and return
        the new node.
        """
    def showChildrenOf(object) -> None:
        """Given an object (usually the root of the site), determine whether
        children should be shown or not. Even if this returns True, if
        showAllParents is True, the path to the current item may be shown.
        """
