from Products.Five.browser import BrowserView

class ContentRulesInfo(BrowserView):
    def show_rules_tab(self):
        """Whether or not the rules tab should be shown"""
