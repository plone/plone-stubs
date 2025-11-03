from Products.Five import BrowserView

class CatalogNavigationTabs(BrowserView):
    def topLevelTabs(self, actions=None, category: str = "portal_tabs"): ...
    def customize_entry(self, entry, brain=None) -> None:
        """a little helper to enlarge customizability."""
