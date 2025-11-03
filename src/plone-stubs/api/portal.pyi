from datetime import date
from datetime import datetime
from plone.base.interfaces import INavigationRoot
from plone.dexterity.content import DexterityContent
from Products.CMFPlone.Portal import PloneSite
from typing import Any
from zope.interface.interface import InterfaceClass
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.schema.vocabulary import SimpleVocabulary

PRINTINGMAILHOST_ENABLED: bool
MISSING: object

def get() -> PloneSite:
    """Get the Plone portal object out of thin air.

    :returns: Plone portal object
    :raises: CannotGetPortalError
    """

def get_navigation_root(context: Any) -> INavigationRoot:
    """Get the navigation root object for the context.

    :param context: [required] Context on which to get the navigation root.
    :returns: Navigation Root
    """

def get_tool(name: str) -> Any:
    """Get a portal tool in a simple way.

    :param name: [required] Name of the tool you want.
    :returns: The tool that was found by name
    :raises: MissingParameterError, InvalidParameterError
    """

def send_email(
    recipient: str,
    subject: str,
    body: str | bytes,
    sender: str | None = None,
    immediate: bool = False,
) -> None:
    """Send an email.

    :param sender: Email sender, 'from' field. If not set, portal default will be used.
    :param recipient: [required] Email recipient, 'to' field.
    :param subject: [required] Subject of the email.
    :param body: [required] Body text of the email
    :param sender: Email sender, 'from' field. If not set, portal default will be used.
    :param immediate: Send immediate or queued at transaction commit time.
    :raises: ValueError
    """

def get_localized_time(
    datetime: datetime | date | Any,
    long_format: bool = False,
    time_only: bool = False,
) -> str:
    """Display a date/time in a user-friendly way.

    :param datetime: [required] Date/time to display.
    :param long_format: When true, show long date format.
    :param time_only: When true, show only the time.
    :returns: Localized time
    :raises: ValueError
    """

def show_message(
    message: str,
    request: IBrowserRequest | None = None,
    type: str = "info",
) -> None:
    """Display a status message.

    :param message: [required] Message to show.
    :param request: Request.
    :param type: Message type. Possible values: 'info', 'warn', 'error'
    :raises: ValueError
    """

def get_registry_record(
    name: str,
    interface: InterfaceClass | None = None,
    default: Any = ...,
) -> Any:
    """Get a record value from plone.app.registry.

    :param name: [required] Name
    :param interface: interface whose attributes are plone.app.registry settings
    :param default: The value returned if the record is not found
    :returns: Registry record value
    :raises: InvalidParameterError
    """

def set_registry_record(
    name: str,
    value: Any,
    interface: InterfaceClass | None = None,
) -> None:
    """Set a record value in the plone.app.registry.

    :param name: [required] Name of the record
    :param value: [required] Value to set
    :param interface: interface whose attributes are plone.app.registry settings
    :raises: InvalidParameterError
    """

def get_default_language() -> str:
    """Return the default language.

    :returns: language identifier
    """

def get_current_language(context: DexterityContent | None = None) -> str:
    """Return the current negotiated language.

    :param context: context object
    :returns: language identifier
    """

def translate(
    msgid: str | Any,
    domain: str = "plone",
    lang: str | None = None,
) -> str:
    """Translate a message into a given language.

    :param msgid: [required] message to translate
    :param domain: i18n domain to use
    :param lang: target language
    :returns: translated message
    """

def get_vocabulary(
    name: str,
    context: Any = None,
) -> SimpleVocabulary:
    """Return a vocabulary object with the given name.

    :param name: [required] Name of the vocabulary.
    :param context: Context to be applied to the vocabulary. Default: portal root.
    :returns: A SimpleVocabulary instance that implements IVocabularyTokenized.
    :raises: InvalidParameterError
    """

def get_vocabulary_names() -> list[str]:
    """Return a list of vocabulary names.

    :returns: A sorted list of vocabulary names.
    """
