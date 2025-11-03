from Products.PluggableAuthService.interfaces.propertysheets import IPropertySheet

class IMutablePropertySheet(IPropertySheet):
    def canWriteProperty(object, id) -> None:
        """Check if a property can be modified."""
    def setProperty(object, id, value) -> None:
        """ """
    def setProperties(object, mapping) -> None:
        """ """

class ISchemaMutablePropertySheet(IMutablePropertySheet): ...
