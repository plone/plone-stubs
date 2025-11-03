from _typeshed import Incomplete

class ConfigurationChangedEvent:
    context: Incomplete
    data: Incomplete
    def __init__(self, context, data) -> None: ...

def handleConfigurationChangedEvent(event) -> None: ...
def handle_enable_self_reg(obj, event) -> None:
    """Additional configuration when the ``enable_self_reg``
    setting is updated in the ``Security```control panel.

    If the setting is enabled, the ``Add portal member`` permission is
    added to ``Anonymous`` role to allow self registration for anonymous
    users. If the setting is disabled, this permission is removed.
    """

def handle_enable_user_folders(obj, event) -> None:
    """Additional configuration when the ``enable_user_folders``
    setting is updated in the ``Security```control panel.

    If the setting is enabled, a new user action is added with a link to
    the personal folder. If the setting is disabled, the action is hidden.
    """

def handle_use_email_as_login(obj, event) -> None:
    """Additional configuration when the ``use_email_as_login``
    setting is updated in the ``Security```control panel.

    If the setting is enabled, existing users' login names are migrated
    to email. If the setting is disabled, then the login names are migrated
    back to user ids.
    """
