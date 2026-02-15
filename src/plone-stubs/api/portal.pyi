from datetime import date
from datetime import datetime
from DateTime import DateTime
from plone.base.interfaces import INavigationRoot
from plone.dexterity.content import DexterityContent
from Products.CMFCore.interfaces import IActionsTool
from Products.CMFCore.interfaces import ICatalogTool
from Products.CMFCore.interfaces import IMembershipTool
from Products.CMFCore.interfaces import ITypesTool
from Products.CMFCore.interfaces import IURLTool
from Products.CMFCore.interfaces import IWorkflowTool
from Products.CMFPlone.Portal import PloneSite
from typing import Any
from typing import Literal
from typing import overload
from zope.interface.interface import InterfaceClass
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.schema.vocabulary import SimpleVocabulary

PRINTINGMAILHOST_ENABLED: bool
MISSING: object

def get() -> PloneSite:
    """Get the Plone portal object out of thin air.

    :returns: Plone portal object.
    :rtype: PloneSite
    """
def get_navigation_root(context: Any) -> INavigationRoot:
    """Get the navigation root object for the context.

    :param context: [required] Context on which to get the navigation root.
    :type context: context object
    :returns: Navigation Root.
    :rtype: INavigationRoot
    """
@overload
def get_tool(name: Literal["portal_catalog"]) -> ICatalogTool: ...
@overload
def get_tool(name: Literal["portal_workflow"]) -> IWorkflowTool: ...
@overload
def get_tool(name: Literal["portal_membership"]) -> IMembershipTool: ...
@overload
def get_tool(name: Literal["portal_types"]) -> ITypesTool: ...
@overload
def get_tool(name: Literal["portal_url"]) -> IURLTool: ...
@overload
def get_tool(name: Literal["portal_actions"]) -> IActionsTool: ...
@overload
def get_tool(name: str) -> Any:
    """Get a portal tool by name.

    :param name: [required] Name of the tool to get.
    :type name: string
    :returns: The tool.
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
    :type sender: string
    :param recipient: [required] Email recipient, 'to' field.
    :type recipient: string
    :param subject: [required] Subject of the email.
    :type subject: string
    :param body: [required] Body text of the email.
    :type body: string or bytes
    :param immediate: Send immediate or queued at transaction commit time.
    :type immediate: boolean
    """
def get_localized_time(
    datetime: datetime | date | DateTime,
    long_format: bool = False,
    time_only: bool = False,
) -> str:
    """Display a date/time in a user-friendly way.

    :param datetime: [required] Date/time to display.
    :type datetime: DateTime, datetime or date
    :param long_format: When true, show long date format.
    :type long_format: boolean
    :param time_only: When true, show only the time.
    :type time_only: boolean
    :returns: Localized time.
    :rtype: string
    """
def show_message(
    message: str,
    request: IBrowserRequest | None = None,
    type: Literal["info", "warn", "error"] = "info",
) -> None:
    """Display a status message.

    :param message: [required] Message to show.
    :type message: string
    :param request: Request. Defaults to current request.
    :type request: IBrowserRequest
    :param type: Message type. Possible values: 'info', 'warn', 'error'.
    :type type: Literal["info", "warn", "error"]
    """
def get_registry_record(
    name: str,
    interface: InterfaceClass | None = None,
    default: Any = ...,
) -> Any:
    """Get a record value from plone.app.registry.

    :param name: [required] Name of the record.
    :type name: string
    :param interface: Interface whose attributes are plone.app.registry settings.
    :type interface: InterfaceClass
    :param default: The value returned if the record is not found.
    :type default: anything
    :returns: Registry record value.
    """
def set_registry_record(
    name: str,
    value: Any,
    interface: InterfaceClass | None = None,
) -> None:
    """Set a record value in the plone.app.registry.

    :param name: [required] Name of the record.
    :type name: string
    :param value: [required] Value to set.
    :type value: python primitive
    :param interface: Interface whose attributes are plone.app.registry settings.
    :type interface: InterfaceClass
    """
def get_default_language() -> str:
    """Return the default language.

    :returns: Language identifier.
    :rtype: string
    """
def get_current_language(context: DexterityContent | None = None) -> str:
    """Return the current negotiated language.

    :param context: Context object.
    :type context: Content object
    :returns: Language identifier.
    :rtype: string
    """
def translate(
    msgid: str,
    domain: str = "plone",
    lang: str | None = None,
) -> str:
    """Translate a message into a given language.

    :param msgid: [required] Message to translate.
    :type msgid: string
    :param domain: i18n domain to use.
    :type domain: string
    :param lang: Target language.
    :type lang: string
    :returns: Translated message.
    :rtype: string
    """
def get_vocabulary(
    name: str,
    context: Any = None,
) -> SimpleVocabulary:
    """Return a vocabulary object with the given name.

    :param name: [required] Name of the vocabulary.
    :type name: string
    :param context: Context to be applied to the vocabulary. Default: portal root.
    :type context: object
    :returns: A SimpleVocabulary instance that implements IVocabularyTokenized.
    :rtype: SimpleVocabulary
    """
def get_vocabulary_names() -> list[str]:
    """Return a list of vocabulary names.

    :returns: A sorted list of vocabulary names.
    :rtype: list of strings
    """
