from _typeshed import Incomplete
from OFS.SimpleItem import SimpleItem

class MajorMinorPredicate(SimpleItem):
    """
    Predicate matching on 'major/minor' content types.
    Empty major or minor implies wildcard (all match).
    """

    major: Incomplete
    minor: Incomplete
    PREDICATE_TYPE: str
    security: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    def getMajorType(self):
        """Get major content types."""
    def getMinorType(self):
        """Get minor content types."""
    def edit(self, major, minor, COMMA_SPLIT=...) -> None: ...
    def __call__(self, name, typ, body):
        """
        Return true if the rule matches, else false.
        """
    def getTypeLabel(self):
        """
        Return a human-readable label for the predicate type.
        """
    predicateWidget: Incomplete

class ExtensionPredicate(SimpleItem):
    """
    Predicate matching on filename extensions.
    """

    extensions: Incomplete
    PREDICATE_TYPE: str
    security: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    def getExtensions(self):
        """Get filename extensions."""
    def edit(self, extensions, COMMA_SPLIT=...) -> None: ...
    def __call__(self, name, typ, body):
        """
        Return true if the rule matches, else false.
        """
    def getTypeLabel(self):
        """
        Return a human-readable label for the predicate type.
        """
    predicateWidget: Incomplete

class MimeTypeRegexPredicate(SimpleItem):
    """
    Predicate matching only on 'typ', using regex matching for
    string patterns (other objects conforming to 'match' can
    also be passed).
    """

    pattern: Incomplete
    PREDICATE_TYPE: str
    security: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    def getPatternStr(self): ...
    def edit(self, pattern) -> None: ...
    def __call__(self, name, typ, body):
        """
        Return true if the rule matches, else false.
        """
    def getTypeLabel(self):
        """
        Return a human-readable label for the predicate type.
        """
    predicateWidget: Incomplete

class NameRegexPredicate(SimpleItem):
    """
    Predicate matching only on 'name', using regex matching
    for string patterns (other objects conforming to 'match'
    and 'pattern' can also be passed).
    """

    pattern: Incomplete
    PREDICATE_TYPE: str
    security: Incomplete
    id: Incomplete
    def __init__(self, id) -> None: ...
    def getPatternStr(self):
        """
        Return a string representation of our pattern.
        """
    def edit(self, pattern) -> None: ...
    def __call__(self, name, typ, body):
        """
        Return true if the rule matches, else false.
        """
    def getTypeLabel(self):
        """
        Return a human-readable label for the predicate type.
        """
    predicateWidget: Incomplete

def registerPredicateType(typeID, klass) -> None:
    """
    Add a new predicate type.
    """

class ContentTypeRegistry(SimpleItem):
    """
    Registry for rules which map PUT args to a CMF Type Object.
    """

    meta_type: str
    id: str
    zmi_icon: str
    zmi_show_add_dialog: bool
    manage_options: Incomplete
    security: Incomplete
    predicate_ids: Incomplete
    predicates: Incomplete
    def __init__(self) -> None: ...
    @security.public
    def listPredicateTypes(self):
        """ """
    manage_predicates: Incomplete
    def doAddPredicate(self, predicate_id, predicate_type, REQUEST) -> None:
        """ """
    def doUpdatePredicate(
        self, predicate_id, predicate, typeObjectName, REQUEST
    ) -> None:
        """ """
    def doMovePredicateUp(self, predicate_id, REQUEST) -> None:
        """ """
    def doMovePredicateDown(self, predicate_id, REQUEST) -> None:
        """ """
    def doRemovePredicate(self, predicate_id, REQUEST) -> None:
        """ """
    manage_testRegistry: Incomplete
    def doTestRegistry(self, name, content_type, body, REQUEST) -> None:
        """ """
    @security.public
    def getPredicate(self, predicate_id):
        """
        Find the predicate whose id is 'id';  return the predicate
        object, if found, or else None.
        """
    @security.public
    def listPredicates(self):
        """List '(id, (predicate, typeObjectName))' tuples for all predicates."""
    @security.public
    def getTypeObjectName(self, predicate_id):
        """
        Find the predicate whose id is 'id';  return the name of
        the type object, if found, or else None.
        """
    def addPredicate(self, predicate_id, predicate_type) -> None:
        """
        Add a predicate to this element of type 'typ' to the registry.
        """
    def updatePredicate(self, predicate_id, predicate, typeObjectName) -> None:
        """
        Update a predicate in this element.
        """
    def removePredicate(self, predicate_id) -> None:
        """
        Remove a predicate from the registry.
        """
    def reorderPredicate(self, predicate_id, newIndex) -> None:
        """
        Move a given predicate to a new location in the list.
        """
    def assignTypeName(self, predicate_id, typeObjectName) -> None:
        """
        Bind the given predicate to a particular type object.
        """
    def findTypeName(self, name, typ, body):
        """
        Perform a lookup over a collection of rules, returning the
        the name of the Type object corresponding to name/typ/body.
        Return None if no match found.
        """

def manage_addRegistry(self, REQUEST=None) -> None:
    """
    Add a CTR to self.
    """
