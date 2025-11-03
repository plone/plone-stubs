from Products.Five import BrowserView

class PortletUtilities(BrowserView):
    def render_portlet(self, portlethash, **kw): ...
