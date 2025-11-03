from plone.app.z3cform.widgets.text import TextWidget

class EmailWidget(TextWidget):
    """Implementation of dumb email widget."""

    klass: str

def EmailFieldWidget(field, request): ...
