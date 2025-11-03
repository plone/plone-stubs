from _typeshed import Incomplete

import z3c.form.browser.checkbox

class SingleCheckBoxWidget(z3c.form.browser.checkbox.SingleCheckBoxWidget):
    ignoreContext: bool
    def update(self) -> None: ...
    terms: Incomplete
    def updateTerms(self): ...
    def extract(self, default=..., setErrors: bool = True): ...

def SingleCheckBoxFieldWidget(field, request): ...

singlecheckboxwidget_factory = SingleCheckBoxFieldWidget
