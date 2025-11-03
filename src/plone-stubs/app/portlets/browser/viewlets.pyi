from _typeshed import Incomplete
from plone.app.layout.viewlets.common import ViewletBase

class ManagePortletsFallbackViewlet(ViewletBase):
    """Manage portlets fallback link that sits below content"""

    index: Incomplete
    portlet_assignable: Incomplete
    sl: Incomplete
    sr: Incomplete
    object_url: Incomplete
    def update(self) -> None: ...
    def available(self): ...

class FooterViewlet(ViewletBase):
    index: Incomplete
    year: Incomplete
    def update(self) -> None: ...
    def render_footer_portlets(self):
        """
        You might ask, why is this necessary. Well, let me tell you a story...

        plone.app.portlets, in order to provide @@manage-portlets on a context,
        overrides the IPortletRenderer for the IManageContextualPortletsView
        view.
        See plone.portlets and plone.app.portlets

        Seems fine right? Well, most of the time it is. Except, here.
        Previously, we were just using the syntax like
        `provider:plone.footerportlets` to render the footer portlets.
        Since this tal expression was inside a viewlet,
        the view is no longer IManageContextualPortletsView when
        visiting @@manage-portlets. Instead, it was IViewlet.
        See zope.contentprovider

        In to fix this short coming, we render the portlet column by
        manually doing the multi adapter lookup and then manually
        doing the rendering for the content provider.
        See zope.contentprovider
        """
