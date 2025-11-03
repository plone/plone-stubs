from _typeshed import Incomplete
from zope.interface import Interface

_: Incomplete
PloneMessageFactory: Incomplete

class ILanguageUtility(Interface):
    """Marker interface for the portal_languages tool."""

class INegotiateLanguage(Interface):
    """Result of language negotiation"""

    language: Incomplete
    default_language: Incomplete
    language_list: Incomplete

class ILanguageSchema(Interface):
    default_language: Incomplete
    available_languages: Incomplete
    use_combined_language_codes: Incomplete
    display_flags: Incomplete
    always_show_selector: Incomplete
    use_content_negotiation: Incomplete
    use_path_negotiation: Incomplete
    use_cookie_negotiation: Incomplete
    authenticated_users_only: Incomplete
    set_cookie_always: Incomplete
    use_subdomain_negotiation: Incomplete
    use_cctld_negotiation: Incomplete
    use_request_negotiation: Incomplete
