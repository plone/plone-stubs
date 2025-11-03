from plone.memoize.view import memoize
from Products.Five.browser import BrowserView

def resolveInterface(dotted_name): ...
def getDottedName(iface): ...
def visitBaseInterfaces(iface, lst) -> None: ...

class InterfaceInformation(BrowserView):
    @memoize
    def provides(self, dotted_name): ...
    @memoize
    def class_provides(self, dotted_name): ...
    @memoize
    def names_and_descriptions(self, dotted_name, all: int = 0):
        """Returns a list of pairs (name, description) for a given
        interface"""
    @memoize
    def get_interfaces(self):
        """Returns the list of interfaces which are implemented by the object"""
    def get_base_interface(self):
        """Returns all base interfaces of an object but no direct interfaces

        Base interfaces are the interfaces which are the super interfaces of
        the direct interfaces
        """
    def get_interface_informations(self, iface):
        """Gets all useful information from an iface

        * name
        * dotted name
        * trimmed doc string
        * base interfaces
        * methods with signature and trimmed doc string
        * attributes with trimemd doc string
        """
