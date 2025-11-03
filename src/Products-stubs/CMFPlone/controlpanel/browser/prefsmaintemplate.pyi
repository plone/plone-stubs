from Products.Five import BrowserView

class PrefsMainTemplate(BrowserView):
    prefs_main_template_name: str
    def __call__(self): ...
    @property
    def macros(self): ...
