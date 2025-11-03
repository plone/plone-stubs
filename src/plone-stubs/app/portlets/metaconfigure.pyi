def portletDirective(
    _context,
    name,
    interface,
    assignment,
    renderer,
    addview,
    view_permission: str = "zope2.View",
    edit_permission: str = "plone.app.portlets.ManageOwnPortlets",
    editview=None,
) -> None:
    """Register a portlet assignment type using typical options.

    Portlets that consist of a simple assignment class deriving form
    base.Assignment, a renderer deriving from base.Renderer, an addview
    using z3c form and deriving from base.AddForm and an editview (optional)
    using z3c form and deriving from base.EditForm, can use this directive
    to avoid having to register each of those components individually.

    In addition, we register the portlet interface using IPortletTypeInterface
    and an IFactory utility, in order to help the GenericSetup handler and
    other generic code instantiate portlets.
    """

def portletRendererDirective(
    _context,
    portlet,
    class_=None,
    template=None,
    for_=...,
    layer=...,
    view=...,
    manager=...,
) -> None:
    """Register a custom/override portlet renderer"""
