from _typeshed import Incomplete

logger: Incomplete

def findObject(base, path):
    """traverse to given path and find the upmost object"""

def getObjectsFromLinks(base, links):
    """Determine actual objects referred to by given links.

    return set of RelationValue
    """

def modifiedContent(obj, event) -> None:
    """Object was modified, cloned or created."""

def removedContent(obj, event) -> None: ...

modifiedArchetype = modifiedContent
modifiedDexterity = modifiedContent

def updateReferences(obj, refs) -> None:
    """Renew all linkintegritry-references.

    Search the zc.relation catalog for linkintegritry-references for this obj.
    Drop them all and set the new ones.
    TODO: Might be improved by not changing anything if the links are the same.
    """

def check_linkintegrity_dependencies(obj): ...
