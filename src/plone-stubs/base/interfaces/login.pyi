from _typeshed import Incomplete
from plone.z3cform.interfaces import IWrappedForm
from zope.interface import Interface

class IRedirectAfterLogin(Interface):
    """Redirect after login adapters should provide this interface"""

class IForcePasswordChange(Interface):
    """Hook point to customize forcing a password change"""

class IInitialLogin(Interface):
    """Hook point to customize what happens the first time a user logs into
    the site"""

class ILogin(Interface):
    """Login form schema"""

    login: Incomplete
    password: Incomplete

class ILoginForm(IWrappedForm):
    """Login form marker interface"""

class ILoginFormSchema(Interface):
    """Login form schema"""

    ac_name: Incomplete
    ac_password: Incomplete
    came_from: Incomplete

class ILoginHelpForm(IWrappedForm):
    """Login Help form marker interface"""

class ILoginHelpFormSchema(Interface):
    """Login Help form schema"""

    reset_password: Incomplete
    recover_username: Incomplete
