from _typeshed import Incomplete

import z3c.form.form
import z3c.form.widget
import zope.publisher.browser

def path(filename): ...

class FormTemplateFactory(z3c.form.form.FormTemplateFactory):
    """Form template factory that will use Chameleon if installed (via
    five.pt), or the Zope 2 ViewPageTemplateFile from Products.Five if not.

    You can use this for a wrapped form, but not for a form that is going
    to be rendered as a standalone view. Use ZopeTwoFormTemplateFactory for
    that instead.
    """

    template: Incomplete
    def __init__(
        self, filename, contentType: str = "text/html", form=None, request=None
    ) -> None: ...

class ZopeTwoFormTemplateFactory(z3c.form.form.FormTemplateFactory):
    """Form template factory for Zope 2 page templates.

    Use this for any form which is going to be rendered as a view, or any
    form wrapper view.
    """

    template: Incomplete
    def __init__(
        self, filename, contentType: str = "text/html", form=None, request=None
    ) -> None: ...
    def __call__(self, form, request): ...

class ZopeTwoWidgetTemplateFactory(z3c.form.widget.WidgetTemplateFactory):
    """A variant of z3c.form's widget.WidgetTemplateFactory which uses Zope 2
    page templates. This should only be necessary if you strictly need the
    extra Zope 2-isms of Five's ViewPageTemplateFile.
    """

    template: Incomplete
    def __init__(
        self,
        filename,
        contentType: str = "text/html",
        context=None,
        request=None,
        view=None,
        field=None,
        widget=None,
    ) -> None: ...

class Macros(zope.publisher.browser.BrowserView):
    def __getitem__(self, key): ...

layout_factory: Incomplete
wrapped_form_factory: Incomplete
standalone_form_factory: Incomplete
subform_factory: Incomplete
