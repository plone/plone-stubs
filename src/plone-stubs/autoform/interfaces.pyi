from _typeshed import Incomplete
from z3c.form.interfaces import IDisplayForm
from z3c.form.interfaces import IFieldsForm
from z3c.form.interfaces import IFieldWidget
from zope.interface import Interface

MODES_KEY: str
OMITTED_KEY: str
ORDER_KEY: str
WIDGETS_KEY: str
READ_PERMISSIONS_KEY: str
WRITE_PERMISSIONS_KEY: str
FORM_NAMESPACE: str
FORM_PREFIX: str
SECURITY_NAMESPACE: str
SECURITY_PREFIX: str

class IFormFieldProvider(Interface):
    """Marker interface for schemata that provide form fields."""

class IAutoExtensibleForm(Interface):
    """The mixin class plone.autoform.form.AutoExtensibleForm can be
    used to have z3c.form forms that build automatically based on the contents
    of various tagged values, on multiple schema interfaces, which
    should be supplied with the properties defined below. See autoform.txt
    for details.
    """

    ignorePrefix: Incomplete
    schema: Incomplete
    additionalSchemata: Incomplete

class IAutoObjectSubForm(Interface):
    """This mixin class enables a form based on z3c.form.object.ObjectSubForm
    to also have its fields updated with form hints. See subform.txt
    """

    schema: Incomplete

class IWidgetsView(IAutoExtensibleForm, IFieldsForm, IDisplayForm):
    """A display form that supports setting up widgets based on schema
    interfaces.
    """

    w: Incomplete
    fieldsets: Incomplete

class IParameterizedWidget(IFieldWidget):
    """A widget factory that can create a widget with parameters."""

class IWidgetExportImportHandler(Interface):
    """Supermodel export/import handler for widgets."""
