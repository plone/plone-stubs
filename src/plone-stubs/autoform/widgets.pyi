from _typeshed import Incomplete

class ParameterizedWidget:
    """A factory for deferred construction of widgets with parameters.

    z3c.form widgets are associated with a particular request,
    so they cannot be instantiated until the form is rendered.
    But it\'s often desired to use a widget with particular attributes set.

    This class acts as a "field widget" factory. It is instantiated
    at configuration time with a widget class and some parameters.
    Then it can be assigned to a z3c.form field\'s widgetFactory attribute
    or stored in the plone.autoform widget tagged value.
    Later, it is called by z3c.form with the Zope field and request
    and returns a widget instance with the desired parameters in place.

    Typically developers will not use this class directly,
    but will use the widget schema directive, the <widget /> directive
    in model XML, or the TTW UI to configure their parameterized widget.
    Those all use ParameterizedWidget internally.
    """

    widget_factory: Incomplete
    params: Incomplete
    def __init__(self, widget_factory=None, **params) -> None: ...
    def __call__(self, field, request): ...
    def getWidgetFactoryName(self):
        """Returns the dotted path of the widget factory for serialization.

        Or None, if widget_factory is None.
        """
    def getExportImportHandler(self, field):
        """Returns an IWidgetExportImportHandler suitable for this widget."""

class WidgetExportImportHandler:
    fieldAttributes: Incomplete
    def __init__(self, widget_schema) -> None: ...
    def read(self, widgetNode, params) -> None: ...
    def write(self, widgetNode, params) -> None: ...

TextInputWidgetExportImportHandler: Incomplete
TextAreaWidgetExportImportHandler: Incomplete
