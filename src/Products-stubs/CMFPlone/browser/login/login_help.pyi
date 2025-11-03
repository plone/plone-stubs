from _typeshed import Incomplete
from z3c.form import form

SEND_USERNAME_TEMPLATE: Incomplete
log: Incomplete

class RequestResetPassword(form.Form):
    id: str
    label: str
    fields: Incomplete
    ignoreContext: bool
    render: Incomplete
    def updateActions(self) -> None: ...
    def updateWidgets(self) -> None: ...
    status: Incomplete
    def handleResetPassword(self, action) -> None: ...
    def use_email_as_login(self): ...

class RequestUsername(form.Form):
    id: str
    label: str
    fields: Incomplete
    ignoreContext: bool
    render: Incomplete
    def updateActions(self) -> None: ...
    status: Incomplete
    def handleGetUsername(self, action) -> None: ...
    def send_username(self, portal, userinfo) -> None: ...
    def encode_mail_header(self, text):
        """Encodes text into correctly encoded email header"""
    def encoded_mail_sender(self):
        """returns encoded version of Portal name <portal_email>"""

class LoginHelpForm(form.EditForm):
    """Implementation of the login help form"""

    subforms: Incomplete
    id: str
    label: Incomplete
    ignoreContext: bool
    def render(self): ...
    def can_reset_password(self): ...
    def can_retrieve_username(self): ...
    def update(self) -> None: ...
    def use_email_as_login(self): ...
