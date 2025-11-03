from _typeshed import Incomplete
from OFS.PropertyManager import PropertyManager
from OFS.SimpleItem import SimpleItem

def flattenInterfaces(implemented): ...

class BasePlugin(SimpleItem, PropertyManager):
    """Base class for all PluggableAuthService Plugins"""

    zmi_icon: str
    security: Incomplete
    manage_options: Incomplete
    prefix: str
    manage_activateInterfacesForm: Incomplete
    def listInterfaces(self):
        """For ZMI update of interfaces."""
    def testImplements(self, interface):
        """Can't access Interface.providedBy() directly in ZPT."""
    def manage_activateInterfaces(self, interfaces, RESPONSE=None) -> None:
        """For ZMI update of active interfaces."""
    @security.private
    def applyTransform(self, value):
        """Transform for login name.

        Possibly transform the login, for example by making it lower
        case.

        Normally this is done in PAS itself, but in some cases a
        method in a plugin may need to do it itself, when there is no
        method in PAS that calls that method.
        """
