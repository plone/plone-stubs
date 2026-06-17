from zope.interface import Interface

class IPropertySheet(Interface):
    """Interface for queryable property sheets.

    o Objects implementing this interface can play in read-only fashion
      in OFS.PropertySheets' framework.
    """
    def getId(self) -> None:
        """Identify the sheet within a collection."""
    def hasProperty(self, id) -> None:
        """Does the sheet have a property corresponding to 'id'?"""
    def getProperty(self, id, default=None) -> None:
        """Return the value of the property corresponding to 'id'.

        o If no such property exists within the sheet, return 'default'.
        """
    def getPropertyType(self, id) -> None:
        """Return the string identifying the type of property, 'id'.

        o If no such property exists within the sheet, return None.
        """
    def propertyInfo(self, id) -> None:
        """Return a mapping describing property, 'id'.

        o Keys must include:

          'id'  -- the unique identifier of the property.

          'type' -- the string identifying the property type.

          'meta' -- a mapping containing additional info about the property.
        """
    def propertyMap(self) -> None:
        """Return a tuple of 'propertyInfo' mappings, one per property."""
    def propertyIds(self) -> None:
        """Return a sequence of the IDs of the sheet's properties."""
    def propertyValues(self) -> None:
        """Return a sequence of the values of the sheet's properties."""
    def propertyItems(self) -> None:
        """Return a sequence of (id, value) tuples, one per property."""
