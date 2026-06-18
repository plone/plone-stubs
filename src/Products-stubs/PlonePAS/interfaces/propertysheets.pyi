from Products.PluggableAuthService.interfaces.propertysheets import IPropertySheet

class IMutablePropertySheet(IPropertySheet):
    def canWriteProperty(self, object, id) -> None:
        """Check if a property can be modified."""
    def setProperty(self, object, id, value) -> None:
        """ """
    def setProperties(self, object, mapping) -> None:
        """ """

class ISchemaMutablePropertySheet(IMutablePropertySheet): ...
