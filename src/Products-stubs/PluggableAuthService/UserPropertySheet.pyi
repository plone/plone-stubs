from _typeshed import Incomplete

StringTypes: Incomplete

class UserPropertySheet:
    """Model a single, read-only set of properties about a user.

    o Values for the sheet are passed as keyword args to the c'tor.

    o The schema for the sheet may be passed into the c'tor explicitly
      as a sequence of (id, type) tuples;  if not passed, the c'tor will
      guess the schema from the keyword args.
    """
    def __init__(self, id, schema=None, **kw) -> None: ...
    def getId(self):
        """See IPropertySheet."""
    def hasProperty(self, id):
        """See IPropertySheet."""
    def getProperty(self, id, default=None):
        """See IPropertySheet."""
    def getPropertyType(self, id):
        """See IPropertySheet."""
    def propertyInfo(self, id):
        """See IPropertySheet."""
    def propertyMap(self):
        """See IPropertySheet."""
    def propertyIds(self):
        """See IPropertySheet."""
    def propertyValues(self):
        """See IPropertySheet."""
    def propertyItems(self):
        """See IPropertySheet."""
