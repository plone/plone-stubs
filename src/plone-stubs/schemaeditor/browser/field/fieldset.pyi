from Products.Five import BrowserView

class ChangeFieldsetView(BrowserView):
    def change(self, fieldset_index) -> None:
        """AJAX method to change the fieldset of a field"""
