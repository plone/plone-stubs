from plone.autoform.view import WidgetsView

class DefaultView(WidgetsView):
    """The default view for Dexterity content. This uses a WidgetsView and
    renders all widgets in display mode.
    """
    @property
    def schema(self): ...
    @property
    def additionalSchemata(self): ...
