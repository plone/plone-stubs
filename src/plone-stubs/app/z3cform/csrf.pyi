from z3c.form.button import ButtonActions

class AuthenticatedButtonActions(ButtonActions):
    """z3c.form action manager that checks Plone's CSRF authenticator.

    The check is performed if the form's enableCSRFProtection attribute is
    True.
    """
    def execute(self) -> None: ...
