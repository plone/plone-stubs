from Products.Five import BrowserView

class MainTemplate(BrowserView):
    ajax_template_name: str
    main_template_name: str
    def __call__(self): ...
    @property
    def template_name(self): ...
    @property
    def macros(self): ...
