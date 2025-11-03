from _typeshed import Incomplete
from zope.interface import Interface

class IPortletDirective(Interface):
    """Directive which registers a new portlet type.

    The portlet should also be installed into a site using a GenericSetup
    portlets.xml file, for example.
    """

    name: Incomplete
    interface: Incomplete
    assignment: Incomplete
    view_permission: Incomplete
    edit_permission: Incomplete
    renderer: Incomplete
    addview: Incomplete
    editview: Incomplete

class IPortletRendererDirective(Interface):
    """Register a portlet renderer, i.e. a different view of a portlet"""

    portlet: Incomplete
    class_: Incomplete
    template: Incomplete
    for_: Incomplete
    layer: Incomplete
    view: Incomplete
    manager: Incomplete
