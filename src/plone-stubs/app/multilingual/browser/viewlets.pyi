from _typeshed import Incomplete
from plone.app.layout.viewlets.common import ViewletBase

class OneLanguageConfiguredNoticeViewlet(ViewletBase):
    """Notice the user that PAM is installed and only one language
    is configured.
    """

    available: bool
    def render(self): ...
    def update(self) -> None: ...

class AddFormIsATranslationViewlet(ViewletBase):
    """Notice the user that this add form is a translation"""

    available: bool
    def language(self): ...
    tool: Incomplete
    def languages(self):
        """Returns list of languages."""
    def language_name(self, lang_code): ...
    def render(self): ...
    def returnURL(self): ...
    lang: Incomplete
    origin: Incomplete
    def update(self) -> None: ...

class AlternateLanguagesViewlet(ViewletBase):
    """Notice search engines about alternates languages of current
    content item
    """

    alternatives: Incomplete
    def get_alternate_languages(self):
        """Cache relative urls only. If we have multilingual sites
        and multi domain site caching absolute urls will result in
        very inefficient caching. Build absolute url in template.
        """
    alternates: Incomplete
    def update(self) -> None: ...
    @property
    def available(self): ...
    def render(self): ...
