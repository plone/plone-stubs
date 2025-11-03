from Products.Five import BrowserView

class PhysicalNavigationBreadcrumbs(BrowserView):
    def breadcrumbs(self): ...
