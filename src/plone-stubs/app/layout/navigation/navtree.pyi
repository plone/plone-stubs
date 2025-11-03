from _typeshed import Incomplete

class NavtreeStrategyBase:
    """Basic navigation tree strategy that does nothing."""

    __allow_access_to_unprotected_subobjects__: int
    rootPath: Incomplete
    showAllParents: bool
    supplimentQuery: Incomplete
    def nodeFilter(self, node): ...
    def subtreeFilter(self, node): ...
    def decoratorFactory(self, node): ...
    def showChildrenOf(self, object): ...

def buildFolderTree(context, obj=None, query={}, strategy=...):
    """Create a tree structure representing a navigation tree. By default,
    it will create a full "sitemap" tree, rooted at the portal, ordered
    by explicit folder order. If the \'query\' parameter contains a \'path\'
    key, this can be used to override this. To create a navtree rooted
    at the portal root, set query[\'path\'] to:

        {\'query\' : \'/\'.join(context.getPhysicalPath()),
         \'navtree\' : 1}

    to start this 1 level below the portal root, set query[\'path\'] to:

        {\'query\' : \'/\'.join(obj.getPhysicalPath()),
         \'navtree\' : 1,
         \'navtree_start\' : 1}

    to create a sitemap with depth limit 3, rooted in the portal:

        {\'query\' : \'/\'.join(obj.getPhysicalPath()),
         \'depth\' : 3}

    The parameters:

    - \'context\' is the acquisition context, from which tools will be acquired
    - \'obj\' is the current object being displayed.
    - \'query\' is a catalog query to apply to find nodes in the tree.
    - \'strategy\' is an object that can affect how the generation works. It
        should be derived from NavtreeStrategyBase, if given, and contain:

            rootPath -- a string property; the physical path to the root node.

            If not given, it will default to any path set in the query, or the
            portal root. Note that in a navtree query, the root path will
            default to the portal only, possibly adjusted for any navtree_start
            set. If rootPath points to something not returned by the query by
            the query, a dummy node containing only an empty \'children\' list
            will be returned.

            showAllParents -- a boolean property; if true and obj is given,
                ensure that all parents of the object, including any that would
                normally be filtered out are included in the tree.

            supplimentQuery -- a dictionary property; provides
                additional query terms which, if not already present
                in the query, are added.  Useful, for example, to
                affect default sorting or default page behavior.

            nodeFilter(node) -- a method returning a boolean; if this returns
                False, the given node will not be inserted in the tree

            subtreeFilter(node) -- a method returning a boolean; if this
                returns False, the given (folderish) node will not be expanded
                (its children will be pruned off)

            decoratorFactory(node) -- a method returning a dict; this can
                inject additional keys in a node being inserted.

            showChildrenOf(object) -- a method returning True if children of
                the given object (normally the root) should be returned

    Returns tree where each node is represented by a dict:

        item            -   A catalog brain of this item
        depth           -   The depth of this item, relative to the startAt
                            level
        currentItem     -   True if this is the current item
        currentParent   -   True if this is a direct parent of the current item
        children        -   A list of children nodes of this node

    Note: Any \'decoratorFactory\' specified may modify this list, but
    the \'children\' property is guaranteed to be there.

    Note: If the query does not return the root node itself, the root
    element of the tree may contain *only* the \'children\' list.

    Note: Folder default-pages are not included in the returned result.
    If the \'obj\' passed in is a default-page, its parent folder will be
    used for the purposes of selecting the \'currentItem\'.
    """
