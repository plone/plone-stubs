from _typeshed import Incomplete
from plone.app.event.base import AnnotationAdapter
from plone.z3cform.layout import FormWrapper
from Products.Five.browser import BrowserView
from z3c.form import form
from zope.interface import Interface

def ical_import(container, ics_resource, event_type, sync_strategy=...): ...
def no_file_protocol_url(value):
    """Validator for ical_url: we do not want file:// urls.

    This opens up security issues.
    """

class IIcalendarImportSettings(Interface):
    event_type: Incomplete
    ical_url: Incomplete
    ical_file: Incomplete
    sync_strategy: Incomplete

class IcalendarImportSettings(AnnotationAdapter):
    """Annotation Adapter for IIcalendarImportSettings."""

    ANNOTATION_KEY: str

class IcalendarImportSettingsForm(form.Form):
    fields: Incomplete
    ignoreContext: bool
    def getContent(self): ...
    def save_data(self, data) -> None: ...
    def handleSave(self, action): ...
    def handleSaveImport(self, action): ...
    def handleCancel(self, action) -> None: ...

class IcalendarImportTool(BrowserView):
    @property
    def available(self): ...
    @property
    def available_disabled(self): ...
    @property
    def enabled(self): ...

class IcalendarImportSettingsFormView(FormWrapper):
    form = IcalendarImportSettingsForm
    def enable(self) -> None:
        """Enable icalendar import on this context."""
    def disable(self) -> None:
        """Disable icalendar import on this context."""
