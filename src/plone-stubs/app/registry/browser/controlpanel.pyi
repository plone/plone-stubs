from _typeshed import Incomplete
from plone.autoform.form import AutoExtensibleForm
from plone.z3cform import layout
from z3c.form import form

_: Incomplete

class RegistryEditForm(AutoExtensibleForm, form.EditForm):
    """Edit a records proxy based on an interface.

    To use this, you should use the <records /> element in a registry.xml
    GS import step to register records for a particular interface. Then
    subclass this form and set the 'schema' class variable to point to
    the same interface. You can use plone.autoform form hints to affect the
    rendering of the form, or override the update() method as appropriate.

    To get the standard control panel layout, use ControlPanelFormWrapper as
    the form wrapper, e.g.

        from plone.app.registry.browser.form import RegistryEditForm
        from plone.app.registry.browser.form import ControlPanelFormWrapper
        from my.package.interfaces import IMySettings
        form plone.z3cform import layout

        class MyForm(RegistryEditForm):
            schema = IMySettings

        MyFormView = layout.wrap_form(MyForm, ControlPanelFormWrapper)

    Then register MyFormView as a browser view.
    """

    control_panel_view: str
    schema_prefix: Incomplete
    def getContent(self): ...
    def updateActions(self) -> None: ...
    status: Incomplete
    def handleSave(self, action) -> None: ...
    def handleCancel(self, action) -> None: ...

class ControlPanelFormWrapper(layout.FormWrapper):
    """Use this form as the plone.z3cform layout wrapper to get the control
    panel layout.
    """

    index: Incomplete
    @property
    def control_panel_url(self): ...
